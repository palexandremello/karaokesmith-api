import dataclasses

@dataclasses.dataclass
class Mp3File:
    name: str
    path: str


    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(**dictionary)
    
    def to_dict(self):
        return dataclasses.asdict(self)