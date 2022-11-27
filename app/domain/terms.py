from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class TermTable(Base):
    __tablename__ = 'term'
    trm_id = Column(Integer, primary_key=True)
    trm_lgcl_nm: Column(String(50), nullable=False)
    trm_phcl_nm: Column(String(50), nullable=False)
    trm_eng_nm: Column(String(50), nullable=False)


class Term(BaseModel):
    trm_id: int
    trm_lgcl_nm: str
    trm_phcl_nm: str
    trm_eng_nm: str