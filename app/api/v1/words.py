from fastapi import APIRouter, Depends, HTTPException
from typing import List

from domain.words import Word


router = APIRouter(
    prefix="/words",
    tags=["Words"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def read_word_list():
    return {"words_list": []}


@router.get("/{word_id}")
def read_word(word_id: int):
    word = {}
    return {"word": word}


@router.post("/")
def create_word(word: Word):
    return {"word": word}


@router.patch("/{word_id}")
def update_word(word_id: int):
    word = {}
    return {"word": word}


@router.delete("/{word_id}")
def delete_word(word_id: int):
    word = {}
    return {"message": "Delete successful"}