
from abc import ABC, abstractmethod
from typing import Union


class Mp3FileValidatorInterface(ABC):

    @abstractmethod
    async def validate(cls, path: str) -> Union[None, Exception]:
        pass