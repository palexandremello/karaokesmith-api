from abc import ABC, abstractmethod
from app.domain.entities.audio_media import AudioMedia
from app.domain.entities.video_source import VideoSource
from app.domain.utils.response import Response


class VideoConverterServiceInterface(ABC):
    @abstractmethod
    async def execute(self, video: VideoSource) -> Response[AudioMedia]:
        pass
