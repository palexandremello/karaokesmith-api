
from abc import ABC, abstractmethod
from domain.utils.response import Response


class Mp3FileServiceInterface(ABC):

    @abstractmethod
    async def validate_mp3_file(self, path: str) -> Response:
        pass