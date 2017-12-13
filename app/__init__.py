# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
scheduler_app_bp = Blueprint("scheduler_app", __name__)

from app import login, user


