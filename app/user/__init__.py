# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import (Api)
from app import scheduler_app_bp
from app.user.view import CreatedUser,UserLogin,UserShow

user_app = Api(scheduler_app_bp)


user_app.add_resource(CreatedUser, '/user/creat')

user_app.add_resource(UserLogin, '/user/login')

user_app.add_resource(UserShow, '/user/show')