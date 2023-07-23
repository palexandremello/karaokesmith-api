from typing import List, Optional
from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from app.domain.entities.sample import Sample
from app.domain.repositories.sample_repository_interface import SampleRepositoryInterface
from app.domain.utils.response import Response


class MongoDbSampleRepository(SampleRepositoryInterface):
    def __init__(self, mongo_client: MongoClient, database_name: str, collection_name: str) -> None:
        self.db = mongo_client[database_name]
        self.collection: Collection = self.db[collection_name]

    def save(self, samples: List[Sample]) -> Response[Sample]:
        try:
            paths = []
            for sample in samples:
                paths.append(sample.path)

            sample = sample.to_dict()
            sample["path"] = paths

            filter = {"name": sample["name"]}
            update = {"$set": sample}
            result = self.collection.update_one(filter, update, upsert=True)
            sample["id"] = result.upserted_id or sample["id"]

            return Response(success=True, body=sample)

        except Exception as error:
            return Response(success=False, body=error)

    def get(self, sample_id: str) -> Response[Optional[Sample]]:
        try:
            result = self.collection.find_one({"_id": ObjectId(sample_id)})
            if result is None:
                return Response(success=True, body=None)

            sample = Sample(
                audio_option=result["audio_option"],
                name=result["name"],
                content=result["content"],
                path=result["path"],
                id=result["_id"],
            )
            return Response(success=True, body=sample)
        except Exception as e:
            return Response(success=False, body=str(e))

    def list_all(self) -> Response[List[Sample]]:
        try:
            cursor = self.collection.find({})
            for result in cursor:
                sample = Sample(
                    name=result["name"],
                    content=result["content"],
                    path=result["path"],
                    id=result["_id"],
                )

            return Response(success=True, body=sample)
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
