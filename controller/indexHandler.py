# -*- coding:utf-8 -*-
#!/usr/bin/env python
from tornado.web import RequestHandler
from tornado import gen
class IndexHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        name = self.get_argument('name', 'people')
        self.render('index.html',name= name)