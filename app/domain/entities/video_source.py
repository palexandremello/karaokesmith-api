

from dataclasses import dataclass, asdict


@dataclass
class VideoSource:
    title: str
    thumbnail_url: str
    path: str


    @classmethod
    def from_dict(cls, dictionary: dict) -> "VideoSource":
        return cls(**dictionary)
    
    def to_dict(self) -> dict:
        return asdict(self)