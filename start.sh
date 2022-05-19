#!/bin/bash

echo "start gunicorn server..."
source .venv/bin/activate
gunicorn -c swiper/gunicorn_config.py swiper.wsgi
echo "success start"



