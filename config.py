# !/usr/bin/python
# -*- coding: utf-8 -*-

print __name__


class DevelopmentConfig():

    SQLALCHEMY_DATABASE_URI = 'mysql://root:Lxp123456@127.0.0.1:3306/sywiser?charset=utf8'

    SQLALCHEMY_ECHO = True
