import os
import git
import mayat
import pika
from fastapi import FastAPI, UploadFile

from schemas import *
from utils import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/check_git_repos")
async def check_git_repos(repo_links: GitRepoLinksPydantic):
    repo_links_json = repo_links.json();

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='mayat')

    channel.basic_publish(
        exchange='',
        routing_key='mayat',
        body=repo_links_json
    )

    connection.close()

    return {"id": 1}

@app.post("/check_zip_file")
async def check_zip_file(zip_file: UploadFile):
    return {"message": "Hello World"}

@app.get("/get_result/{result_id}")
async def get_result(result_id: int):
    return {"message": "Hello World"}