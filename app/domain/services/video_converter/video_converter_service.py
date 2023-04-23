from app.domain.entities.audio_media import AudioMedia
from app.domain.entities.video_source import VideoSource
from app.domain.services.video_converter.converter_interface import ConverterInterface
from .video_converter_service_interface import VideoConverterServiceInterface


class VideoConverterService(VideoConverterServiceInterface):
    def __init__(self, converter: ConverterInterface) -> None:
        self.converter = converter

    async def execute(self, video: VideoSource) -> AudioMedia:
        path = await self.converter.execute(video)
        audio_media = AudioMedia.from_dict({"path": path, "audio_format": "mp3"})
        return audio_media
