"""Main module."""
from pypack import logs

logger = logs.get_logger(__name__)


def a_function() -> str:
    logger.debug("Generating hello world string")
    return "Hello World!"
