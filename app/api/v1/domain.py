from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.domain.domains import Domain


router = APIRouter(
    prefix="/v1/domain",
    tags=["Domain"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def read_domain_list():
    return {"domain_list": []}


@router.get("/{domain_id}")
def read_domain(domain_id: int):
    domain = {}
    return {"domain": domain}


@router.post("/")
def create_domain(domain: Domain):
    domain = {}
    return {"domain": domain}


@router.patch("/{domain_id}")
def update_domain(domain_id: int):
    domain = {}
    return {"domain": domain}


@router.delete("/{domain_id}")
def delete_domain(domain_id: int):
    domain = {}
    return {"message": "Delete successful"}