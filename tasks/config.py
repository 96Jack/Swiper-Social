# -*- encoding: utf-8 -*-


timezone = 'Asia/shanghai'
accept_content = ['pickle', 'json']
worker_redirect_stdouts_level = 'INFO'

broker_url = 'redis://127.0.0.1:6379/3'
# broker的连接池
broker_pool_limit = 100 
task_serizlizer = 'pickle'

result_backend = 'redis://127.0.0.1:6379/3'
result_serializer = 'pickle'
# 任务的过期时间
result_experies = 3600
# 任务结果最大缓存数量
result_cache_max = 10000