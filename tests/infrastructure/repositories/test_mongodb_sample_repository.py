from unittest.mock import MagicMock
from mongomock import MongoClient, patch
import pytest
from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample

from infrastructure.repositories.mongodb_sample_repository import MongoDbSampleRepository


class TestMongoDbRepository:
    @pytest.fixture
    def mongo_client(self):
        client = MongoClient()
        yield client

    @pytest.fixture
    def repository(self, mongo_client):
        repository = MongoDbSampleRepository(
            mongo_client=mongo_client, database_name="karaokesmith", collection_name="samples"
        )
        yield repository

    def test_should_able_to_save_sample_with_successful(self, repository: MongoDbSampleRepository):
        # Cria uma instância do objeto de entidade a ser salvo
        sample_with_mp3 = Sample(audio_option=Mp3File(name="any_artist", path="any_path"))

        # Salva a entidade utilizando o repositório
        response = repository.save(sample_with_mp3)

        assert response.success is True
        assert response.body is sample_with_mp3
        assert response.body is not None

    def test_should_returns_a_response_error_when_MongoDbSampleRepository_throws(
        self, repository: MongoDbSampleRepository
    ):
        # Salva a entidade utilizando o repositório
        response = repository.save("any")

        assert not response.success

    def test_should_able_to_get_a_sample_with_successful(self, repository: MongoDbSampleRepository):
        # Cria uma instância do objeto de entidade a ser salvo
        sample_with_mp3 = Sample(audio_option=Mp3File(name="any_artist", path="any_path"), content=b"any_bytes")

        # Salva a entidade utilizando o repositório
        sample_response = repository.save(sample_with_mp3)

        response = repository.get(sample_id=sample_response.body.id)

        assert response.body.id == sample_response.body.id

    def test_should_return_a_body_None_when_sample_does_not_exists(self, repository: MongoDbSampleRepository):
        response = repository.get(sample_id="626bccb9697a12204fb22ea3")

        assert response.body is None
