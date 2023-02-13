
from abc import ABC, abstractmethod
from typing import Union


class Mp3FileValidatorInterface(ABC):

    @abstractmethod
    def validate(cls, path: str) -> Union[None, Exception]:
        pass