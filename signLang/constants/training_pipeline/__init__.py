import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "jonathanoheix/face-expression-recognition-dataset"

GDRIVE_DOWNLOAD_URL: str ="https://drive.google.com/uc?id=10iHvwk510kQiw45XN9zEBjBzY1mRpAz5"

USE_GDRIVE = True

# https://drive.google.com/file/d//view?usp=sharing
# https://drive.google.com/file/d/10iHvwk510kQiw45XN9zEBjBzY1mRpAz5/view?usp=sharing

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

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = 'yolov5m.pt'

MODEL_TRAINER_NO_EPOCH: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 4


"""
Model pusher
"""

BUCKET_NAME:str = "sign-lang-39"
S3_MODEL_NAME:str = "best.pt"