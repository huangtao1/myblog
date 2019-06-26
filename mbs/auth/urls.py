# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/26
from flask_restful import Api
from . import auth
from .views import Login

# 将auth模块蓝图加入Api进行管理
api = Api(auth)
api.add_resource(Login, '/login')
