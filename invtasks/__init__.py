from invoke import ctask, run
from config import PROCESSORS, RUN_PORT, FLOWER_PORT, DEBUG


@ctask
def server(ctx):
    from rfdmovies import app
    app.run('0.0.0.0', port=RUN_PORT, debug=DEBUG)


@ctask
def gunicorn(ctx):
    port = RUN_PORT
    nprocs = PROCESSORS
    cmd = "gunicorn -w {} -k gevent -b 0.0.0.0:{} rfdmovies:app --access-logfile {}"
    run(cmd.format(nprocs, port, "-"))


@ctask
def celery(ctx):
    cmd = 'celery --app=rfdmovies.celery worker --loglevel=INFO --beat'
    run(cmd)


@ctask
def flower(ctx):
    cmd = 'flower -A rfdmovies.celery --port={}'.format(FLOWER_PORT)
    run(cmd)
