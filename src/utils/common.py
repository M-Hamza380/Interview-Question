from pathlib import Path

import yaml, os
from functools import lru_cache

from src.configuration.config import Settings


@lru_cache
def get_setting():
    """Returns the application settings"""
    return Settings()


def read_yaml(path_to_yaml: Path):
    """
    Reads a YAML file and returns its content as a dictionary.

    Args:
        path_to_yaml (Path): The path to the YAML file to be read.

    Returns:
        dict: The content of the YAML file as a dictionary.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return content
    except Exception as e:
        print(f"Error reading {path_to_yaml}: {e}")

def create_directories(path_to_directories: list):
    """
    Create list of directories.

    Args:
        path_to_directories: list of path of directories to be created
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error: {e.strerror}")
