import os
import logging
from pathlib import Path

logging.basicConfig( level=logging.INFO, format="[%(asctime)s ] %(message)")

project_name = "text_summarizer"

files_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebook/pre_train.ipynb"
]

# Creating folders and files
for file in files_list:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)

    # Creating directory
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Directory {file_dir} created for file {file_name}")

    # Creating file
    if (os.path.exists(file_path) == False) or (os.path.getsize(file_path) == 0):
        with open(file_name, 'w') as file:
            pass
            logging.info(f"File created: {file_name}")
    else:
        logging.info(f"File {file} already exists.")


