from flask import Flask
from werkzeug.local import LocalProxy
from celery import Celery


def create_app():
    app = Flask(__name__)
    return app


def make_celery(app):
    celery = Celery(app.__name__)
    celery.config_from_object('celery_settings')
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app = LocalProxy(create_app)
celery = make_celery(app)
