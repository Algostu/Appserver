import json, time
from datetime import datetime
from flask import jsonify, make_response, escape, Blueprint, request, session, current_app as app
from sqlalchemy import text, desc
from main.extensions import *
from main.model import *

article_api = Blueprint('article', __name__, url_prefix='/article')

com_type = [ArticleAll, ArticleRegion, ArticleSchool]
allowed_ids = ['allowed_all_ids', 'allowed_region_ids', 'allowed_school_ids']

time_format = "%04d/%02d/%02d %02d:%02d:%02d"

@article_api.route('/read', methods=['GET'])
@login_required
@allowed_access
def get_read_article():
    communityType = int(request.args.get('communityType'))
    articleID = int(request.args.get('articleID'))
    communityID = int(request.args.get('communityID'))
    article = com_type[communityType]
    # query db and change to dict
    query_result = article.query.filter_by(articleID=articleID, communityID=communityID).first()
    if not query_result:
        return response_with_code("<fail>:2:no article")
    target_article = convert_to_dict(query_result)
    writer = target_article.pop('userID')
    target_article['edit'] = 1 if writer == session['user_id'] else 0
    #  increase view number
    query_result.viewNumber += 1
    db.session.commit()
    return response_with_code("<success>", target_article)

# For future use
# request.on_json_loading_failed = on_json_loading_failed_return_dict
# def on_json_loading_failed_return_dict(e):
#     return {}

@article_api.route('/write', methods=['POST'])
@login_required
@allowed_access
@user_have_write_right
def post_write_article():
    written_info = request.json
    if written_info is None:
        return response_with_code("<fail>:2:no post data")
    # get time and nickName info
    now = time.localtime()
    written_time = time_format % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    nickname = '익명' if written_info['isAnonymous'] else session['nick_name']
    # generate articleID
    article_id = (written_info['communityID'] % 100) * 10000000 + get_random_numeric_value(2) * 100000 + current_milli_time()
    # create article instante
    article = com_type[written_info['communityType']]
    new_article = article(communityID=written_info['communityID'],
    userID=session['user_id'],
    nickName=nickname,
    title=written_info['title'],
    content=written_info['content'],
    writtenTime=written_time, heart = 0, viewNumber = 0, reply = 0)
    # add school and region id
    if written_info['communityType'] == 1:
        new_article.regionID = session['region_id']
    elif written_info['communityType'] == 2:
        new_article.schoolID = session['school_id']
    db.session.add(new_article)
    db.session.commit()
    return response_with_code("<success>")


@article_api.route('/delete', methods=['GET'])
@login_required
@allowed_access
@user_have_write_right
def get_delete_article():
    communityType = int(request.args.get('communityType'))
    articleID = int(request.args.get('articleID'))
    communityID = int(request.args.get('communityID'))
    article = com_type[communityType]
    # query db and check if user wrote it
    query_result = article.query.filter_by(articleID=articleID, communityID=communityID).first()
    if not query_result:
        return response_with_code("<fail>:2:no article")
    if query_result.userID != session['user_id']:
        return response_with_code("<fail>:2:no right to delete")
    #  delete target article
    db.session.delete(query_result)
    db.session.commit()
    return response_with_code("<success>")


@article_api.route('/articleList', methods=['GET'])
@login_required
@allowed_access
def get_article_list():
    communityType = int(request.args.get('communityType'))
    communityID = int(request.args.get('communityID'))
    writtenAfter = request.args.get('writtenAfter')
    article = com_type[communityType]

    if writtenAfter == 'latest':
        rows = article.query.filter_by(communityID=communityID).order_by(desc(article.writtenTime)).limit(15).all()
    else:
        rows = article.query.filter(article.writtenTime<writtenAfter, article.communityID==communityID).\
        order_by(desc(article.writtenTime)).limit(15).all()
    articles = []
    for row in rows:
        dict_row = convert_to_dict(row)
        dict_row.pop('userID')
        articles.append(dict_row)
    return response_with_code("<success>", articles)

@article_api.route('/hotArticleList', methods=['GET'])
@login_required
def get_hot_article_list():
    articles = []
    for id in range(3):
        community = com_type[id]
        for communityID in session[allowed_ids[id]]:
            # load heart and calculate max heart value
            hearts = db.session.query(community.heart).filter_by(communityID=communityID).all()
            if len(hearts) == 0:
                continue
            max_hearts = max([heart[0] for heart in hearts])
            hot_article = community.query.filter_by(heart=max_hearts).first()
            if hot_article:
                hot_article = convert_to_dict(hot_article)
                hot_article.pop('userID')
                articles.append(hot_article)
    return response_with_code("<success>", articles)

@article_api.route('/latestArticleList', methods=['GET'])
@login_required
def get_latest_article_list():
    articles = []
    for id in range(3):
        community = com_type[id]
        for communityID in session[allowed_ids[id]]:
            article = community.query.order_by(desc(community.writtenTime)).filter_by(communityID=communityID).first()
            if article:
                article = convert_to_dict(article)
                article.pop('userID')
                articles.append(article)
    return response_with_code("<success>", articles)
