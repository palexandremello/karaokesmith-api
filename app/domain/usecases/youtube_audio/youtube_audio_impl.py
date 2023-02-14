
from typing import Optional
from domain.entities.youtube_audio import YoutubeAudio
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface


class YoutubeAudioUseCaseImpl(YoutubeAudioUseCaseInterface):
    def __init__(self) -> None:
        pass

    def execute(cls, link: str, name: Optional[str] = None) -> YoutubeAudio:
        return None