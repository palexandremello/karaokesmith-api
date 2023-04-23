from app.main.adapters.starlette_adapter import starlette_adapter
from starlette.responses import JSONResponse

from app.main.composite.create_sample_composite import create_sample_composer
from app.main.adapters.starlette_request_adapter import StarletteRequestAdapter


async def create_sample(request):
    message = {}

    response = await starlette_adapter(
        request=request, api_controller=create_sample_composer(), request_adapter=StarletteRequestAdapter()
    )

    if response.status_code < 300:
        message = {"type": "samples", "body": "Samples was created with success"}
        return JSONResponse(message, status_code=response.status_code)

    return JSONResponse(
        {"error": {"status": response.status_code, "title": str(response.body["error"])}},
        status_code=response.status_code,
    )
