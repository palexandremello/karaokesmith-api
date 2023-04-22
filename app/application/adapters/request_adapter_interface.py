from abc import ABC, abstractmethod

from app.application.helpers.http.request import HttpRequest


class RequestAdapterInterface(ABC):
    @abstractmethod
    async def adapt(self, request: any) -> HttpRequest:
        pass
