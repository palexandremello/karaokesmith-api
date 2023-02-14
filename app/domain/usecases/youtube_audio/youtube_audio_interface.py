

from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.youtube_audio import YoutubeAudio


class YoutubeAudioUseCaseInterface(ABC):
    @abstractmethod
    def execute(cls, link: str, name: Optional[str] = None) -> YoutubeAudio:
        pass