from starlette.requests import Request
from app.application.adapters.request_adapter_interface import RequestAdapterInterface
from app.application.controllers.interface.controller_interface import ControllerInterface as Controller
from app.application.helpers.http.response import HttpResponse
from app.errors.http import HttpErrors


async def starlette_adapter(
    request: Request, api_controller: Controller, request_adapter: RequestAdapterInterface
) -> any:
    """Adapter pattern to FastAPI
    :param - FastAPI Request
    :api_controller: Controller function
    """
    try:
        http_request = await request_adapter.adapt(request)
    except Exception as error:
        print(error)
        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    try:
        response = await api_controller.handle(http_request)
        return response

    except Exception as error:
        print(error)
        print("testando")
        http_error = HttpErrors.error_500()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
