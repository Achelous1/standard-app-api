from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class DomainTable(Base):
    __tablename__ = 'domain'
    dmn_id = Column(Integer, primary_key=True)
    dmn_lgcl_nm: Column(String(50), nullable=False)
    dmn_phcl_nm: Column(String(50), nullable=False)
    dmn_eng_nm: Column(String(50), nullable=False)


class Domain(BaseModel):
    dmn_id: int
    dmn_lgcl_nm: str
    dmn_phcl_nm: str
    dmn_eng_nm: str