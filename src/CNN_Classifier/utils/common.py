import os
import sys
import yaml
import json
import joblib
import base64
from CNN_Classifier.logging import logging
from CNN_Classifier.exception_handler import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path


@ensure_annotations
def read_yaml(yaml_filepath:Path) -> ConfigBox:
    try:
        with open(yaml_filepath, 'r') as file_obj:
            content = yaml.safe_load(file_obj)
            logging.info(f"yaml file: {yaml_filepath} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    try:
        for directory in path_to_directories:
            os.makedirs(directory,exist_ok=True)
            if verbose:
                logging.info(f"creating directory at : {directory}")
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def save_json(json_filepath: Path,data: dict):
    try:
        with open(json_filepath, "w") as obj:
            json.dump(data, obj, indent=4)

        logging.info(f"json file saved at: {json_filepath}")
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def load_json(json_filepath: Path) -> ConfigBox:
    try:
        with open(json_filepath) as obj:
            content = json.load(obj)

        logging.info(f"json file loaded succesfully from: {json_filepath}")
        return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def save_bin(bin_filepath: Path,data: Any):
    try:
        joblib.dump(value=data, filename=bin_filepath)
        logging.info(f"binary file saved at: {bin_filepath}")
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def load_bin(bin_filepath: Path) -> Any:
    try:
        data = joblib.load(bin_filepath)
        logging.info(f"binary file loaded from: {bin_filepath}")
        return data
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def get_size(filepath: Path) -> str:
    try:
        size_in_kb = round(os.path.getsize(filepath)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        raise CustomException(e,sys)

def decodeImage(imgstring, fileName):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, "wb") as file_obj:
            file_obj.write(imgdata)
            file_obj.close()
    except Exception as e:
        raise CustomException(e,sys)

def encodeImageIntoBase64(ImagePath):
    try:
        with open(ImagePath, "rb") as file_obj:
            return base64.b64encode(file_obj.read())
    except Exception as e:
        raise CustomException(e,sys)
