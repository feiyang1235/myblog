# -*- coding:utf-8 -*-
#!/usr/bin/env python
import tornado.web 
from tornado import gen
from model.models import Login
from data_service.user_service import UserService
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import MySQLdb
import MySQLdb
# def db_pool_init():
#     engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/people",encoding='utf-8',echo=False)
#     Session = sessionmaker(bind=engine)
#     return Session()
class LoginHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        next_url = self.get_argument("next_url",'/')
        # result = yield self.application.async_do(UserService.save_user,self.application.db_cursor,self.application.db_conn,dict(email='haha@163.com',username='admin163',password='163163'))
        # print result
        # cursor.close()   
        # connection.close()
        # result = yield self.application.async_do(UserService.get_user, self.application.db_pool,"username_wfs")
        self.render('login.html',next_url = next_url)
    @gen.coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        next_url = self.get_argument('next', '/')
        user = yield self.application.async_do(UserService.get_user, self.application.db_cursor,username)
        # print type(user)
        # print user
        if user != None and user[4] == password:
            # self.save_login_user(user)
            # self.add_message('success', u'登陆成功！欢迎回来，{0}!'.format(username))
            self.redirect(next_url+"?name="+username)
        else:
            print "登录失败"
            self.get()
            # self.add_message('danger', u'登陆失败！用户名或密码错误，请重新登陆。')
            # self.get()