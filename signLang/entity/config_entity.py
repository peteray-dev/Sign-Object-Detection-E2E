import os
from dataclasses import dataclass
from datetime import datetime
from signLang.constants.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME
    )
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_download_url: str = DATA_DOWNLOAD_URL

    gdrive_download_url: str = GDRIVE_DOWNLOAD_URL

    use_gdrive: str = USE_GDRIVE