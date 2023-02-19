
from typing import Union
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface
from domain.utils.service_response import ServiceResponse

class Mp3FileService(Mp3FileServiceInterface):
    def __init__(self, validator: Mp3FileValidatorInterface) -> None:
        self.validator = validator
    

    async def validate_mp3_file(self, path: str) -> ServiceResponse:
        try:
            await self.validator.validate(path)
            return ServiceResponse(success=True, error_message=None)
        except (FileNotFoundError, ValueError) as error:
            return ServiceResponse(success=False, error_message=str(error))