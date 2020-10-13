from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_session import Session
from functools import *

from flask_security import Security,  \
    UserMixin, RoleMixin, login_required, current_user
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
from flask import Flask, session, url_for, redirect, request
from flask_mail import Mail
from uuid import uuid4
from datetime import datetime, timedelta
import redis
import _pickle
import time
import string
import json
import random


security = Security()
admin = Admin(base_template='my_master.html', template_mode='bootstrap3',)
flask_bcrypt = Bcrypt()
login_manager = LoginManager()
sess = Session()
mail = Mail()

current_milli_time = lambda: int(round(time.time() * 1000)) % 100000

def response_with_code(status, body=None):
    return json.dumps({'status':status, 'body':body})

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def get_random_numeric_value(length):
    digits = string.digits
    result_str = ''.join((random.choice(digits) for i in range(length)))
    return int(result_str)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_token = session.get('user_id')
        if session_token is None:
            return response_with_code("<fail>:2:login required")
        return f(*args, **kwargs)
    return decorated_function

def user_have_write_right(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_token = session.get('authorized')
        print(session_token)
        if session_token is None:
            return response_with_code("<fail>:4:인증 해주세요")
        if session_token == 0:
            return response_with_code("<fail>:4:인증 해주세요")
        return f(*args, **kwargs)
    return decorated_function

def is_highSchool(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_token = session.get('age')
        if session_token is None:
            return response_with_code("<fail>:2:고등학생이 아닙니다.")
        if session_token > 19:
            return response_with_code("<fail>:2:고등학생이 아닙니다.")
        return f(*args, **kwargs)
    return decorated_function

def get_cur_date():
    time_format = "%04d/%02d/%02d %02d:%02d:%02d"
    now = time.localtime()
    written_time = time_format % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return written_time

def allowed_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        json_data = request.json
        id = int(json_data['communityID']) if json_data else int(request.args.get('communityID'))
        ids = session.get('allowed_ids')
        if id not in ids:
            return response_with_code("<fail>:2:access denied")
        return f(*args, **kwargs)
    return decorated_function

def convert_to_dict(query_result):
    dict_result = dict(query_result.__dict__)
    dict_result.pop('_sa_instance_state', None)
    written_time = dict_result.pop('writtenTime', None)
    if written_time:
        dict_result['writtenTime'] = str(written_time)
    return dict_result
