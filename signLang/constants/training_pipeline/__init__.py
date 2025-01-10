import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "jonathanoheix/face-expression-recognition-dataset"

GDRIVE_DOWNLOAD_URL: str ="https://drive.google.com/uc?id=177Cu3-Ae2Rv3SUsrbWOdfu8fW-W7a7SZ"

USE_GDRIVE = True


"""
Data Validation Constant
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE: str = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ['train', 'validation', 'data.yaml']