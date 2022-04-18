from multiprocessing import cpu_count

# 私网ip开启服务器
bind = ['10.0.4.2:8000']
# 开启守护进程模式：后台运行      
daemon = True
pidfile = "logs/gunicorn.pid"


# 工作进程数量
workers = cpu_count() * 2
# 指定异步处理库：在gunicorn内部已经封装好gevent相关的东西
# worker_class = "gevent"
worker_class = "egg:meinheld#gunicorn_worker"

# 每个进程的最大连接数
worker_connections = 65535

# 服务器保持连接的时间，避免频繁的三次握手过程：60s内其他请求保持连接，若60s内无请求则断开连接
keepalive = 60 
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = "*"

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/error.log'
