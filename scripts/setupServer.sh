#!/bin/bash


echo "Setting up server..." && \


echo "Setting up Django data..." && \

python manage.py collectstatic --noinput && \

python manage.py migrate --database=default &&


echo "Done setting up server!"
