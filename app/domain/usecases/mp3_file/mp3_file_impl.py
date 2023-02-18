from domain.entities.mp3_file import Mp3File
from domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.utils.use_case_response import UseCaseResponse


class Mp3FileUseCase(Mp3FileUseCaseInterface):
    def __init__(self, mp3_file_service: Mp3FileServiceInterface) -> None:
        self.mp3_file_service  = mp3_file_service
    
    async def execute(self, name: str, path: str) -> UseCaseResponse[Mp3File]:
        try:
            await self.mp3_file_service.validate_mp3_file(path)
            mp3_file = Mp3File(name=name, path=path)
            return UseCaseResponse(success=True, body=mp3_file)
        
        except Exception as errorr:
            return UseCaseResponse(success=False, body=str(errorr))            