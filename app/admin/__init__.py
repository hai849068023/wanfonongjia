# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 10:50'
from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

from . import views

