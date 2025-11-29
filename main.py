from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging 
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DatatValidaiton
from networksecurity.components.data_transformation import DataTransformation
import sys

if __name__ == "__main__":
    try:
        trainingpiplineconfig = TrainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(trainingpiplineconfig)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        Dataingetstionartifact = data_ingestion.initiate_data_ingetstion()
        logging.info("data initiation completed")
        print(Dataingetstionartifact)
        data_validation_config = DataValidationConfig(trainingpiplineconfig)
        data_validation = data_validation = DatatValidaiton(Dataingetstionartifact, data_validation_config)
        logging.info("Initiate the data validation")
        data_vallidation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_vallidation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpiplineconfig)
        logging.info("data transformation started")
        data_transformation = DataTransformation(data_vallidation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")
    except Exception as e:
        raise CustomException(e, sys)
