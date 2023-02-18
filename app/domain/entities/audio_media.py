
from dataclasses import asdict, dataclass
from enum import Enum

class AudioFormat(Enum):
    MP3 = "mp3"
    WAV = "wav"


@dataclass
class AudioMedia:
    path: str
    audio_format: AudioFormat

    @classmethod
    def from_dict(cls, dictionary: dict) -> "AudioMedia":
        dictionary['audio_format'] = AudioFormat(dictionary['audio_format'])
        return cls(**dictionary)
    
    def to_dict(self) -> dict:
        dictionary = asdict(self)
        dictionary['audio_format'] = self.audio_format.value
        return dictionary
