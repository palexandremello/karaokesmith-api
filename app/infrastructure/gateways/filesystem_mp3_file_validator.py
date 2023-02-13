import os
from typing import Union
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface


class FileSystemMp3FileValidator(Mp3FileValidatorInterface):
    def __init__(self) -> None:
        self.__mp3_metadata = b'ID3'
        self.mime_type = ".mp3"

    def validate(self, path: str) -> Union[None, Exception]:

        if not os.path.exists(path):
            return FileNotFoundError("File not found")
        
        if not path.endswith(self.mime_type):
            return ValueError("File is not an MP3 file")
        try:

           with open(path, 'rb') as f:
               data = f.read(10)
               if not data[:3] == self.__mp3_metadata:
                   return ValueError("File is not a valid MP3 file")
                   
        except Exception:
            return ValueError("MP3 file is broken")
