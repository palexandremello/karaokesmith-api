import os
import pytest
from domain.entities.mp3_file import Mp3File
from infrastructure.gateways.sampler.pydub_sampler import PydubSampler


# class TestPyDubSampler:
#    file = f"{os.getcwd()}/tests/infrastructure/gateways/sampler/integrate_test_file.mp3"
#
#    @pytest.fixture
#    def pydub_sampler(self) -> PydubSampler:
#        return PydubSampler()
#
#    def test_should_be_able_to_create_sample(self, pydub_sampler: PydubSampler):
#        mp3_file = Mp3File(path=self.file, name="any_name")
#        list_of_samples = pydub_sampler.execute(mp3_file, 1)
#
#        print(list_of_samples)
#        assert len(list_of_samples) == 1
#        assert False
