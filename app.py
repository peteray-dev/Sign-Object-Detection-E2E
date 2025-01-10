# from signLang.logger import logging
# # from signLanguage.exception import SignException
# logging.info('welcome to the project')
from signLang.pipeline.training_pipeline import TrainingPipeliine

obj = TrainingPipeliine()
obj.run_pipeline()