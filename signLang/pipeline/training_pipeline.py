import os , sys

from signLang.logger import logging
from signLang.exception import SignException

from signLang.component.data_ingestion import Dataingestion

from signLang.component.data_validation import DataValidation

from signLang.entity.config_entity import (DataIngestionConfig, DataValidationConfig)
from signLang.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact) 

class TrainingPipeliine:
    def __init__(self) -> DataIngestionArtifact:
        self.data_ingestion_config = DataIngestionConfig
        self.data_validation_coonfig = DataValidationConfig

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("Enterned into the start data ingestion method in the trainig pipeline")
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

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact )-> DataValidationArtifact:
        logging.info("Enterned into the start data validation method in the training pipeline")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_coonfig
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("perform the data validation operation")
            logging.info("exited the start data validation method of training Pipeline class")

            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)
        
        

    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )

        except Exception as e:
            raise SignException(e, sys)
        


    