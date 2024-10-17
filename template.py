import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, 
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)d : %(message)s ]"
)

list_of_files = [
    "config/config.yaml",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/prompt.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/vector_embeddings.py",
    "src/components/llm_model.py",
    "src/configuration/__init__.py",
    "src/configuration/configuration.py",
    "src/contants/__init__.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/pipeline/__init__.py",
    "src/pipeline/llm_pipeline.py",
    "requirements.txt",
    "setup.py",
    "app.py",
    "notebook exp/exp.ipynb",
    "templates/index.html",
    "static/style.css"
]

for file in list_of_files:
    filepath = Path(file)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"Creating empty file: {file}")
    else:
        logging.info(f"{file} already exists")
