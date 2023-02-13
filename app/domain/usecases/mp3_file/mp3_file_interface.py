from abc import ABC, abstractmethod
from typing import Union

from domain.entities.mp3_file import Mp3File


class Mp3FileInterface(ABC):

    @abstractmethod
    def execute(cls, name: str, path: str) -> Union[Exception, Mp3File]:
        pass
