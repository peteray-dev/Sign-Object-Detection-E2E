import os
import sys
import zipfile 
from kaggle.api.kaggle_api_extended import KaggleApi
from signLang.logger import logging
from signLang.exception import SignException
from signLang.entity.artifacts_entity import DataIngestionArtifact
from signLang.entity.config_entity import DataIngestionConfig

class Dataingestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.api = KaggleApi()
            self.api.authenticate()
        except Exception as e:
            raise SignException(e, sys)

    def download_data(self) -> str:
        """
        Download dataset from Kaggle using the Kaggle API.
        Returns the path to the downloaded zip file.
        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url  # Dataset identifier
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            
            dataset_owner, dataset_name = dataset_url.split("/")  # e.g., "username/dataset-name"
            zip_file_path = os.path.join(zip_download_dir, f"{dataset_name}.zip")

            logging.info(f"Downloading dataset {dataset_url} into {zip_file_path}")
            self.api.dataset_download_files(dataset_owner + '/' + dataset_name, path=zip_download_dir, unzip=False)
            logging.info(f"Downloaded dataset {dataset_url} into {zip_file_path}")
            return zip_file_path
        except Exception as e:
            raise SignException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        Extract the zip file in the data directory.
        Returns the path to the extracted feature store.
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracted zip file from {zip_file_path} into directory {feature_store_path}")

            return feature_store_path
        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Initiating data ingestion in the Data Ingestion class")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifacts = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Completed data ingestion")
            logging.info(f"Data Ingestion Artifacts: {data_ingestion_artifacts}")

            return data_ingestion_artifacts
        except Exception as e:
            raise SignException(e, sys)
