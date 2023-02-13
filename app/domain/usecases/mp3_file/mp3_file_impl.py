

from typing import Union
from domain.entities.mp3_file import Mp3File
from domain.usecases.mp3_file.mp3_file_interface import Mp3FileInterface
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface

class Mp3FileUseCaseImpl(Mp3FileInterface):
    def __init__(self, mp3_file_service: Mp3FileServiceInterface) -> None:
        self.mp3_file_service  = mp3_file_service

    def execute(self, path: str) -> Union[Exception, Mp3File]:
        response = self.mp3_file_service.validate_mp3_file(path)

        if not response:
            return Mp3File(name="musica", path=path)
        
        return response