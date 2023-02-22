from abc import ABC, abstractmethod
from domain.entities.youtube_audio import YoutubeAudio
from domain.utils.response import Response


class YoutubeAudioUseCaseInterface(ABC):
    @abstractmethod
    async def execute(self, video_url: str) -> Response[YoutubeAudio]:
        pass
