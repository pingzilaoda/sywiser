# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from datetime import timedelta
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'app.login'


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

#session和cookie设置
app.permanent_session_lifetime = timedelta(minutes=5)
login_manager.remember_cookie_duration=timedelta(days=1)

# 开启数据库
db = SQLAlchemy(app)

#开启视图
from app import scheduler_app_bp
app.register_blueprint(scheduler_app_bp, url_prefix='/app')

#开启用户认证
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from app.user.model import User
    return User.query.get(int(user_id))

print "aaaaaaaaaaa"
print app.url_map
print app.view_functions
print "vvvvvvvvvvvv"

db.create_all()

print __name__

if __name__ == '__main__':
    app.run(debug=True)
