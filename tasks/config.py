# -*- encoding: utf-8 -*-

# 通用
timezone = 'Asia/shanghai'
# accept_content = ['pickle', 'json']
accept_content = ['json']
worker_redirect_stdouts_level = 'INFO'

# broker: 消息队列的配置
broker_url = 'redis://127.0.0.1:6379/3' 
broker_pool_limit = 100 # broker的连接池， 默认是10
# task_serizlizer = 'pickle' # 任务的序列化
task_serizlizer = 'pickle' # 任务的序列化

# 结果的配置
result_backend = 'redis://127.0.0.1:6379/3'
# result_serializer = 'pickle' # 结果的序列化
result_serializer = 'pickle' # 结果的序列化
result_experies = 3600 # 任务的过期时间
result_cache_max = 10000 # 任务结果最大缓存数量