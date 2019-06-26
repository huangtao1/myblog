# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/26
from flask_sqlalchemy import Model
from base import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    create_date = db.Column(db.DateTime, default=datetime.now())
    
    @property
    def password(self):
        # password不可读
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
