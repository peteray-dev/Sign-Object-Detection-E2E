import os , sys

from signLang.logger import logging
from signLang.exception import SignException

from signLang.component.data_ingestion import Dataingestion

from signLang.component.data_validation import DataValidation
from signLang.component.model_trainer import Modeltrainer
from signLang.component.model_pusher import ModelPusher
from signLang.configuration.s3_operations import S3Operation
from signLang.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig, ModelPusherConfig)
from signLang.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact, ModelPusherArtifacts) 


class TrainingPipeline:
    def __init__(self) -> DataIngestionArtifact:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_coonfig = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_pusher_config = ModelPusherConfig()
        self.s3_operations = S3Operation()
        
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
        
    # def start_model_trainer(self, model ) -> ModelTrainerArtifact:
    #     try:
    #         model_trainer = Modeltrainer(
    #             model_trainer_config = self.model_trainer_config
    #         )
    #         model_trainer_artifact = model_trainer.initiate_model_trainer()
    #         return model_trainer_artifact
        
    #     except Exception as e:
    #         raise SignException(e, sys)

    def start_model_trainer(self, data_ingestion_artifact: DataIngestionArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer = Modeltrainer(
                model_trainer_config=self.model_trainer_config,
                data_ingestion_artifact=data_ingestion_artifact  # Pass the data_ingestion_artifact
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise SignException(e, sys)
        

    def start_model_pusher(self, model_trainer_artifact: ModelTrainerArtifact, s3: S3Operation):

        try:
            model_pusher = ModelPusher(
                model_pusher_config=self.model_pusher_config,
                model_trainer_artifact= model_trainer_artifact,
                s3=s3
                
            )
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise SignException(e, sys)




    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer(data_ingestion_artifact)
                model_pusher_artifact = self.start_model_pusher(model_trainer_artifact=model_trainer_artifact,s3=self.s3_operations)

            else:
                raise Exception("your data is not in correct format")

        except Exception as e:
            raise SignException(e, sys)
        

    
        


    