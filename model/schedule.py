from model.lesson import Lesson


class Schedule:
    def __init__(self, group, day, lessons: list[Lesson]):
        self.group = group
        self.day = day
        self.lessons = lessons


def schedule_to_dictionary(schedule: Schedule):
    return {
        "group": schedule.group,
        "day": schedule.day,
        "lessons": [
            {
                "subject": lesson.subject,
                "tutor": lesson.tutor,
                "room": lesson.room,
                "type": lesson.type,
                "teams_meeting_url": lesson.teams_meeting_url,
                "time_from": lesson.time_from,
                "time_to": lesson.time_to,
            }
            for lesson in schedule.lessons
        ],
    }
