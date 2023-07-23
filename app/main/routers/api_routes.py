from starlette.routing import Mount
from starlette.routing import Route

from app.main.routers.create_sample_router import create_sample
from app.main.routers.create_karaoke_music_router import create_karaoke_music


routes = [Mount("/v1/api/sample", routes=[Route("/create", create_sample, methods=["POST"])]),
          Mount("/v1/api/karaoke", routes=[Route("/create", create_karaoke_music, methods=["POST"])])]
