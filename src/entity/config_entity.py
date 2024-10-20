from pathlib import Path
from dataclasses import dataclass

from src.constants import *

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    copy_data_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path

@dataclass(frozen=True)
class VectorEmbeddingsConfig:
    root_dir: Path
    copy_embeds_dir: Path

@dataclass(frozen=True)
class ModelConfig:
    TOKEN_MODEL: str
    LLM_MODEL_NAME: str
