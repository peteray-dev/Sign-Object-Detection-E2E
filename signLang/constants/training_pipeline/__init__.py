import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "jonathanoheix/face-expression-recognition-dataset"

GDRIVE_DOWNLOAD_URL: str ="https://drive.google.com/uc?id=1G36QmJg16YmZAoxoZ0kv5W1yP3EUSe15"

USE_GDRIVE = True
# https://drive.google.com/file/d//view?usp=sharing

"""
Data Validation Constant
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE: str = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ['train', 'validation', 'data.yaml']

"""
Model training
"""

MODEL_TRAINER_DIR_NAME: str = 'model_trainer'

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = 'yolov5s.pt'

MODEL_TRAINER_NO_EPOCH: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 32