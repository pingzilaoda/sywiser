# !/usr/bin/python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash

from app.until.format import str_now,format_result
from app.user.model import User


class UserSever():

    @staticmethod
    def creatUser(args):
        args['password'] = generate_password_hash(args['password'])
        args['created'] = str_now()
        result = User.insert_user_datastore(args)
        return result

    @staticmethod
    def loginUser(args):
        username = args['username']
        password = args['password']
        password_hash = User.select_user_by_name(username)
        password_dict = format_result(password_hash)
        if password_dict:
             login_flag = check_password_hash(password_dict[0]['password'], password)
             if login_flag:
                 from flask_login import login_user
                 login_user(User.query.get(int(password_dict[0]['id'])))
                 return 'success'
             else:
                 return 'password is error'
        else:
            return 'user does not exist'
