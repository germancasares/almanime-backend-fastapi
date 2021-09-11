from datetime import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import as_declarative
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime


@as_declarative()
class Base(object):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    modification_date = Column(DateTime)
