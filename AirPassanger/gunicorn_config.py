# gunicorn_config.py

import multiprocessing

bind = "0.0.0.0:80"  # Replace with your desired host and port
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "logfile/error.log"  # Replace with your log file path
accesslog = "logfile/access.log"  # Replace with your log file path
