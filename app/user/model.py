# !/usr/bin/python
# -*- coding: utf-8 -*-
from manage import db
from sqlalchemy import text
from flask.ext.login import UserMixin

class User(UserMixin,db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.DATETIME, nullable=False)

    @staticmethod
    def insert_user_datastore(args):
        """
        新增记录
        :param args:
        :return:
        """
        sql = "INSERT INTO user(username,password,email,created)  VALUES (:username,:password,:email,:created)"
        data = db.session.execute(text(sql),args)
        db.session.commit()
        return data

    @staticmethod
    def select_user_by_name(username):
        """
        新增记录
        :param args:
        :return:
        """
        sql = "SELECT password FROM user WHERE username=:username "
        data = db.session.execute(text(sql), {'username':username})
        db.session.commit()
        return data