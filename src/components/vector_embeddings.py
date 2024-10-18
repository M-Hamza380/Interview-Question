from src.entity.config_entity import VectorEmbeddingsConfig


class VectorEmbeddings:
    def __init__(self, vector_embeddings_config: VectorEmbeddingsConfig) -> None:
        self.vector_embeddings_config = vector_embeddings_config

    def vector_embedding(self) -> None:
        try:
            pass
        except Exception as e:
            raise e
