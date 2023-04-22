from io import BytesIO
import os
from pydub import AudioSegment
from typing import List
from app.domain.entities.mp3_file import Mp3File
from app.domain.services.create_sample_service.sampler_interface import SamplerInterface


class PydubSampler(SamplerInterface):
    def __init__(self) -> None:
        self.samples = []
        self.__samples_dir = f"{os.getcwd()}/samples/"

    def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> List[Mp3File]:
        audio = AudioSegment.from_file(BytesIO(mp3_file.path), format="mp3")

        samples_size = minutes_per_sample * 60 * 1000

        total_of_samples = len(audio) // samples_size

        for each_sample in range(total_of_samples):
            start = each_sample * samples_size
            end = (each_sample + 1) * samples_size

            sample = audio[start:end]
            sample_name = f"{mp3_file.name}_{each_sample}.mp3"
            #            print(sample_name)
            path = f"{self.__samples_dir}/{sample_name}"
            mp3_file = Mp3File(name=sample_name, path=path)
            self.samples.append(mp3_file)

            sample.export(path, format="mp3")

        print(self.samples)
        return self.samples
