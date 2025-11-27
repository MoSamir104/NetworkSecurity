from networksecurity.entity.arifact_entity import DataIngetsionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging 
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file
from scipy.stats import ks_2samp
import pandas 
import os, sys


class DatatValidaiton:
    def __init__(self
                 , data_ingestion_artifac:DataIngetsionArtifact
                 , data_validation_config: DataValidationConfig):
        
        try:
            self.data_ingestion_artifact = data_ingestion_artifac
            self.data_validation_config = data_validation_config
            self.__schema__config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e, sys)






