from datetime import datetime as dt
import environ
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

print(env)

# ---- FOR DEVELOPMENT - reload the app on code changes
reload = True
# spew                        = True

# ---- Server Hooks
# worker_abort                =                                                # function(worker) -> clear environment


# ---- Django settings
chdir = "/app"
wsgi_app = "app.wsgi:application"


# ---- socket information
bind = f"0.0.0.0:{env('SERVER_PORT')}"  # HOST:PORT
backlog = 2048  # number of connections in the queue


# ---- process settings
# workers = multiprocessing.cpu_count() * 2 + 1
workers = env("NUMBER_OF_WORKERS")
# worker_class                = 'eventlet'
# worker_connections          = 1000
proc_name = "bloop-api-server"
threads = 1


# ---- worker automatic restarts
max_requests = 50
timeout = 30


# ---- Logging
# now = dt.now()
# string = now.strftime('logs/log_server_%Y-%m-%d-%H')
# accesslog = f"{dt.now().strftime('logs/log_server_%Y-%m-%d-%H')}.txt"
# errorlog = accesslog
# access_log_format           = 'logs/log_server_%(t)s-%(T)s.txt'
# errorlog                    = 'logs/log_server_%(t)s-%(T)s.txt'
capture_output = False
# loglevel = "debug"


# ---- Security
# limit_request_line          = 50
limit_request_fields = 32768


# ---- Server operation
preload_app = True
# daemon                      = True     # detach mode
# worker_tmp_dir              = ''       # a directory to use for the worker heartbeat temporary file.
