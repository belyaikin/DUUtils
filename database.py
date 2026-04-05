import os

from dotenv import load_dotenv
from pymongo import MongoClient

from models import Schedule

load_dotenv()

collection = MongoClient(os.environ["MONGO_CONNECTION_URI"])["duutils"]["schedules"]


def schedule_to_dictionary(schedule: Schedule):
    return {
        "group": schedule.group,
        "lessons": [
            {
                "subject": lesson.subject,
                "tutor": lesson.tutor,
                "room": lesson.room,
                "type": lesson.type,
                "teams_meeting_url": lesson.teams_meeting_url,
                "day_of_the_week": lesson.day_of_the_week,
                "from_to": lesson.from_to,
            }
            for lesson in schedule.lessons
        ],
    }


def save_schedule(schedule: Schedule):
    collection.insert_one(schedule_to_dictionary(schedule))


def find_schedule(group: str):
    result = collection.find_one({"group": group})
    if result:
        result["_id"] = str(result["_id"])
    return result
