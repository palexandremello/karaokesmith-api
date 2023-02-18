
from typing import Union
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface

class Mp3FileService(Mp3FileServiceInterface):
    def __init__(self, validator: Mp3FileValidatorInterface) -> None:
        self.validator = validator
    

    async def validate_mp3_file(self, path: str) -> Union[Exception, None]:
        try:
            await self.validator.validate(path)
                    
        except Exception as error:
            return error