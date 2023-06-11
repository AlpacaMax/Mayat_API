import os
import uuid
import git
import mayat
from fastapi import FastAPI, UploadFile

from schemas import *
from utils import *

SCRATCH_DIR = "scratch"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/check_git_repos")
async def check_git_repos(repo_links: GitRepoLinksPydantic):
    repos_root_dir = gen_repos_root_dirname()
    for url in repo_links.urls:
        git.Repo.clone_from(
            url,
            os.path.join(SCRATCH_DIR, repos_root_dir, gen_repo_dirname(url))
        )

    return {"id": 1}

@app.post("/check_zip_file")
async def check_zip_file(zip_file: UploadFile):
    return {"message": "Hello World"}

@app.get("/get_result/{result_id}")
async def get_result(result_id: int):
    return {"message": "Hello World"}