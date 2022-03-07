# pymysql 初始化

import pymysql

# sys.modules["MySQLdb"] = sys.modules["_mysql"] = sys.modules["pymysql"]
# 用pymysql替换Mysqldb : Monkey patch : 打补丁
pymysql.install_as_MySQLdb()