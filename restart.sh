#!/bin/bash

Gunicorn_pid=`cat logs/gunicorn.pid `
echo "Gunicorn_pid: $Gunicorn_pid"
kill -HUP $Gunicorn_pid
