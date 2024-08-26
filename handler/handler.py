"""Module "handler".

File:
    handler.py

About:
    File describing session handler class.
"""

from typing import Any
from vk_api import VkApi
from loguru import logger
from funcka_bots.handler import ABCHandler
from toaster.scripts import (
    close_menu_session,
    get_expired_sessions,
)
import config


class SessionHandler(ABCHandler):
    """Session handler class"""

    def __call__(self, _=None) -> None:
        try:
            reqsponse = self._execute()
            logger.info(reqsponse)

        except Exception as error:
            logger.error(error)

        finally:
            logger.info("Waiting for next checnking iteration...")

    def _execute(self) -> str:
        sessions = get_expired_sessions()

        if not sessions:
            return "No expired sessions."

        api = self._get_api()
        for bpid, cmids in sessions:
            for cmid in cmids:
                close_menu_session(bpid=bpid, cmid=cmid)

            api.messages.delete(
                peer_id=bpid,
                cmids=cmids,
                delete_for_all=1,
            )

        response = f"Closed {len(sessions)} sessions."
        return response

    def _get_api(self) -> Any:
        session = VkApi(
            token=config.VK_GROUP_TOKEN,
            api_version=config.VK_API_VERSION,
        )
        return session.get_api()
