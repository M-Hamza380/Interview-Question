from pathlib import Path
from dataclasses import dataclass

from src.contants import *

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    stats_data: Path

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
    def __init__(self):
        self.TOKEN_MODEL = TOKEN_MODEL
        self.LLM_MODEL_NAME = LLM_MODEL_NAME
