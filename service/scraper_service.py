import os
import time
from datetime import date
from json import loads

import requests
from dotenv import load_dotenv

from model.faculties import BachelorFaculties
from model.lesson import Lesson
from model.schedule import Schedule
from repository.schedule_repository import save_schedule

load_dotenv()

BEARER_TOKEN = os.environ["BEARER_TOKEN"]

SCHEDULE_API_URL: str = (
    "https://du.astanait.edu.kz:8765/astanait-schedule-module/api/v1/schedule"
)


def scrape_schedules(request_timeout=1):
    for faculty in BachelorFaculties:
        for year in range(date.today().year - 3, date.today().year):
            current_group_number = 1

            while True:
                current_group_code = f"{faculty.value}-{year % 100}{current_group_number if current_group_number >= 10 else f'0{current_group_number}'}"

                try:
                    url = f"{SCHEDULE_API_URL}/groupName/{current_group_code}"

                    print(f"Sending request to: {url}")

                    response = requests.get(
                        url, headers={"Authorization": f"Bearer {BEARER_TOKEN}"}
                    )

                    if response.status_code == 401:
                        raise Exception("Bearer token is invalid")

                    data = response.json()

                    if data["body"] == [] and current_group_number == 1:
                        print(f"No data for {year} groups, skipping to {year + 1}")

                        time.sleep(request_timeout)

                        year += 1
                        break

                    if data["body"] == []:
                        print(
                            f"Recorded data for {year} groups, skipping to {year + 1}"
                        )

                        time.sleep(request_timeout)

                        year += 1
                        break

                    lessons: list[Lesson] = []

                    # THIS IS BROKEN!!!

                    for lesson in data["body"]:
                        lessons.append(
                            Lesson(
                                subject=lesson["subject"],
                                tutor=lesson["tutor"],
                                room=lesson["room"],
                                type=lesson["lesson_type"],
                                teams_meeting_url=lesson["teamsMeetingUrl"],
                                day_of_the_week=next(
                                    (
                                        loads(lesson["days"])["daysname"][i]
                                        for i, d in enumerate(
                                            loads(lesson["days"])["days"]
                                        )
                                        if d == lesson["classtime_day"]
                                    ),
                                    None,
                                ),
                                from_to=next(
                                    (
                                        f"{t['start']} - {t['finish']}"
                                        for t in loads(lesson["days"])["time"]
                                        if t["id"] == lesson["classtime_time"]
                                    ),
                                    None,
                                ),
                            )
                        )

                    save_schedule(Schedule(group=current_group_code, lessons=lessons))

                    print(f"Recored schedule for group {current_group_code}!")

                    time.sleep(request_timeout)
                except Exception as e:
                    print(f"Error occured: {e}")

                    time.sleep(request_timeout)
                    break

                current_group_number += 1
            print(f"Finished saving schedules for year {year - 1}!")
        print(f"Finished saving schedules for {faculty.name} faculty!")
    print("Done scraping! Check your new MongoDB collection :)")
