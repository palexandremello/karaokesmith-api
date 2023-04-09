from abc import ABC, abstractmethod
from application.helpers.http.request import HttpRequest
from application.helpers.http.response import HttpResponse


class ControllerInterface(ABC):
    @abstractmethod
    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
