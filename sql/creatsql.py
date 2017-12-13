from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.DATETIME, nullable=False)

class UserRoleRef(db.Model):

    __tablename__ = 'user_role_ref'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(80), unique=True, nullable=False)
    roleid = db.Column(db.String(120), nullable=False)

class Role(db.Model):

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(80), unique=True, nullable=False)


class RoleFunRef(db.Model):

    __tablename__ = 'role_fun_ref'
    id = db.Column(db.Integer, primary_key=True)
    roleid = db.Column(db.String(80), nullable=False)
    funid = db.Column(db.String(120), nullable=False)

class Function(db.Model):

    __tablename__ = 'function'
    id = db.Column(db.Integer, primary_key=True)
    funname = db.Column(db.String(80), unique=True, nullable=False)


db.create_all()


if __name__ == '__main__':
    app.run()