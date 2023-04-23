from starlette.config import Config

config = Config(".env")

LOGGER_APP_NAME = config("LOGGER_APP", default="app")
SAMPLES_DIRECTORY = config("SAMPLES_DIRECTORY", default="samples")
MONGODB_URI = config("MONGODB_URI", default="")
