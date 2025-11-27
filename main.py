from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging 
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpiplineconfig = TrainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(trainingpiplineconfig)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        Dataingetstionartifact = data_ingestion.initiate_data_ingetstion()
        print(Dataingetstionartifact)
        logging.info("Enter the try block")
    except Exception as e:
        raise CustomException(e, sys)
