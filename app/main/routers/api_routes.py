from starlette.routing import Mount
from starlette.routing import Route

from app.main.routers.create_sample_router import create_sample


routes = [Mount("/v1/api/sample", routes=[Route("/create", create_sample, methods=["POST"])])]
