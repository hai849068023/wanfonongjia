# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 8:59'
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] ='wangfonongjia'

from .admin import admin as admin_blueprint
from .smallapp import smallapp as smallapp_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(smallapp_blueprint, url_prefix='/smallprint')