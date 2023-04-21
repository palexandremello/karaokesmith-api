from app.domain.entities.mp3_file import Mp3File
from app.domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface
from app.domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from app.domain.utils.response import Response


class Mp3FileUseCase(Mp3FileUseCaseInterface):
    def __init__(self, mp3_file_service: Mp3FileServiceInterface) -> None:
        self.mp3_file_service = mp3_file_service

    async def execute(self, name: str, path: str) -> Response[Mp3File]:
        try:
            await self.mp3_file_service.validate_mp3_file(path)
            mp3_file = Mp3File(name=name, path=path)
            return Response(success=True, body=mp3_file)

        except Exception as errorr:
            return Response(success=False, body=str(errorr))
