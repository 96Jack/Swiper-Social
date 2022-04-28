#!/bin/bash

echo "start gunicorn server..."
gunicorn -c swiper/gunicorn_config.py swiper.wsgi
echo "success start"



