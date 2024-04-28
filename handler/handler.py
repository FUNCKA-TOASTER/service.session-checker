from vk_api import VkApiError
from logger import logger
from db import db
from .abc import ABCHandler
import asyncio


class SessionHandler(ABCHandler):
    """Event handler class that recognizes commands
    in the message and executing attached to each command
    actions.
    """

    async def _handle(self) -> bool:
        while True:
            log_message = "Waiting for checnking iteration."
            await logger.info(log_message)

            query = """
            SELECT 
                conv_id,
                cm_id 
            FROM 
                menu_sessions
            WHERE
                expired <= NOW();
            """
            sessions = db.execute.raw(schema="toaster", query=query)
            sessions = await self._group(sessions)

            if not sessions:
                log_message = "There are no expired sessions."
            else:
                log_message = f"Fetched sessions: \n  {sessions}"

            await logger.info(log_message)

            for peer_id, cmids in sessions.items():
                try:
                    self.api.messages.delete(
                        peer_id=peer_id, cmids=cmids, delete_for_all=1
                    )
                except VkApiError:
                    ...

            await asyncio.sleep(60)

    async def _group(self, session_list: tuple) -> dict:
        result = {}
        for peer_id, cmid in session_list:
            await self._expose_session(peer_id, cmid)
            cmids = result.get(peer_id, "")
            cmids += f"{cmid}, "

            result[peer_id] = cmids

        return result

    @staticmethod
    async def _expose_session(peer_id, cmid):
        db.execute.delete(
            schema="toaster", table="menu_sessions", conv_id=peer_id, cm_id=cmid
        )


session_handler = SessionHandler()
