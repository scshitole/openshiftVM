# Gunicorn configuration file
import multiprocessing

# Server socket
bind = "0.0.0.0:5000"
backlog = 1024

# Worker processes - using fewer workers to prevent memory issues
workers = 2  # Reduced from dynamic calculation to fixed number
worker_class = 'sync'
worker_connections = 750
timeout = 60
keepalive = 2

# Logging
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '-'
loglevel = 'debug'

# Process naming
proc_name = 'llama-chat'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Max requests per worker before reload
max_requests = 1000
max_requests_jitter = 50

# SSL
keyfile = None
certfile = None

