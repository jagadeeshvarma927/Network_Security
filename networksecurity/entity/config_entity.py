from datetime import datetime
import os
from networksecurity.constant import training_pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
import sys

print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self):
        try:
           pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

class DataIngestionConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

class DataValidationConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
class DataTransformationConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

class ModelTrainerConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

class ModelEvaluationConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
class ModelPusherConfig:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

