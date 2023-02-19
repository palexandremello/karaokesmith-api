
from abc import ABC, abstractmethod
from domain.utils.service_response import ServiceResponse


class Mp3FileServiceInterface(ABC):

    @abstractmethod
    async def validate_mp3_file(self, path: str) -> ServiceResponse:
        pass