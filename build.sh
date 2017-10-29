#!/bin/bash

date_=$(date +"%y%m%d")
pwd_=$(cd `dirname $0`; pwd)

docker build -t ability:${date_} .
