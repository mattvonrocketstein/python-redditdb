"""
"""
import os
from dotenv import load_dotenv

from .util import get_logger
from .db import RedditDB

logger = get_logger(__name__)
logger.debug("Loading .env")
load_dotenv(os.path.join(os.getcwd(), '.env'), verbose=True)
