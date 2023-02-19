


from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ServiceResponse:
    success: bool
    error_message: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)