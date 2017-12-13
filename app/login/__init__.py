# !/usr/bin/python
# -*- coding: utf-8 -*-
from app import scheduler_app_bp
from flask import render_template,redirect
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])


@scheduler_app_bp.route('/login')
def login():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user.html', form=form)



@scheduler_app_bp.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('aaa.html')