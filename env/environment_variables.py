import os

from dotenv import load_dotenv

load_dotenv()


def _get_variable(name: str) -> str:
    variable = os.getenv(name)

    if variable is None:
        raise ValueError(f"Specified environment variable ({name}) does not exist")
    else:
        return variable


MONGO_DB_CONNECTION_URI = _get_variable("MONGO_CONNECTION_URI")
DIGITAL_UNIVERSITY_BEARER_TOKEN = _get_variable("DIGITAL_UNIVERSITY_BEARER_TOKEN")
