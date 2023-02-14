import dataclasses
from typing import Optional
from domain.entities.mp3_file import Mp3File

@dataclasses.dataclass
class YoutubeAudio:
    link: str
    mp3_file: Optional[Mp3File] = None


    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(**dictionary)

    
    def to_dict(self):
        return dataclasses.asdict(self)