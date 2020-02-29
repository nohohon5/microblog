"""
Flask在加载环境变量的优先级
手动设置的环境变量 > .env中设置的环境变量 > .flaskenv设置的环境变量
.env存储敏感信息的环境变量
.flaskenv存储公开环境变量
"""
# 这就是注释
FLASK_APP = "microblog.py"
FLASK_ENV = "development"
FLASK_RUN_HOST = '0.0.0.0'
FLASK_RUN_PORT = '5555'
