import json

from django.http import HttpResponse
from django.conf import settings
from common.stat import OK
from libs.my_encode import OurEncoder


def render_json(data=None, code=OK):
    """
    封装json接口
    当处于debug状态的时候;空格较多,格式比较容易识别
    当处于传输状态的时候,空格较少,利于传输
    JsonResponse()本质是继承HttpResponse功能
    """
    result = {
        'data':data,
        'code':code
    }

    if settings.DEBUG:
        json_result = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_result = json.dumps(result, cls=OurEncoder, ensure_ascii=False, separators=(',',':')) 
        # print("type_result========================================\n{}".format(type(result)))
        # print("json_result:=======================================\n{}".format(json_result))
    return HttpResponse(json_result) 