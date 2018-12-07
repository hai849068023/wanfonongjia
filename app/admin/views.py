# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 10:51'
from . import admin
from app.models import User
from flask import render_template


@admin.route('/')
def adminHome():
    return '这是后台'


@admin.route('/user')
def adminUser():
    users = User.query.all()
    return render_template('admin/users.html',users=users)
