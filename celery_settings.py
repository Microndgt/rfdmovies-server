from celery.schedules import crontab
from config import PROCESSORS, RM_VHOST, RM_PORT, RM_HOST, RM_PWD, RM_USER, SSDB_PORT, SSDB_HOST, SSDB_PASSWORD

# celery 配置
BROKER_URL = 'pyamqp://{}:{}@{}:{}/{}'.format(RM_USER, RM_PWD, RM_HOST, RM_PORT, RM_VHOST)
CELERY_RESULT_BACKEND = "rfdmovies.ssdb.SSDBBackend"
CELERY_SSDB_BACKEND_SETTINGS = {
    "host": SSDB_HOST,
    "port": SSDB_PORT,
    "password": SSDB_PASSWORD,
    "expires": None
}
CELERY_RESULT_SERIALIZER = 'json'
# 防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 40
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False
CELERY_IMPORTS = ()

CELERY_SEND_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True
# celery worker的并发数
CELERYD_CONCURRENCY = PROCESSORS
# celery任务执行结果的超时时间,A value of None or 0 means results will never expire
CELERY_TASK_RESULT_EXPIRES = None
CELERY_REDIRECT_STDOUTS_LEVEL = "INFO"
# CELERYBEAT_SCHEDULE = {}
