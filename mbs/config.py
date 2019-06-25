# -*- coding:utf-8 -*-
# Created by huangtao@oraro.net on 2019/6/25
# 项目配置文件

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 根目录
    BASEDIR = basedir
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    # 研发环境
    DB_NAME = os.environ.get('DB_NAME') or 'mbs_rest'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_USERNAME = os.environ.get('DB_USERNAME') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'Aa123456'
    # 生产环境
    PRO_DB_NAME = os.environ.get('DB_NAME') or 'mbs_rest'
    PRO_DB_HOST = os.environ.get('DB_HOST') or '192.168.8.240'
    PRO_DB_USERNAME = os.environ.get('DB_USERNAME') or 'root'
    PRO_DB_PASSWORD = os.environ.get('DB_PASSWORD') or '123456'
    # 工具类文件夹
    UTIL_FOLDER = os.path.join(basedir, 'utils')
    
    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(Config.DB_USERNAME, Config.DB_PASSWORD,
                                                                                 Config.DB_HOST, Config.DB_NAME)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        # 配置日志文件
        import logging
        import datetime
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)s[line:%(lineno)d]:%(levelname)s %(message)s',
        )
        
        # 输出到文件
        log_file = os.path.join(basedir, 'logs', datetime.datetime.now().strftime('%Y-%m-%d'), 'mbs.log')
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        
        # 输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(console_handler)


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://{0}:{1}@{2}:3306/{3}?charset=utf8'.format(Config.PRO_DB_USERNAME,
                                                                                 Config.PRO_DB_PASSWORD,
                                                                                 Config.PRO_DB_HOST, Config.PRO_DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        # 配置日志文件
        import logging
        import datetime
        
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)s[line:%(lineno)d]:%(levelname)s %(message)s',
        )
        
        # 输出到文件
        log_file = os.path.join(basedir, 'logs', datetime.datetime.now().strftime('%Y-%m-%d'), 'mbs.log')
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        
        # 输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(console_handler)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
