# !/usr/bin/python
# -*- coding: utf-8 -*-
import traceback

from flask import current_app
from flask_restful import (Resource, reqparse)
from flask_login import login_required
from app.user.service import UserSever

# 参数解析对象生成
parser = reqparse.RequestParser()


class CreatedUser(Resource):

    @staticmethod
    def post():
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        parser.add_argument("email", required=True)
        try:
            ags = parser.parse_args()
            result = UserSever.creatUser(ags)
            return "success"
        except Exception as e:
            current_app.logger.error(e.message)
            current_app.logger.error(traceback.format_exc())
            return "fail"


class UserLogin(Resource):

    @staticmethod
    def post():
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        try:
            ags = parser.parse_args()
            result = UserSever.loginUser(ags)
            return result
        except Exception as e:
            current_app.logger.error(e.message)
            current_app.logger.error(traceback.format_exc())
            return "fail"


class UserShow(Resource):

    @login_required
    @staticmethod
    def post():
        parser.add_argument("page_id", required=True)
        try:
            return 'success'
        except Exception as e:
            current_app.logger.error(e.message)
            current_app.logger.error(traceback.format_exc())
            return "fail"
