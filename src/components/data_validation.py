from pathlib import Path

from src.entity.config_entity import DataIngestionConfig, DataValidationConfig

class DataValidation:
    def __init__(self, ingestion_config: DataIngestionConfig, data_validation_config: DataValidationConfig) -> None:
        self.ingestion_config = ingestion_config
        self.data_validation_config = data_validation_config
    
    def validation_pdf_files(self):
        try:
            ingestion_files = list(self.ingestion_config.root_dir.glob("*.pdf"))
            report_lines = []

            if ingestion_files:
                report_lines.append("PDF files in data ingestion directory.")
                for pdf in ingestion_files:
                    report_lines.append(f"- {pdf.name}")
            else:
                report_lines.append("No PDF files in data ingestion directory.")
            
            all_files = list(self.ingestion_config.root_dir.glob("*"))
            other_files = [f for f in all_files if f.suffix != ".pdf"]

            if other_files:
                report_lines.append("Other files in data ingestion directory.")
                for file in other_files:
                    report_lines.append(f"- {file.name}")
            
            with open(self.data_validation_config.status_file, "w") as report_file:
                for line in report_lines:
                    report_file.write(line + "\n".join(report_lines))
        except Exception as e:
            raise e

