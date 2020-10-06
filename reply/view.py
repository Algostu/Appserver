import json, time
from flask import Blueprint, request, current_app as app
from sqlalchemy import text

from main.model import *

reply_api = Blueprint('reply', __name__, url_prefix='/reply')

@reply_api.route('/read', methods=['GET'])
def get_read_article():
    articleID = request.args.get('articleID')
    row = app.db.execute(
    """
    select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
    from article JOIN user_info ON article.userID = user_info.userID
    where articleID = %s and communityID = %s
    """, (articleID, articleType)).fetchone()
    article = {}
    if row:
        if row[1]:
            nickName = 'Anonymous'
        else:
            nickName = row[8]

        article = {'articleID': row[0], 'content':row[2], 'title':row[3],
        'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':str(row[7]), 'nickName':nickName}
    return json.dumps(article)

@reply_api.route('/write', methods=['POST'])
def post_write_article():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    article = request.json
    if type(article) == type(''):
        article = json.loads(article)

    if article is None:
        return 'fail'

    now = time.localtime()
    article['time'] = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    result = app.db.execute(text(
    """
    INSERT INTO article (communityID, userID, isAnonymous, title, content, writtenTime)
    VALUES (:articleType, :userId, :isAnonymous, :title, :content, :time)
    """), article)
    return 'success:' + str(result.lastrowid)
