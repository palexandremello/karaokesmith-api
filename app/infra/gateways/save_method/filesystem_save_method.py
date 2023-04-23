import os
from typing import List
from app.domain.services.sample_saver.save_method_interface import SaveMethodInterface
from app.domain.utils.logger.logger_interface import LoggerInterface
from app.main.config.settings import SAMPLES_DIRECTORY
from app.domain.entities.sample import Sample
from app.domain.utils.response import Response
from app.domain.entities.mp3_file import Mp3File


class FilesystemSaveMethod(SaveMethodInterface):
    def __init__(self, logger: LoggerInterface) -> None:
        self.logger = logger
        self.samples_directory = SAMPLES_DIRECTORY

    def save(self, samples: List[Mp3File]) -> Response[List[Sample]]:
        files_path = []
        try:
            if not os.path.exists(self.samples_directory):
                os.makedirs(self.samples_directory)

            sample_number = 1
            for sample in samples:
                file_path = os.path.join(self.samples_directory, f"{sample.name}_{sample_number}.mp3")

                with open(file_path, "wb") as file:
                    file.write(sample.path)

                self.logger.info(f"Amostra {sample.name} salva com sucesso: {file_path}")
                files_path.append(Sample(name=sample.name, path=file_path))
                sample_number += 1

        except Exception as e:
            self.logger.error(f"Erro ao salvar amostras: {e}")
            return Response(success=False, body="Erro ao salvar amostras")

        return Response(success=True, body=files_path)
