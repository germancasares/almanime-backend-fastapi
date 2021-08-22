from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    creation_date: datetime
    modification_date: Optional[datetime] = None

    class Config:
        orm_mode = True
