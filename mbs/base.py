#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by huangtao@oraro.net on 2019/6/25
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 注册每个APP view对应的蓝本
    # 处理根url
    return app
