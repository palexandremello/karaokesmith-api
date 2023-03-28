from typing import Optional
from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from domain.entities.sample import Sample
from domain.repositories.sample_repository_interface import SampleRepositoryInterface

from domain.utils.response import Response


class MongoDbSampleRepository(SampleRepositoryInterface):
    def __init__(self, mongo_client: MongoClient, database_name: str, collection_name: str) -> None:
        self.db = mongo_client[database_name]
        self.collection: Collection = self.db[collection_name]

    def save(self, sample: Sample) -> Response[Sample]:
        try:
            result = self.collection.insert_one(sample.to_dict())

            sample.id = result.inserted_id
            return Response(success=True, body=sample)

        except Exception as error:
            return Response(success=False, body=error)

    def get(self, sample_id: str) -> Response[Optional[Sample]]:
        try:
            result = self.collection.find_one({"_id": ObjectId(sample_id)})
            if result is None:
                return Response(success=True, body=None)
            return Response(success=True, body=Sample.from_dict(result))
        except Exception as e:
            return Response(success=False, body=str(e))

    def delete(self, sample_id: str) -> Response:
        try:
            result = self.collection.delete_one({"_id": ObjectId(sample_id)})
            if result.deleted_count == 0:
                return Response(success=False, body="Sample not found")
            return Response(success=True, body=None)
        except Exception as e:
            return Response(success=False, body=str(e))