from src.constants import Config_File_Path
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import (DataIngestionConfig, DataValidationConfig,
                        VectorEmbeddingsConfig)


class ConfigurationManager:
    def __init__(self, config_file_path: str = Config_File_Path) -> None:
        self.config: dict = read_yaml(config_file_path)

        create_directories([self.config['artifacts_root']])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Gets the data ingestion configuration from the config file.

        Returns:
            DataIngestionConfig: The data ingestion configuration
        """
        config = self.config['data_ingestion']

        create_directories([config['root_dir']])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            copy_data_dir=config['copy_data_dir']
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Gets the data validation configuration from the config file.

        Returns:
            DataValidationConfig: The data validation configuration
        """
        config = self.config['data_validation']

        create_directories([config['root_dir']])

        data_validation_config = DataValidationConfig(
            root_dir=config['root_dir'],
            status_file=config['status_file']
        )
        return data_validation_config

    def get_vector_embeddings_config(self) -> VectorEmbeddingsConfig:
        """
        Gets the vector embeddings configuration from the config file.

        Returns:
            VectorEmbeddingsConfig: The vector embeddings configuration
        """
        config = self.config['vector_embeddings']

        create_directories([config['root_dir']])

        vector_embeddings_config = VectorEmbeddingsConfig(
            root_dir=config['root_dir'],
            copy_embeds_dir=config['copy_embeds_dir']
        )
        return vector_embeddings_config        
