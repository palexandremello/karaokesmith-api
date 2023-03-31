from unittest.mock import MagicMock
import pytest
from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.services.sample_saver.sample_saver import SampleSaver

from domain.services.sample_saver.save_method_interface import SaveMethodInterface
from domain.utils.response import Response


class TestSampleSaver:
    @pytest.fixture
    def save_method_stub(self):
        return MagicMock(spec=SaveMethodInterface)

    @pytest.fixture
    def sample_saver(self, save_method_stub):
        return SampleSaver(save_method=save_method_stub)

    def test_should_be_able_to_save_a_sample(self, save_method_stub, sample_saver):
        sample = Sample(audio_option=Mp3File(name="any_name", path="any_path"), content=b"any_bytes")
        expected_sample = sample
        expected_sample.path = "any_path"
        save_method_stub.save.return_value = Response(success=True, body=expected_sample)

        response = sample_saver.save_sample(sample)

        assert response.success
        assert response.body.path == "any_path"
