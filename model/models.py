# coding=utf-8
from sqlalchemy.orm import contains_eager, deferred
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, Text, ForeignKey, BigInteger, DATE
from sqlalchemy.orm import relationship, backref
from datetime import datetime

DbBase = declarative_base()

class DbInit(object):
    create_time = Column(DateTime,default = datetime.now)

class Login(DbBase,DbInit):
    __tablename__='login'
    id = Column(Integer,primary_key=True)
    email = Column(String(64),default = None,unique=True)
    username = Column(String(64), unique=True, index=True)
    nickname = Column(String(64),default = "customer")
    password = Column(String(128),default = "123456")
    # 验证当前对象的密码是否正确
    def verify_password(self, password):
        return self.password == password

class A(object):
    def __init__(self):
        pass

