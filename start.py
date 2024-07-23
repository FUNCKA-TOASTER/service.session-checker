"""Service "toaster.comman-handling-service"."""

import sys
import time
import config
from loguru import logger
from data import TOASTER_DB
from handler import SessionHandler


def setup_logger() -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <red>{module}</red> | <level>{level}</level> | {message}",
        level="DEBUG",
    )


def main() -> None:
    """Entry point."""

    setup_logger()
    TOASTER_DB.create_tables()
    start_checking = SessionHandler()

    logger.info("Starting session checking...")
    while True:
        start_checking()
        time.sleep(config.ITERRATION_DELAY)


if __name__ == "__main__":
    main()
