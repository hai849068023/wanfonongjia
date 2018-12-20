# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/11 8:56'
from flask import Blueprint

smallapp = Blueprint('smallapp', __name__, template_folder='templates')

from . import views