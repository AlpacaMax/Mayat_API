from pydantic import BaseModel, validator


class GitRepoLinksPydantic(BaseModel):
    urls: list[str]
    file: str
    language: str
    function_name: str = "*"
    threshold: int = 5