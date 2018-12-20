# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2018/12/7 9:01'
from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/wanfonongjia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 用户记录表
class User(db.Model):
    __tablename__ = 'wfnj_user'  # 表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 表的主键
    wxname = db.Column(db.String(50), nullable=False)  # 微信昵称
    username = db.Column(db.String(50), nullable=False)  # 登录用户名
    hash_password = db.Column(db.String(200))  # 登录密码
    truename = db.Column(db.String(50))  # 真实姓名
    tel = db.Column(db.String(11), unique=True)  # 电话号码
    portrait = db.Column(db.String(200))  # 微信头像
    datatime = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间
    userlogs = db.relationship('Userlog', backref='User')  # 会员日志外键关系

    def set_password(self, rwdpwd):
        hash_password = generate_password_hash(rwdpwd)
        return hash_password

    def check_password(self, rwdpwd):
        return check_password_hash(self.hash_password, rwdpwd)

    def __repr__(self):
        return '<User %r>' % self.wxname


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "wfnj_userlog"  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    # 定义外键 db.ForeignKey
    user_id = db.Column(db.Integer, db.ForeignKey('wfnj_user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 登录时间 ，默认时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 商品表
class Product(db.Model):
    __tablename__ = 'wfnj_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 表的主键
    product_id = db.Column(db.Integer, unique=True, autoincrement=True)  # 表的主键
    pic_path = db.Column(db.String(200), nullable=False)  # 商品图片
    name = db.Column(db.String(50), nullable=False)  # 商品名称
    price = db.Column(db.Float, nullable=False)  # 商品价格
