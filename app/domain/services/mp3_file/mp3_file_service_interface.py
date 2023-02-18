
from abc import ABC, abstractmethod
from typing import Union


class Mp3FileServiceInterface(ABC):

    @abstractmethod
    async def validate_mp3_file(cls, path: str) -> Union[Exception, None]:
        pass