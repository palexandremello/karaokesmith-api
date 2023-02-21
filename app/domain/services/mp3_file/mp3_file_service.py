from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface
from domain.utils.response import Response

class Mp3FileService(Mp3FileServiceInterface):
    def __init__(self, validator: Mp3FileValidatorInterface) -> None:
        self.validator = validator
    

    async def validate_mp3_file(self, path: str) -> Response:
        try:
            await self.validator.validate(path)
            return Response(success=True, body=None)
        except (FileNotFoundError, ValueError) as error:
            return Response(success=False, body=str(error))