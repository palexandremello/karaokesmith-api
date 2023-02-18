import dataclasses

@dataclasses.dataclass
class Mp3File:
    name: str
    path: str

    @classmethod
    def from_dict(cls, dictionary: dict) -> "Mp3File":
        return cls(**dictionary)
    
    def to_dict(self) -> dict:
        return dataclasses.asdict(self)