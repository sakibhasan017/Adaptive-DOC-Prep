from fastapi import FastAPI
from app.prep import run_prep
from app.kb import init_db

app = FastAPI()

init_db()


@app.get("/")
def root():
    return {"message": "Adaptive Doc Prep API"}


@app.post("/prep")
def prep(section_ids: list[int]):
    return run_prep(section_ids)