from fastapi import FastAPI

from .api.v1 import words, domain, terms


app = FastAPI()

app.include_router(words.router)
app.include_router(domain.router)
app.include_router(terms.router)


@app.get("/")
async def index():
    return {"message": "Ok"}


@app.get("/health-check")
def health_check():
    return {"message": "Ok"}