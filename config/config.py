"""Module "config".

File:
    config.py

About:
    This file defines the used variables
    and configuration objects.
"""

import os
from toaster.credentials import (
    AlchemyCredentials,
    AlchemySetup,
)

# Service name used for identification
SERVICE_NAME = "toaster.session-checker-service"

# API token obtained from environment variable
TOKEN: str = os.getenv("TOKEN")

# Group ID for identifying specific groups
GROUP_ID: int = int(os.getenv("GROUPID"))

# API version used for API requests
API_VERSION: str = "5.199"

# Delay between checking iterrations in seconds
ITERRATION_DELAY = 60

# Setup for sqlalchemy. Driver, Database and DBMS.
ALCHEMY_SETUP = AlchemySetup(
    dialect="mysql",
    driver="pymysql",
    database="toaster_dev",  # TODO: Позже заменить на toaster
)

# DBMS credentials that includes host, port, user, password.
DBMS_CREDS = AlchemyCredentials(
    host=os.getenv("SQL_HOST"),
    port=int(os.getenv("SQL_PORT")),
    user=os.getenv("SQL_USER"),
    pswd=os.getenv("SQL_PSWD"),
)
