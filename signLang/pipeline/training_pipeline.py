import os , sys

from signLang.logger import logging
from signLang.exception import SignException

from signLang.component.data_ingestion import Dataingestion

from signLang.entity.config_entity import (DataIngestionConfig)
from signLang.entity.artifacts_entity import (DataIngestionArtifact) 

class TrainingPipeliine:
    def __init__(self) -> DataIngestionArtifact:
        self.data_ingestion_config = DataIngestionConfig

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("Enterned into the adata ingestion method in the trainig pipeline")
            logging.info("getting started with data from the url")

            data_ingestion = Dataingestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("got the data from the url")
            logging.info(
                "Exited rom the start data ingestion method from the Training pipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)
        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise SignException(e, sys)