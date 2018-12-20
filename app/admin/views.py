# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 10:51'
from flask import render_template, request, redirect, url_for

from app.models import User
from app.models import db
from . import admin
from .forms import AdminLogin, AdminRegister

model_key = 'wangfonongjia'


@admin.route('/register', methods=['GET', 'POST'])
def adminRegister():
    form = AdminRegister(request.form)
    user = User()
    if request.method == 'POST':
        wxname = request.form.get('wxname')
        password = request.form.get('password')
        is_existing = User.query.filter_by(wxname=wxname).first()
        if is_existing:
            return render_template('admin/admin_login.html', msg='用户名已存在，请更换或者直接登录！', form=form)
        hash_password = user.set_password(password + model_key)
        addmessage = User(wxname=wxname, hash_password=hash_password)
        db.session.add(addmessage)
        db.session.commit()
        return redirect(url_for('admin.adminLogin'))
    return render_template('admin/admin_register.html', form=form)


@admin.route('/login', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLogin(request.form)
    user = User()
    if request.method == 'POST':
        wxname = request.form.get('wxname')
        password = request.form.get('password')
        user = User.query.filter_by(wxname=wxname).first()
        if user and user.check_password(password + model_key):
            return redirect(url_for('admin.adminHome'))
        return render_template('admin/admin_login.html', data='账号密码错误！', form=form)
    return render_template('admin/admin_login.html', form=form)


@admin.route('/index')
def adminIndex():
    return render_template('admin/admin_index.html')


@admin.route('/indexv')
def adminIndexv():
    return render_template('admin/admin_indexv.html')


@admin.route('/user')
def adminUser():
    users = User.query.all()
    return render_template('admin/admin_users.html', users=users)
