from dataclasses import asdict, dataclass
from typing import Optional, Union
from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.youtube_audio import YoutubeAudio


@dataclass
class Sample:
    audio_option: Union[Mp3File, YoutubeAudio]
    name: Optional[str] = None
    content: bytes = None
    path: Optional[str] = None
    id: Optional[str] = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> "Sample":
        return cls(**dictionary)

    def to_dict(self) -> dict:
        return asdict(self)
