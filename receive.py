import pika, sys, os, json, git, time, shutil
from sqlalchemy import update
from mayat.frontends import TS_C, TS_Java, TS_Python
from mayat.Result import serialize_result

import models
from database import SessionLocal
from utils import *

SCRATCH_DIR = "scratch"
language_mapper = {
    "C": TS_C,
    "Java": TS_Java,
    "Python": TS_Python,
}

def callback(ch, method, properties, body):
    repo_links = json.loads(body)

    if repo_links["language"] not in language_mapper:
        session = SessionLocal()
        stmt = (
            update(models.Task)
            .where(models.Task.id == repo_links["task_id"])
            .values(
                message = f"Unsupported Language! We currently support {', '.join(language_mapper.keys())}.",
                status = models.TaskStatus.Error,
            )
        )
        session.execute(stmt)
        session.commit()
        session.close()
        
        return

    repos_root_dir = gen_repos_root_dirname()
    repos_paths = []
    for url in repo_links["urls"]:
        print(url)
        path = os.path.join(
            SCRATCH_DIR,
            repos_root_dir,
            gen_repo_dirname(url)
        )

        repos_paths.append(os.path.join(path, repo_links["file"]))

        git.Repo.clone_from(
            url,
            path,
            env={"GIT_TRACE": "1", "GIT_CURL_VERBOSE": "1"},
            multi_options=["--verbose"],
        )
    print()

    result = language_mapper[repo_links["language"]].main(
        source_filenames=repos_paths,
        function_name=repo_links["function_name"],
        threshold=repo_links["threshold"]
    )
    serialized_result = serialize_result(
        result,
        format="JSON",
        list_all=False
    )
    shutil.rmtree(os.path.join(SCRATCH_DIR, repos_root_dir))

    session = SessionLocal()
    stmt = (
        update(models.Task)
        .where(models.Task.id == repo_links["task_id"])
        .values(
            result = serialized_result,
            status = models.TaskStatus.Finished
        )
    )
    session.execute(stmt)
    session.commit()
    session.close()

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue='mayat')

    channel.basic_consume(
        queue='mayat',
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)