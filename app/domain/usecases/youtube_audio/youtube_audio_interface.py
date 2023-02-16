

from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.youtube_audio import YoutubeAudio
from domain.utils.use_case_response import UseCaseResponse


class YoutubeAudioUseCaseInterface(ABC):
    @abstractmethod
    def execute(cls, link: str, name: Optional[str] = None) -> UseCaseResponse[YoutubeAudio]:
        pass