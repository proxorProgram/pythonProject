from celery import Celery

app = Celery('documents_app',
             broker='amqp://guest:guest@rabbitmq:5672//',
             include=['documents_app.tasks'])

if __name__ == '__main__':
    app.start()
