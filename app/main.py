from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from .api.v1 import words, domain, terms


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(words.router)
app.include_router(domain.router)
app.include_router(terms.router)


@app.get("/")
async def index(token: str = Depends(oauth2_scheme)):
    return {"message": "Ok"}


@app.get("/health-check")
def health_check():
    return {"message": "Ok"}