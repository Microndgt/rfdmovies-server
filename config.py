import os
import multiprocessing

basedir = os.path.abspath(os.path.dirname(__file__))

PROCESSORS = multiprocessing.cpu_count()
RUN_PORT = 5000
FLOWER_PORT = 5001
DEBUG = False

# rabbitmq
RM_USER = 'celery'
RM_PWD = 'celerypwd'
RM_HOST = '127.0.0.1'
RM_PORT = 5672
RM_VHOST = 'celery_host'

# ssdb
SSDB_HOST = '127.0.0.1'
SSDB_PORT = 8888
SSDB_PASSWORD = ''
