from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.sample import Sample
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.services.create_sample_service.sampler_interface import SamplerInterface
from app.domain.utils.response import Response


class CreateSampleService(CreateSampleServiceInterface):
    def __init__(
        self,
        sampler: SamplerInterface,
    ) -> None:
        self.sampler = sampler

    async def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        try:
            samples = await self.sampler.execute(mp3_file, minutes_per_sample)
            return Response(success=True, body=samples)
        except Exception as error:
            return Response(success=False, body=str(error))
