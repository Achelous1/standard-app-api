from sqlalchemy import Column
from pydantic import BaseModel
from datetime import datetime

from app.config.databases import Base


class AbstractTableBase(Base):
    reg_dtt = Column(Datetime, server_default=text('NOW()'))
    upd_dtt = Column(Datetime)


class AbstractBaseModel(BaseModel):
    reg_dtt: datetime
    upd_dtt: datetime