import pika
from fastapi import FastAPI, UploadFile, Depends
from sqlalchemy.orm import Session

from database import engine
import models
import schemas
import utils


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/check_git_repos")
async def check_git_repos(
    repo_links: schemas.GitRepoLinksPydantic,
    db: Session = Depends(utils.get_db),
):
    new_task = models.Task()
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    repo_links.task_id = new_task.id
    repo_links_json = repo_links.json()

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

    return new_task

@app.post("/check_zip_file")
async def check_zip_file(zip_file: UploadFile):
    return {"message": "Hello World"}

@app.get("/task/{task_id}")
async def get_result(task_id: int, db: Session = Depends(utils.get_db)):
    return db.get(models.Task, task_id)