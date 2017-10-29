#!/usr/bin/env bash
nohup /usr/local/bin/inv web.celery &
nohup /usr/local/bin/inv web.flower &
inv web.gunicorn
