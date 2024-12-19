#!/bin/bash

export PROJECT_HOME=`pwd`

cd $PROJECT_HOME/worker
docker build -f Dockerfile -t celery-base:1.0 .

cd $PROJECT_HOME