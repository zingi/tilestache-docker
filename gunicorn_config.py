import multiprocessing

bind = "0.0.0.0:8080"
loglevel = "debug"
workers = multiprocessing.cpu_count() * 2 + 1