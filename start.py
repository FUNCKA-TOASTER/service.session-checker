"""Service "service.session-checker".

File:
    start.py

About:
    This service is responsible for checking and deleting
    expired menu sessions.
"""

import sys
from typing import Callable
from loguru import logger
from handler import SessionHandler
from apscheduler.schedulers.blocking import BlockingScheduler


def setup_logger() -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <red>{module}</red> | <level>{level}</level> | {message}",
        level="DEBUG",
    )


def setup_scheduler(job: Callable) -> BlockingScheduler:
    scheduler = BlockingScheduler()
    scheduler.add_job(
        func=job,
        trigger="cron",
        second=0,
    )


def main() -> None:
    """Program entry point."""

    setup_logger()
    check_sessions = SessionHandler()

    scheduler = setup_scheduler(job=check_sessions)

    logger.info("Starting session checking...")
    scheduler.start()


if __name__ == "__main__":
    main()
