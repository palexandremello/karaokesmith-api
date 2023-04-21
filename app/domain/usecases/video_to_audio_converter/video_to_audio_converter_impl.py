from app.domain.entities.audio_media import AudioMedia
from app.domain.entities.video_source import VideoSource
from app.domain.services.video_converter.video_converter_service_interface import VideoConverterServiceInterface
from app.domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import (
    VideoToAudioConverterUseCaseInterface,
)
from app.domain.utils.response import Response


class VideoToAudioConverterUseCase(VideoToAudioConverterUseCaseInterface):
    def __init__(self, video_converter_service: VideoConverterServiceInterface) -> None:
        self.video_converter_service = video_converter_service

    async def convert(self, video: VideoSource) -> Response[AudioMedia]:
        try:
            audio = await self.video_converter_service.execute(video)
            return Response(success=True, body=audio)

        except Exception as error:
            return Response(success=False, body=str(error))
