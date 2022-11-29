from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.domain.terms import Term


router = APIRouter(
    prefix="/term",
    tags=["Term"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def read_term_list():
    return {"term_list": []}


@router.get("/{term_id}")
def read_term(term_id: int):
    term = {}
    return {"term": term}


@router.post("/")
def create_term(term: Term):
    term = {}
    return {"term": Term}


@router.patch("/{term_id}")
def update_term(term_id: int):
    term = {}
    return {"term": Term}


@router.delete("/{term_id}")
def delete_term(term_id: int):
    term = {}
    return {"message": "Delete successful"}