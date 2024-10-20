import shutil
from pathlib import Path

from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config = data_ingestion_config
    
    def copy_pdf_files(self) -> None:
        """
            Copies all PDF files from the copy_data_dir to the root_dir.
        """
        
        try:
            from_dir = Path(self.data_ingestion_config.copy_data_dir)
            to_dir = Path(self.data_ingestion_config.root_dir)

            to_dir.mkdir(parents=True, exist_ok=True)

            for pdf_file in from_dir.glob("*.pdf"):
                shutil.copy(pdf_file, to_dir / pdf_file.name)
        except Exception as e:
            raise e
