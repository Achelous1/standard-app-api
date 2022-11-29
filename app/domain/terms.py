from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

from . import AbstractTableBase, AbstractBaseModel


class TermTable(AbstractTableBase):
    __tablename__ = 'term'
    trm_id = Column(Integer, primary_key=True, autoincrement="auto")
    trm_lgcl_nm: Column(String(50), nullable=False)
    trm_phcl_nm: Column(String(50), nullable=False)
    trm_eng_nm: Column(String(50), nullable=False)


class Term(AbstractBaseModel):
    trm_id: int
    trm_lgcl_nm: str
    trm_phcl_nm: str
    trm_eng_nm: str