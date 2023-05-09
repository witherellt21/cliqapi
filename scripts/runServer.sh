#!/bin/bash

# Restart server automatically if it dies unexpectedly
while true; do

    echo "Starting server listening on port $SERVER_PORT..."
    # python -u manage.py runserver 0.0.0.0:8000 > >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt) 2> >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt >&2)
    # uwsgi --socket uwsgi.sock --chmod-socket=666 --enable-threads --workers $NUM_WORKERS --module app.wsgi > >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt) 2> >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt >&2)
    # uwsgi --ini config/uwsgi/uwsgi_dev.ini --honour-stdin > >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt) 2> >(tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt >&2)
    # gunicorn app.wsgi
    # gunicorn --config config/uwsgi/uwsgi.py
    python manage.py runserver

    echo "Server running."

    EXITSTATUS=$?
    if [[ $EXITSTATUS -eq 0 ]]; then
        exit 0
    fi

    echo "Server process exited with $EXITSTATUS. Restarting..." | tee -a logs/log_server_$(date '+%Y-%m-%d-%H').txt
    sleep 1
done
