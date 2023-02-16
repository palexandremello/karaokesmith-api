
from dataclasses import dataclass, asdict
from typing import Generic, TypeVar, Union


T = TypeVar("T")

@dataclass
class UseCaseReponse(Generic[T]):
    success: bool
    body: Union[T, str]



    def to_dict(self):
        return asdict(self)