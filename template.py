import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, 
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)d : %(message)s ]"
)

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
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
