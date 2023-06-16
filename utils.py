import uuid
import os

def gen_repos_root_dirname():
    return f"github_repos_{uuid.uuid4()}"

def gen_repo_dirname(repo_url):
    return repo_url.split('/')[-1].split('.')[0]