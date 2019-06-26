# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/25
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config

# 数据库处理
db = SQLAlchemy()
# csrf防护
csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    # 注册每个APP view对应的蓝本
    # 处理根url
    from auth import auth
    app.register_blueprint(auth, url_prefix='/user')
    return app
