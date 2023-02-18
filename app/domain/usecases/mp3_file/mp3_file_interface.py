from abc import ABC, abstractmethod
from domain.entities.mp3_file import Mp3File
from domain.utils.use_case_response import UseCaseResponse


class Mp3FileUseCaseInterface(ABC):

    @abstractmethod
    async def execute(cls, name: str, path: str) -> UseCaseResponse[Mp3File]:
        pass
