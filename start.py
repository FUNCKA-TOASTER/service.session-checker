"""Service "toaster.comman-handling-service".
About:
    ...

Author:
    Oidaho (Ruslan Bashinskii)
    oidahomain@gmail.com
"""

import asyncio
from handler import session_handler
from logger import logger


async def main():
    """Entry point."""
    log_text = "Starting session checking..."
    await logger.info(log_text)

    await session_handler()


if __name__ == "__main__":
    asyncio.run(main())
