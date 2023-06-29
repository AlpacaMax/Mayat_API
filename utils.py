import uuid
import os

from database import SessionLocal

def gen_repos_root_dirname():
    return f"github_repos_{uuid.uuid4()}"

def gen_zip_file_dirname():
    return f"zip_file_{uuid.uuid4()}"

def gen_repo_dirname(repo_url):
    return repo_url.split('/')[-1].split('.')[0]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
