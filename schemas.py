from pydantic import BaseModel


class GithubRepoLinksPydantic(BaseModel):
    links: list[str]