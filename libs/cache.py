from logging import exception
import pickle
from redis import Redis as _Redis

from swiper.cfg import REDIS


class Redis(_Redis):
    """重写redis方法,使其可以序列化"""
    def set(self, name, value):
        pickled_data = pickle.dumps(value, pickle.HIGHEST_PROTOCOL)
        return super().set(name, pickled_data)

    def get(self, name, default=None):
        pickled_data = super().get(name)
        if pickled_data is None:
            return default
        else:
            try:
                return pickle.loads(pickled_data)
            except (TypeError, pickle.UnpicklingError):
                return pickled_data
            
    
rds = Redis(**REDIS)

