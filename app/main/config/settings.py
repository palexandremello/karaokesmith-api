from starlette.config import Config

config = Config(".env")

LOGGER_APP_NAME = config("LOGGER_APP", default="app")
