import yaml, os, sys, dill, pickle
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
import numpy as np


def read_yaml_file(file_path):
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys)
