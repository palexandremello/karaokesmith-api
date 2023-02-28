from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from domain.services.create_sample_service.sampler_interface import SamplerInterface
from domain.utils.response import Response


class CreateSampleService(CreateSampleServiceInterface):
    def __init__(self, sampler: SamplerInterface) -> None:
        self.sampler = sampler
        self.__list_path = []

    async def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        try:
            list_of_samples = await self.sampler.execute(mp3_file, minutes_per_sample)

            for mp3_file in list_of_samples:
                self.__list_path.append(mp3_file.path)

            sample = Sample(audio_option=mp3_file, minutes_per_sample=minutes_per_sample, path=self.__list_path)

            return Response(success=True, body=sample)

        except Exception as error:
            return Response(success=False, body=str(error))
