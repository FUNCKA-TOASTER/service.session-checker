from typing import Any
from vk_api import VkApi
from loguru import logger
from db import TOASTER_DB
from toaster_utils.scripts import (
    close_menu_session,
    get_expired_sessions,
)
import config


class SessionHandler:
    """DOCSTRING"""

    def __call__(self) -> None:
        try:
            reqsponse = self._execute()
            logger.info(reqsponse)

        except Exception as error:
            logger.error(error)

        finally:
            logger.info("Waiting for next checnking iteration...")

    def _execute(self) -> str:
        sessions = get_expired_sessions(db_instance=TOASTER_DB)

        if not sessions:
            return "No expired sessions."

        api = self._get_api()
        for bpid, cmids in sessions:
            for cmid in cmids:
                close_menu_session(
                    db_instance=TOASTER_DB,
                    bpid=bpid,
                    cmid=cmid,
                )

            api.messages.delete(
                peer_id=bpid,
                cmids=cmids,
                delete_for_all=1,
            )

        response = f"Closed {len(sessions)} sessions."
        return response

    def _get_api(self) -> Any:
        session = VkApi(
            token=config.TOKEN,
            api_version=config.API_VERSION,
        )
        return session.get_api()
