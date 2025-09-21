from sqlalchemy import Boolean, Column, Integer, String

from ..db import Base
from ._table_name_provider import TableNameProvider


class User(Base, TableNameProvider):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True, unique=True)
    name = Column(String, nullable=False, index=True, unique=True)
    auth = Column(String, nullable=False)
    perms = Column(Integer, nullable=False, default=0)
