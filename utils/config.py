import os

from dotenv import load_dotenv


load_dotenv()


def get(variable_name: str, variable_type: type = str):
    value = os.getenv(variable_name)
    if value is None:
        return None
    return variable_type(value)
