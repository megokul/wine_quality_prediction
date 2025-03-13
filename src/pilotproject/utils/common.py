import os
import yaml
from src.pilotproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import Configbox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Configbox:
    """
    Reads a YAML file and returns its content as a Configbox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        Configbox: Parsed content of the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs during reading the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open YAML file
            content = yaml.safe_load(yaml_file)  # Load content safely to prevent code execution
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log successful loading
            return Configbox(content)  # Convert loaded data to Configbox object for easy access
    except BoxValueError:
        raise ValueError("yaml file is empty")  # Handle case where YAML content is empty
    except Exception as e:
        raise e  # Propagate other exceptions


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from the provided list.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): Enables logging of created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create directories, ignoring if they already exist
        if verbose:
            logger.info(f"created directory at: {path}")  # Log directory creation


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to the output JSON file.
        data (dict): Dictionary to save.
    """
    with open(path, 'w') as file:  # Open file in write mode
        json.dump(data, file, indent=4)  # Write data as formatted JSON

    logger.info(f"JSON file saved at: {path}")  # Log JSON file creation


@ensure_annotations
def load_json(path: Path) -> Configbox:
    """
    Loads a JSON file and returns its content as a Configbox object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        Configbox: Parsed content of the JSON file.
    """
    with open(path) as file:  # Open JSON file
        content = json.load(file)  # Load JSON content

    logger.info(f"JSON file loaded successfully from: {path}")  # Log successful load
    return Configbox(content)  # Convert loaded data to Configbox object


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves a Python object in binary format using joblib.

    Args:
        path (Path): Path to the binary file.
        data (Any): Python object to serialize.
    """
    joblib.dump(value=data, filename=path)  # Serialize and save the Python object
    logger.info(f"Binary file saved at: {path}")  # Log binary file creation


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a Python object from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Python object loaded from the binary file.
    """
    data = joblib.load(path)  # Load Python object from binary file
    logger.info(f"Binary file loaded from: {path}")  # Log successful load
    return data
