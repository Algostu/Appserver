from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
from functools import *

from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
from flask import Flask, session, url_for, redirect, request

from uuid import uuid4
from datetime import datetime, timedelta
import redis
import _pickle
import time
import string
import random



flask_bcrypt = Bcrypt()
login_manager = LoginManager()
sess = Session()

current_milli_time = lambda: int(round(time.time() * 1000)) % 100000

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
            return "login required"
        return f(*args, **kwargs)
    return decorated_function

def allowed_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ids = session.get('allowed_ids')
        json_data = request.json
        print(json_data)
        print(ids)
        if json_data['communityID'] not in ids:
            return "access denied"
        return f(*args, **kwargs)
    return decorated_function

def convert_to_dict(query_result):
    dict_result = dict(query_result.__dict__)
    dict_result.pop('_sa_instance_state', None)
    return dict_result
