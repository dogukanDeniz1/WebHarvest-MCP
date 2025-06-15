import logging
import sys
import os

# Create a logger
logger = logging.getLogger("WebHarvest-MCP")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)

# Add handler if not already present
if not logger.hasHandlers():
    logger.addHandler(ch)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
ch.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

# Helper functions

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def fatal(msg, *args, **kwargs):
    logger.fatal(msg, *args, **kwargs)
