import pika, json

msg = {
    "urls": [
        "git@github.com:os3224/homework-5-filesystem-4f727de3-srg537.git",
        "git@github.com:os3224/homework-5-filesystem-4f727de3-sp6370.git",
        "git@github.com:os3224/homework-5-filesystem-4f727de3-an3015.git",
    ]
}

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mayat')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=json.dumps(msg)
)
print(" [x] Sent 'Hello World!'")
connection.close()