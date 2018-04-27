# coding=utf-8
from model.models import Login

class UserService(object):
    @staticmethod
    def get_user_list(db_cursor):
        return db_cursor.query(Login).all()
    @staticmethod
    def get_user(db_cursor, username):
        db_cursor.execute("select * from login where username = '%s'"%(username))
        result = db_cursor.fetchone()
        return result
    @staticmethod
    def save_user(db_cursor,db_conn,user_dict):
        try:
            c = db_cursor.execute("insert into login (login.email,login.username,login.password)values('%s','%s','%s')"%(user_dict['email'],user_dict['username'],user_dict['password']))
        except Exception:
            pass
        # db_cursor.close()
        # db_conn.close()
        # add_user = Login(email = user_dict['email']
        #                 ,username = user_dict['username'])
        # db_cursor.add(add_user)
        # db_cursor.commit()
        # return add_user


    
