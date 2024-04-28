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

            log_message = f"Fetched sessions: \n  {sessions}"
            await logger.info(log_message)

            for peer_id, cmids in sessions:
                self.api.messages.delete(peer_id=peer_id, cmids=cmids, delete_for_all=1)

            await asyncio.sleep(60)

    @staticmethod
    async def group(session_list: tuple) -> dict:
        result = {}
        for peer_id, cmid in session_list:
            cmids = result.get(peer_id, "")
            cmids += f"{cmid}, "

            result[peer_id] = cmids

        return result


session_handler = SessionHandler()
