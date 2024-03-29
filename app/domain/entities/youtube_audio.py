import dataclasses
from typing import Optional
from app.domain.entities.mp3_file import Mp3File


@dataclasses.dataclass
class YoutubeAudio:
    video_url: str
    mp3_file: Optional[Mp3File] = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> "YoutubeAudio":
        return cls(**dictionary)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
