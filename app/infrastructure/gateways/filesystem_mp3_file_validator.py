import os
import aiofiles
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface


class FileSystemMp3FileValidator(Mp3FileValidatorInterface):
    def __init__(self) -> None:
        self.__mp3_metadata = b"ID3"
        self.mime_type = ".mp3"

    async def validate(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")

        if not path.endswith(self.mime_type):
            raise ValueError("File is not an MP3 file")

        async with aiofiles.open(path, mode="rb") as f:
            data = await f.read(10)
            if not data[:3] == self.__mp3_metadata:
                raise ValueError("File is not a valid MP3 file")
