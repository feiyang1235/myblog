# -*- coding:utf-8 -*-
#!/usr/bin/env python
'''
    desc: 主服务
    author: jsongo
'''
import concurrent.futures
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tornado.web 
import tornado.ioloop
from tornado.options import define, options
import uimethod
from model.constants import Constants
# import uimoudle
from controller.indexHandler import IndexHandler
from controller.loginHandler import LoginHandler
from tornado.web import url
import MySQLdb

define("port", default=8000, help="run on the given port", type=int)
settings = {                                    #html文件归类配置，设置一个字典
    "template_path":"template",                #键为template_path固定的，值为要存放HTML的文件夹名称
    "static_path":"static",                    #键为static_path固定的，值为要存放js和css的文件夹名称
}
def db_pool_init():
    # engin_db_str = "%s+%s://%s:%s@%s:%s/%s"%(
    #      Constants.DB_TYPE
    #     ,Constants.DB_ENGINE
    #     ,Constants.DB_USER
    #     ,Constants.DB_PASSWORD
    #     ,Constants.DB_HOST
    #     ,Constants.DB_PORT
    #     ,Constants.DB_NAME)
    # # print "engin_db_str",engin_db_str
    # # engine = create_engine(engin_db_str,encoding='utf-8',echo=True,pool_pre_ping=True)
    # engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/people",encoding='utf-8',echo=False)
    # Session = sessionmaker(bind=engine)
    connection=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="people",charset="utf8")  
    cursor = connection.cursor()
    return [cursor,connection]
#  从命令行读取配置，如果这些参数不传，默认使用config.py的配置项
def parse_command_line():
    options.define("port", help="run server on a specific port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r"/", IndexHandler,name='index'),
            url(r"/login",LoginHandler,name='login'),
            # (r"/room", RoomHandler), # 用http请求的方式
            # (r"/dig", AnswerHandler),# 用http请求的方式
        ]
        settings = {
             "template_path":"template",                #键为template_path固定的，值为要存放HTML的文件夹名称
             "static_path":"static",                    #键为static_path固定的，值为要存放js和css的文件夹名称
             'ui_methods':uimethod,                    #配置html文件函数调用模块
             # 'ui_modules':uimodule,                    #配置html文件函数调用模块
        }
        self.db_cursor = db_pool_init()[0]
        self.db_conn = db_pool_init()[1]
        self.async_do = concurrent.futures.ThreadPoolExecutor(500).submit
        super(Application, self).__init__(handlers, **settings)
        # tornado.web.Application.__init__(self, handlers, **settings)
# class IndexHandler(tornado.web.RequestHandler):
#    def get(self):
#        self.write('我们既然改变不了规则，那就做到最好')
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
