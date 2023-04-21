from abc import ABC, abstractmethod
from app.domain.entities.mp3_file import Mp3File
from app.domain.utils.response import Response


class Mp3FileUseCaseInterface(ABC):
    @abstractmethod
    async def execute(cls, name: str, path: str) -> Response[Mp3File]:
        pass
