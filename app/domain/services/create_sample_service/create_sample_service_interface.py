from abc import ABC, abstractmethod


class CreateSampleServiceInterface(ABC):
    @abstractmethod
    async def execute(self):
        pass
