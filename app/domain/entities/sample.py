from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class Sample:
    name: Optional[str] = None
    content: bytes = None
    path: Optional[str] = None
    id: Optional[str] = None

    @classmethod
    def from_dict(cls, dictionary: dict) -> "Sample":
        return cls(**dictionary)

    def to_dict(self) -> dict:
        return asdict(self)
