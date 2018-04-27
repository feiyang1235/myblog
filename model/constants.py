# coding=utf-8


class Constants(object):
    DB_TYPE = "mysql"
    DB_ENGINE = "mysqldb"
    DB_USER = "root"
    DB_PASSWORD = "123456"
    DB_HOST = "127.0.0.1"
    DB_PORT = "3306"
    DB_NAME = "people"

    SYSTEM_PLUGIN = "system_plugin"

    COMMENT_RANK_ADMIN = "admin"
    COMMENT_RANK_NORMAL = "normal"
    COMMENT_TYPE_COMMENT = "comment"
    COMMENT_TYPE_REPLY = "reply"

    FLUSH_ARTICLE_ACTION_ADD = "add"
    FLUSH_ARTICLE_ACTION_UPDATE = "update"
    FLUSH_ARTICLE_ACTION_REMOVE = "remove"

    FLUSH_COMMENT_ACTION_ADD = "add"
    FLUSH_COMMENT_ACTION_UPDATE = "update"
    FLUSH_COMMENT_ACTION_REMOVE = "remove"

    ARTICLE_TYPE_DEFAULT_ID = 1
