from model.schedule import Schedule
from repository import schedule_repository


def get_schedule(group: str):
    return schedule_repository.find_schedule(group)


def add_schedule(schedule: Schedule):
    schedule_repository.save_schedule(schedule)
