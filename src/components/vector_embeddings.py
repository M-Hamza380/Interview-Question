import shutil
from pathlib import Path

from src.entity.config_entity import VectorEmbeddingsConfig


class VectorEmbeddings:
    def __init__(self, vector_embeddings_config: VectorEmbeddingsConfig) -> None:
        self.vector_embeddings_config = vector_embeddings_config

    def vector_embeddings_file(self) -> None:
        """
            Copies all files and directories from the copy_embeds_dir to the root_dir.

            This function ensures that the destination directory exists and then iterates
            through all items in the source directory, copying each file or directory to
            the destination directory.

            Raises:
                Exception: Propagates any exception encountered during the copy operation.
        """
        try:
            from_dir = Path(self.vector_embeddings_config.copy_embeds_dir)
            to_dir = Path(self.vector_embeddings_config.root_dir)
            to_dir.mkdir(parents=True, exist_ok=True)

            for item in from_dir.iterdir():
                if item.is_file():
                    shutil.copy(item, to_dir / item.name)
                elif item.is_dir():
                    shutil.copytree(item, to_dir / item.name, dirs_exist_ok=True)
        except Exception as e:
            raise e
