#!/bin/bash


echo "Setting up server..." && \


echo "Setting up Django data..." && \

python manage.py collectstatic --noinput && \

python manage.py migrate --database=default && \
# python manage.py migrate --database=default users zero && \
# python manage.py migrate --database=default && movies zero \
# python manage.py migrate --database=default movies && \
# python manage.py migrate --database=default users && \
# python manage.py migrate --database=default && \

# python manage.py migrate users
# python manage.py migrate
# python manage.py migrate --fake admin zero


echo "Done setting up server!"
