import os
import logging
import sys

# Define the log message format including timestamp, log level, module name, and log message
log_format = "[%(asctime)s] - %(levelname)s - %(module)s - %(message)s"

# Directory where log files will be stored
log_dir = 'logs'

# Name of the log file
log_filename = 'app_logs.log'

# Complete path of the log file
log_filepath = os.path.join(log_dir, log_filename)


def create_logger():
    """
    Creates and configures a logger instance named 'app_logger'.
    Ensures logs are written both to a file and to standard output.
    Prevents duplicate handlers from being attached if called multiple times.
    """

    # Ensure that the logs directory exists; create it if it doesn't
    os.makedirs(log_dir, exist_ok=True)

    # Create or retrieve a logger instance
    logger = logging.getLogger('app_logger')

    # Set the minimum logging level to DEBUG, capturing all types of logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(level=logging.DEBUG)

    # Check if the logger already has handlers attached; if not, proceed to add them
    if not logger.hasHandlers():

        # Create a formatter object using the specified log format
        formatter = logging.Formatter(log_format)

        # Create a file handler to write logs to a file, using append mode ('a')
        file_handler = logging.FileHandler(log_filepath, mode='a')
        file_handler.setFormatter(formatter)

        # Create a stream handler to print logs to standard output (console)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        # Add both file and stream handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    # Return the configured logger instance
    return logger


# Instantiate and configure logger using create_logger function
logger = create_logger()

# Example usage (Uncomment to test logging functionality)
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
