import json
class OurEncoder(json.JSONEncoder):
    def default(self, obj):
        # print("type(type)------------------\n:{}".format(type(obj)))
        if isinstance(obj, bytes):        # xxx是你要编码的类型
            return str(obj, encoding='utf-8')             # 返回你定义的处理方法
        return super(OurEncoder, self).default(obj)  # 对于其他处理不了的类，依然抛出一个错误