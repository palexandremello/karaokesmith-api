
from abc import ABC, abstractmethod


class Mp3FileValidatorInterface(ABC):

    @abstractmethod
    async def validate(cls, path: str) -> None:
        pass