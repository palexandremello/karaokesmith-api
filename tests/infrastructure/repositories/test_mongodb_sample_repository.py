from mongomock import MongoClient
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

    def test_save(self, repository: MongoDbSampleRepository):
        # Cria uma instância do objeto de entidade a ser salvo
        sample_with_mp3 = Sample(audio_option=Mp3File(name="any_artist", path="any_path"))

        # Salva a entidade utilizando o repositório
        response = repository.save(sample_with_mp3)

        assert response.success is True
        assert response.body is sample_with_mp3
        assert response.body is not None
