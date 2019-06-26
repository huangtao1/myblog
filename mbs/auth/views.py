#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/26

from flask_restful import Resource
from .models import User

class Login(Resource):
    def get(self):
        return {'a': 'd'}


class Users(Resource):
    """
    返回所有用户信息
    """
    def get(self):
        return
