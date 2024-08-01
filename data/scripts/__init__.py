"""Module "scripts".

File:
    __init__.py

About:
    Initializing the "scripts" module.
"""

from .peer import (
    get_peer_mark,
    set_peer_mark,
    drop_peer_mark,
    update_peer_data,
    get_log_peers,
)
from .user import (
    get_user_permission,
    set_user_permission,
    update_user_permission,
    drop_user_permission,
    get_user_warns,
    get_user_queue_status,
    insert_user_to_queue,
)
from .setting import (
    get_destinated_settings_status,
    get_setting_status,
    update_setting_status,
    get_setting_points,
    update_setting_points,
)
from .delay import (
    get_setting_delay,
    update_setting_delay,
)
from .session import (
    open_menu_session,
    close_menu_session,
    get_expired_sessions,
)
from .url import insert_pattern, get_patterns
from .cursed import insert_cursed, get_curse_words

__all__ = (
    "get_peer_mark",
    "set_peer_mark",
    "update_peer_data",
    "drop_peer_mark",
    "get_user_permission",
    "set_user_permission",
    "update_user_permission",
    "drop_user_permission",
    "get_destinated_settings_status",
    "get_setting_status",
    "update_setting_status",
    "get_setting_points",
    "update_setting_points",
    "get_setting_delay",
    "update_setting_delay",
    "get_user_warns",
    "get_user_queue_status",
    "insert_user_to_queue",
    "insert_pattern",
    "get_patterns",
    "insert_cursed",
    "get_curse_words",
    "get_log_peers",
    "open_menu_session",
    "close_menu_session",
    "get_expired_sessions",
)
