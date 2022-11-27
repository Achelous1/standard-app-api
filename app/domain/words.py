from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class WordTable(Base):
    __tablename__ = 'word'
    wrd_id = Column(Integer, primary_key=True)
    wrd_lgcl_nm: Column(String(50), nullable=False)
    wrd_phcl_nm: Column(String(50), nullable=False)
    wrd_eng_nm: Column(String(50), nullable=False)


class Word(BaseModel):
    wrd_id: int
    wrd_lgcl_nm: str
    wrd_phcl_nm: str
    wrd_eng_nm: str