import json, time
import pandas as pd
import locale
import functools

from flask import escape, Blueprint, request, session, current_app as app
from sqlalchemy import text

from main.extensions import *
from main.model import *

search_api = Blueprint('search', __name__, url_prefix='/search')

@search_api.route('/schoolList', methods=['GET'])
def get_schoolList():
    # this is server-side query.
    # trim 고,등,학,교 off
    search_text = escape(request.args.get('schoolName')).strip('고등학교')
    if not search_text or search_text == "":
        return response_with_code("<fail>:2:invalid search text")
    schoolList = SchoolInfo.query.filter(SchoolInfo.schoolName.like('%'+search_text+'%'))
    df = pd.read_sql(schoolList.statement, schoolList.session.bind)
    return response_with_code("<success>", json.loads(df.to_json(orient='records', force_ascii=False)))

@search_api.route('/univList', methods=['GET'])
def get_univList():
    org_search_text = escape(request.args.get('univName'))
    search_text = org_search_text.strip('대학교')
    print(search_text)
    if not search_text or search_text == "":
        return response_with_code("<fail>:2:invalid search text")
    schoolList = UnivInfo.query.filter(UnivInfo.univName.like('%'+search_text+'%'))
    df = pd.read_sql(schoolList.statement, schoolList.session.bind)
    df_dict = df.to_dict('records')
    contain_df_dict = []
    not_contain_df_dict = []
    for row in df_dict:
        if org_search_text in row['univName']:
            contain_df_dict.append(row)
        else:
            not_contain_df_dict.append(row)
    return response_with_code("<success>", contain_df_dict + not_contain_df_dict)

@search_api.route('/majorList', methods=['GET'])
def get_majorList():
    search_text = escape(request.args.get('majorName')).strip('학과')
    if not search_text or search_text == "":
        return response_with_code("<fail>:2:invalid search text")
    majorList = MajorInfo.query.filter(MajorInfo.mClass.like('%'+search_text+'%'))
    df = pd.read_sql(majorList.statement, majorList.session.bind)
    df_dict = df.to_dict('records')
    contain_df_dict = []
    not_contain_df_dict = []
    for row in df_dict:
        if org_search_text in row['univName']:
            contain_df_dict.append(row)
        else:
            not_contain_df_dict.append(row)
    return response_with_code("<success>", contain_df_dict + not_contain_df_dict)
