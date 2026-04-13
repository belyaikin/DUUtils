from pymongo.synchronous.mongo_client import MongoClient

from env import environment_variables
from model.schedule import Schedule, schedule_to_dictionary

MONGO_CLIENT = MongoClient(environment_variables.MONGO_DB_CONNECTION_URI)


def save_schedule(schedule: Schedule):
    schedule_dictionary = schedule_to_dictionary(schedule)

    MONGO_CLIENT["duutils"]["schedules"].insert_one(schedule_dictionary)


def find_schedule(group: str):
    result = MONGO_CLIENT["duutils"]["schedules"].find_one({"group": group})
    if result:
        result["_id"] = str(result["_id"])
    return result
