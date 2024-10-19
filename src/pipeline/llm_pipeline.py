from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.vector_embeddings import VectorEmbeddings
from src.components.llm_model import LLMModel
from src.components.file_process import FileProcessing

from src.entity.config_entity import (DataIngestionConfig, DataValidationConfig, 
                                       VectorEmbeddingsConfig, ModelConfig)

class LLMPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.vector_embeddings_config = VectorEmbeddingsConfig()
        self.model_config = ModelConfig()

    def run_llm_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion.copy_pdf_files()

            # Data Validation
            data_validation = DataValidation(self.data_validation_config)
            data_validation.validation_pdf_files()

            # Vector Embeddings
            vector_embeddings = VectorEmbeddings(self.vector_embeddings_config)
            vector_embeddings.vector_embeddings_file()

            # File Processing
            file_processing = FileProcessing(self.model_config, self.data_ingestion_config)

            # LLM Model
            model = LLMModel(self.model_config, self.vector_embeddings_config, file_processing)
            answer_chain, questions_list = model.llm_model()

            return answer_chain, questions_list

        except Exception as e:
            raise RuntimeError(f"Error in LLMPipeline: {e}")
