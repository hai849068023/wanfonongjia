# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/18 16:21'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User


class AdminRegister(FlaskForm):
    wxname = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    submit = SubmitField('注册')

    # 自定义用户名验证器
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册请选用其他名称！')


class AdminLogin(FlaskForm):
    wxname = StringField(
        '用户名',
        validators=[DataRequired('请输入账号！')],
        description='账号',
        render_kw={'class':"form-control", 'placeholder':"用户名"})
    password = PasswordField(
        '密码',
        validators=[DataRequired('请输入密码！')],
        description='账号',
        render_kw={'class': "form-control", 'placeholder': "用户名"})
    submit = SubmitField('登录',render_kw={'class':'btn btn-primary block full-width m-b'})
