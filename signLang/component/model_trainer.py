import os, sys
import shutil
import yaml
from signLang.utils.main_utils import read_yaml_file
from signLang.exception import SignException
from signLang.logger import logging
from signLang.entity.config_entity import ModelTrainerConfig
from signLang.entity.artifacts_entity import ModelTrainerArtifact, DataIngestionArtifact

class Modeltrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig,
            data_ingestion_artifact: DataIngestionArtifact
    ):
        self.model_trainer_config = model_trainer_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            data_yaml_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images", "data.yaml")
            data_yaml_path = os.path.abspath(data_yaml_path)


            # Read number of classes from the data.yaml file
            with open(data_yaml_path, 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
                logging.info(f"Number of classes: {num_classes}")

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            logging.info(f"Model configuration file name: {model_config_file_name}")

            # Load the model configuration YAML
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            # Update the number of classes
            config['nc'] = int(num_classes)

            # Save the updated configuration
            custom_model_path = f'yolov5/models/custom_{model_config_file_name}.yaml'
            with open(custom_model_path, 'w') as f:
                yaml.dump(config, f)

            # Run training using YOLOv5
            train_command = (
                f"cd yolov5 && python train.py --img 416 --batch {self.model_trainer_config.batch_size} "
                f"--epochs {self.model_trainer_config.no_epochs} --data ../{self.data_ingestion_artifact.feature_store_path}/images/data.yaml "
                f"--cfg ./models/custom_{model_config_file_name}.yaml --weights {self.model_trainer_config.weight_name} "
                f"--name yolov5s_results --cache"
            )
            os.system(train_command)

            # Copy the best model to the desired location
            best_model_src = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            best_model_dst = "yolov5/best.pt"
            shutil.copy(best_model_src, best_model_dst)

            # Create the model trainer directory if it doesn't exist
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            final_model_dst = os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
            shutil.copy(best_model_src, final_model_dst)

            # Clean up intermediate directories and files
            shutil.rmtree("yolov5/runs", ignore_errors=True)
            # if os.path.exists("train"):
            #     shutil.rmtree("train", ignore_errors=True)
            # if os.path.exists("test"):
            #     shutil.rmtree("test", ignore_errors=True)
            # if os.path.exists("data.yaml"):
            #     os.remove("data.yaml")

            # Create and return the artifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=best_model_dst,
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
