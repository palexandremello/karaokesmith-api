from abc import ABC, abstractmethod
from domain.entities.audio_media import AudioMedia
from domain.entities.video_source import VideoSource

from domain.utils.response import Response


class VideoToAudioConverterUseCaseInterface(ABC):
    @abstractmethod
    async def convert(self, video: VideoSource) -> Response[AudioMedia]:
        pass
