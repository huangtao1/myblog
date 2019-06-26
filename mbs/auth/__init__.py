#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by mark.huang on 2019/6/26
from flask import Blueprint

auth = Blueprint('auth', __name__)
from .urls import *
