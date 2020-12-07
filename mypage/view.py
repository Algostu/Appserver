import json, time
import pandas as pd

from flask import escape, Blueprint, request, session, current_app as app
from sqlalchemy import text

from main.extensions import *
from main.model import *

mypage_api = Blueprint('mypage', __name__, url_prefix='/mypage')

@mypage_api.route('/surveyLink', methods=['GET'])
@login_required
def get_surveyLink():
    return response_with_code("<success>", "https://www.naver.com")

@mypage_api.route('/myWork', methods=['GET'])
@login_required
def get_myWork():
    com_type = [(ArticleAll,session['allowed_all_ids']),(ArticleSchool,session['allowed_school_ids']), (ArticleRegion,session['allowed_region_ids'])]
    numArticles = 0
    numReplies = 0
    numHearts = 0
    for com, com_ids in com_type:
        for com_id in com_ids:
             articles = com.query.filter_by(communityID=com_id, userID=session['user_id']).all()
             numArticles += len(articles)
             for article in articles:
                 numReplies += article.reply
                 numHearts += article.heart
    my_work = {"numArticles":numArticles,
    "numReplies":numReplies,
    "numHearts":numHearts}
    return response_with_code("<success>", my_work)
