import os
import uuid
import git
import mayat
from fastapi import FastAPI, UploadFile
from .schemas import *

SCRATCH_DIR = "scratch"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/check_github_repos")
async def check_github_repos(github_repo_links: GithubRepoLinksPydantic):
    return {"id": 1}

@app.post("/check_zip_file")
async def check_zip_file(zip_file: UploadFile):
    return {"message": "Hello World"}

@app.get("/get_result/{result_id}")
async def get_result(result_id: int):
    return ("message": "Hello World")