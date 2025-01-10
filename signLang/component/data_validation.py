import os, sys, yaml
import shutil #to copy file
from signLang.logger import logging
from signLang.exception import SignException
from signLang.entity.config_entity import DataValidationConfig
from signLang.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact)

class DataValidation:
    def __init__(
            self,
            data_ingestion_artifact = DataIngestionArtifact,
            data_validation_config = DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact 
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SignException(e, sys)
        
    def validate_all_file_exist(self) -> bool:
        try:
            validation_status = True
            # Add /images to the feature store path
            images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")

            # List all files in the /images directory
            all_files = os.listdir(images_path)
            # all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            # Check if all required files are in the directory
            for required_file in self.data_validation_config.required_file_list:
                if required_file not in all_files:
                    validation_status = False
                    break

            # Write validation status to a file
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f'Validation status: {validation_status}')

            return validation_status
        
        except Exception as e:
            raise SignException(e, sys)

    def create_dataset_yaml(self):
        """
        Create a dataset.yaml file based on the structure of the dataset.
        """
        try:
            images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")

            train_path = os.path.join(images_path, "train")
            val_path = os.path.join(images_path, "validation")

            # Get class names from training folder structure
            class_names = sorted(
                folder for folder in os.listdir(train_path)
                if os.path.isdir(os.path.join(train_path, folder))
            )

            dataset_yaml_path = os.path.join(images_path, "data.yaml")

            # Create YAML content
            dataset_yaml_content = {
                "train": train_path,
                "val": val_path,
                "nc": len(class_names),  # Number of classes
                "names": class_names  # Class names
            }

            # Write YAML file
            with open(dataset_yaml_path, 'w') as yaml_file:
                yaml.dump(dataset_yaml_content, yaml_file)

            logging.info(f"dataset.yaml created successfully at {dataset_yaml_path}")
            return dataset_yaml_path
        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered into initiating data validation class")
        try:

            self.create_dataset_yaml()
            # Validate all files exist
            status = self.validate_all_file_exist()

            # Create dataset.yaml
            # if status:
                # self.create_dataset_yaml()

            # Prepare DataValidationArtifact
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logging.info("Exited initiate data validation method of data validation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)
