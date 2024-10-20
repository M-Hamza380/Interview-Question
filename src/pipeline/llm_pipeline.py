from src.configuration.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.vector_embeddings import VectorEmbeddings
from src.components.file_process import FileProcessing
from src.components.llm_model import LLMModel
from src.entity.config_entity import ModelConfig
from src.constants import TOKEN_MODEL, LLM_MODEL_NAME

class LLMPipeline:
    def __init__(self) -> None:
        config_manager = ConfigurationManager()
        self.data_ingestion_config = config_manager.get_data_ingestion_config()
        self.data_validation_config = config_manager.get_data_validation_config()
        self.vector_embeddings_config = config_manager.get_vector_embeddings_config()
        self.model_config = ModelConfig(TOKEN_MODEL, LLM_MODEL_NAME)

    def run_llm_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion.copy_pdf_files()

            # Data Validation
            data_validation = DataValidation(ingestion_config=self.data_ingestion_config, data_validation_config=self.data_validation_config)
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
