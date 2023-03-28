import pytest
from mongomock import MongoClient
from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from infrastructure.repos.mongodb.mongodb_sample_repository import MongoDbSampleRepository


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

    def test_should_returns_a_response_error_when_get_throws(self, repository: MongoDbSampleRepository):
        # Salva a entidade utilizando o repositório
        response = repository.get(sample_id="any_id")

        assert not response.success

    def test_should_able_to_delete_a_sample_with_successful(self, repository: MongoDbSampleRepository):
        # Cria uma instância do objeto de entidade a ser salvo
        sample_with_mp3 = Sample(audio_option=Mp3File(name="any_artist", path="any_path"), content=b"any_bytes")

        # Salva a entidade utilizando o repositório
        sample_response = repository.save(sample_with_mp3)

        response = repository.delete(sample_id=sample_response.body.id)

        assert response.success

    def test_should_returns_a_response_with_error_when_try_to_delete_a_sample_not_exists(
        self, repository: MongoDbSampleRepository
    ):
        response = repository.delete(sample_id="626bccb9697a12204fb22ea3")

        assert response.body == "Sample not found"

    def test_should_returns_a_response_with_error_when_delete_throws(self, repository: MongoDbSampleRepository):
        response = repository.delete(sample_id="incorrect_id")

        assert not response.success
