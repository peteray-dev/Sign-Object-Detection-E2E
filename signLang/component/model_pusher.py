import sys
from signLang.configuration.s3_operations import S3Operation
from signLang.entity.artifacts_entity import ModelPusherArtifacts, ModelTrainerArtifact
from signLang.entity.config_entity import ModelPusherConfig
from signLang.exception import SignException
from signLang.logger import logging

class ModelPusher:
    def __init__(
            self,
            model_pusher_config: ModelPusherConfig, model_trainer_artifact: ModelTrainerArtifact, s3: S3Operation
    ):
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifact= model_trainer_artifact
        self.s3 = s3


    def initiate_model_pusher(self) -> ModelPusherArtifacts:

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                from_filename= self.model_trainer_artifact.trained_model_file_path,
                to_filename=self.model_pusher_config.S3_MODEL_KEY_PATH,
                bucket_name= self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )

            return model_pusher_artifact

        except Exception as e:
            raise SignException(e, sys) from e
