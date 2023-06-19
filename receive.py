import pika, sys, os, json, git, time, shutil
from mayat.frontends import TS_C
from mayat.Result import print_result
from utils import *

SCRATCH_DIR = "scratch"

def callback(ch, method, properties, body):
    repo_links = json.loads(body)

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

    result = TS_C.main(
        source_filenames=repos_paths,
        function_name=repo_links["function_name"],
        threshold=repo_links["threshold"]
    )

    print_result(
        result,
        format="JSON",
        list_all=False
    )

    shutil.rmtree(os.path.join(SCRATCH_DIR, repos_root_dir))

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