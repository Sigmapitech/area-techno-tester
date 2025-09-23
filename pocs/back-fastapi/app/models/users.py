from pydantic import Field
from sqlalchemy import Column, Integer, String

from ..db import Base
from ._table_name_provider import TableNameProvider


class User(Base, TableNameProvider):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True, unique=True)
    name = Column(String, nullable=False, index=True, unique=True)
    auth = Column(String, nullable=False)
    perms = Column(Integer, nullable=False, default=0)

    # For the POC scope, this is enough
    discord_access_token = Column(String, nullable=True)
    discord_refresh_token = Column(String, nullable=True)
    discord_expires_in = Column(Integer, nullable=True)
