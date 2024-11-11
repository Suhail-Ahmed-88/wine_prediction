import os
from box.exceptions import BoxValueError
import yaml
from wine import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Returns:
        ValueError: if yaml file is empty
        e: empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} empty file")
    except Exception as e:
        raise e    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """ save json file

    Args:
        path (Path): path to json file
        data (dict): data to save in json file
    """            
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        ConfigBox: _description_
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)
           
@ensure_annotations
def save_binary(file_path: Path, data: Any):
    """_summary_

    Args:            
        file_path (Path): _description_
        data (Any): _description_
    """
    joblib.dump(data, file_path)
    logger.info(f"binary file saved at: {file_path}")     
    
@ensure_annotations
def load_binary(file_path: Path) -> Any:
    """_summary_

    Args:
        file_path (Path): _description_

    Returns:
        Any: _description_
    """
    
    data = joblib.load(file_path)
    logger.info(f"binary file loaded from: {file_path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        str: _description_
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"