import os
import uuid
import git

SCRATCH_DIR = "scratch"

repo_url = "git@github.com:os3224/homework-5-filesystem-4f727de3-srg537.git"

cloned_repo = git.Repo.clone_from(
    repo_url,
    os.path.join(SCRATCH_DIR, f"github_repos_{uuid.uuid4()}/{repo_url.split('/')[1].split('.')[0]}")
)