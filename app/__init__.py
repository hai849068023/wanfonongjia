# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 8:59'
from flask import Flask

app = Flask(__name__)

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')