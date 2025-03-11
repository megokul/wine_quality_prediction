import os
from pathlib import Path
import logging


logging.basicConfig(format='[%(asctime)s] - %(levelname)s - %(message)s')
logger = logging.getLogger('directory_builder')
logger.setLevel(logging.INFO)

project_name = 'pilotproject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]

for filepath in list_of_files:
    filedir, filename = Path(filepath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logger.info(f'Creating the directory {filedir} for file : {filename}')
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filename, 'w'):
            pass
            logger.info(f'Creating empty file: {filename}')
    else:
        logger.info(f'File : {filename} already exists')
        