import os
from pathlib import Path
import logging

# Define the directory where logs will be stored
log_dir = "logs"
log_filepath = os.path.join(log_dir, 'directorygen_logs.log')

# Ensure the logs directory exists before writing logs
os.makedirs(log_dir, exist_ok=True)

# Create a FileHandler to save logs to a file
file_handler = logging.FileHandler(log_filepath)

# Create a StreamHandler to print logs to the console
stream_handler = logging.StreamHandler()

# Configure logging with both file and console handlers
logging.basicConfig(
    format='[%(asctime)s] - %(levelname)s - %(message)s',
    handlers=[file_handler, stream_handler]
)

# Create a logger instance with a specific name
logger = logging.getLogger('directory_builder')
logger.setLevel(logging.INFO)  # Set log level to INFO (ignores DEBUG messages)

# Define the project name
project_name = 'pilotproject'

# List of files and directories that should be created
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

# Iterate over the list of files to create necessary directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and filename

    # Ensure the directory exists before creating the file
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating the directory '{filedir}' for file : '{filename}'")
    
    # Check if the file does not exist or is empty, then create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w'):  # Create an empty file
            pass
        logger.info(f"Creating empty file: '{filepath}'")
    else:
        logger.info(f"'{filepath}' already exists")
