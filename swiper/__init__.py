# pymysql 初始化

import pymysql

from libs.orm import patch

# sys.modules["MySQLdb"] = sys.modules["_mysql"] = sys.modules["pymysql"]
# 用pymysql替换Mysqldb : Monkey patch : 打补丁
pymysql.install_as_MySQLdb()

# 在系统加载之前就加载数据
patch()
