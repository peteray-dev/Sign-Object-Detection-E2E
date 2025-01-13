import os
import sys
import yaml
import shutil  # to copy file
from signLang.logger import logging
from signLang.exception import SignException
from signLang.entity.config_entity import DataValidationConfig
from signLang.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact)


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise SignException(e, sys) 
        

    
    def validate_all_files_exist(self) -> bool:
        try:
            
            validation_status = None
            all_files = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")
            all_files = os.listdir(all_files)

            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            
            return validation_status

        except Exception as e:
            raise SignException(e, sys)
        


    def update_dataset_yaml(self):
        try:
            # Paths for train and validation data
            # images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")
            # train_path = os.path.abspath(os.path.join(images_path, "train"))
            # val_path = os.path.abspath(os.path.join(images_path, "test"))

            images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")
            train_path = os.path.join( images_path, "train")
            val_path = os.path.join("../", images_path, "test")

            train_path = os.path.abspath(os.path.join(images_path, "train"))
            val_path = os.path.abspath(os.path.join(images_path, "test"))


            # File path for dataset.yaml
            dataset_yaml_path = os.path.join(images_path, "data.yaml")

            # Read existing YAML file if it exists
            if os.path.exists(dataset_yaml_path):
                with open(dataset_yaml_path, 'r') as yaml_file:
                    dataset_yaml_content = yaml.safe_load(yaml_file)
            else:
                dataset_yaml_content = {}

            # Update the train and val paths
            dataset_yaml_content["train"] = train_path
            dataset_yaml_content["val"] = val_path

            # Write updated content back to YAML file
            with open(dataset_yaml_path, 'w') as yaml_file:
                yaml.dump(dataset_yaml_content, yaml_file)

            logging.info(f"dataset.yaml updated successfully at {dataset_yaml_path}")
            return dataset_yaml_path

        except Exception as e:
            raise SignException(e, sys)

        

    
    # def initiate_data_validation(self) -> DataValidationArtifact: 
    #     logging.info("Entered initiate_data_validation method of DataValidation class")
    #     try:
    #         status = self.validate_all_files_exist()
    #         data_validation_artifact = DataValidationArtifact(
    #             validation_status=status)

    #         logging.info("Exited initiate_data_validation method of DataValidation class")
    #         logging.info(f"Data validation artifact: {data_validation_artifact}")

    #         if status:
    #             shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

    #         return data_validation_artifact

    #     except Exception as e:
    #         raise SignException(e, sys)

# class DataValidation:
#     def __init__(
#             self,
#             data_ingestion_artifact=DataIngestionArtifact,
#             data_validation_config=DataValidationConfig,
#     ):
#         try:
#             self.data_ingestion_artifact = data_ingestion_artifact
#             self.data_validation_config = data_validation_config
#         except Exception as e:
#             raise SignException(e, sys)

#     def validate_all_file_exist(self) -> bool:
#         try:
#             validation_status = True
#             images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")

#             all_files = os.listdir(images_path)

#             for required_file in self.data_validation_config.required_file_list:
#                 if required_file not in all_files:
#                     validation_status = False
#                     break

#             os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
#             with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
#                 f.write(f'Validation status: {validation_status}')

#             return validation_status

#         except Exception as e:
#             raise SignException(e, sys)

    # def create_dataset_yaml(self):
    #     try:
    #         images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")
    #         train_path = os.path.join( images_path, "train")
    #         val_path = os.path.join("../", images_path, "validation")

    #         train_path = os.path.abspath(os.path.join(images_path, "train"))
    #         val_path = os.path.abspath(os.path.join(images_path, "validation"))


    #         print(train_path)
    #         print(val_path)

    #         # class_names = sorted(
    #         #     folder for folder in os.listdir(train_path)
    #         #     if os.path.isdir(os.path.join(train_path, folder))
    #         # )

    #         dataset_yaml_path = os.path.join(images_path, "data.yaml")

    #         dataset_yaml_content = {
    #             "train": train_path,
    #             "val": val_path,
    #             # "nc": len(class_names),
    #             # "names": class_names
    #         }

    #         with open(dataset_yaml_path, 'w') as yaml_file:
    #             yaml.dump(dataset_yaml_content, yaml_file)

    #         logging.info(f"dataset.yaml created successfully at {dataset_yaml_path}")
    #         return dataset_yaml_path
    #     except Exception as e:
    #         raise SignException(e, sys)

    # def create_labels(self):
    #     """
    #     Generate label files for images based on directory structure.
    #     """
    #     try:
    #         # Define paths for images and labels
    #         images_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "images")
    #         train_path = os.path.join(images_path, "train")
    #         val_path = os.path.join(images_path, "validation")
    #         label_base_path = os.path.join(self.data_ingestion_artifact.feature_store_path, "labels")

    #         # Define train and validation directories for label generation
    #         label_dirs = [("train", train_path), ("validation", val_path)]

    #         # Map class names to numerical labels
    #         class_names = sorted(
    #             folder for folder in os.listdir(train_path)
    #             if os.path.isdir(os.path.join(train_path, folder))
    #         )
    #         class_map = {name: idx for idx, name in enumerate(class_names)}

    #         logging.info(f"Class Mapping: {class_map}")

    #         # Function to generate label files
    #         def generate_labels(image_dir, label_dir, class_map):
    #             """
    #             Generate YOLO label files for images in the dataset.
    #             """
    #             for class_name, class_id in class_map.items():
    #                 class_image_path = os.path.join(image_dir, class_name)
    #                 class_label_path = os.path.join(label_dir, class_name)
    #                 os.makedirs(class_label_path, exist_ok=True)

    #                 for img_file in os.listdir(class_image_path):
    #                     if img_file.endswith((".jpg", ".png", ".jpeg")):
    #                         label_file = os.path.splitext(img_file)[0] + ".txt"
    #                         label_content = f"{class_id} 0.5 0.5 1.0 1.0\n"

    #                         with open(os.path.join(class_label_path, label_file), "w") as f:
    #                             f.write(label_content)

    #         # Generate labels for train and validation datasets
    #         for label_dir_name, image_dir in label_dirs:
    #             label_dir = os.path.join(label_base_path, label_dir_name)
    #             generate_labels(image_dir, label_dir, class_map)

    #         logging.info("Labels generated successfully!")
    #     except Exception as e:
    # #         raise SignException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info("Entered into initiating data validation class")
        try:
            # self.create_dataset_yaml()

            status = self.validate_all_files_exist()

            if status:
                self.update_dataset_yaml()

            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logging.info("Exited initiate data validation method of data validation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)
