from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr
from pydantic import BaseModel
from datetime import datetime

from app.config.databases import Base


class AbstractTableMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    reg_dtt = Column(DateTime, server_default=func.now())
    upd_dtt = Column(DateTime, onupdate=func.now())



class AbstractBaseModel(BaseModel):
    reg_dtt: datetime
    upd_dtt: datetime