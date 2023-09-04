#!/bin/bash


echo "Setting up server..." && \


echo "Setting up Django data..." && \

python manage.py collectstatic --noinput && \

python manage.py migrate --database=default && \
# python manage.py migrate --database=default --fake myapp zero && \
# python manage.py migrate --database=default --fake movie zero && \
# python manage.py migrate --database=default --fake admin zero && \
# python manage.py migrate --database=default --fake auth zero && \
# python manage.py migrate --database=default movies && \
# python manage.py migrate --database=default users && \
# python manage.py migrate --database=default && \

# python manage.py migrate users
# python manage.py migrate
# python manage.py migrate --fake admin zero


echo "Done setting up server!"
