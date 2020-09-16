#-*-coding:utf-8-*-
import os, sys, json, unittest, time
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#from flaskr import create_app
from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine, text

from config import config_by_name

flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)

    # 설정 로드
    app.config.from_object(config_by_name[config_name])
    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')

    app.db = database

    # 암호화? 나도 잘은 모르겠다
    flask_bcrypt.init_app(app)

    return app




app = create_app('dev')

app.app_context().push()

#api = Api(app)
#api.add_resource(articleHandler, '/article')

manager = Manager(app)

@manager.command
def run():
	app.run()

@manager.command
def test():
	"""Runs the unit tests."""
	tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

def on_json_loading_failed_return_dict(e):
    return {}

@app.route('/article/<method>', methods=['GET', 'POST'])
def article(method):
    if method == 'read' and request.method == 'GET':
        articleID = request.args.get('articleID')
        articleType = request.args.get('articleType')
        row = app.db.execute(
        """
        select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
        from article JOIN user_info ON article.userID = user_info.userID
        where articleID = %s and communityID = %s
        """, (articleID, articleType)).fetchone()
        print(row)
        article = {}
        if row:
            article = {'articleId': row[0], 'isAnonymous': row[1], 'content':row[2], 'title':row[3],
            'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':row[7], 'nickName':row[8]}
        return json.dumps(article)

    elif method == 'write' and request.method == 'POST':
        request.on_json_loading_failed = on_json_loading_failed_return_dict
        article = request.json
        if article is None:
            return 'fail'
        now = time.localtime()
        article['time'] = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        app.db.execute(text(
        """
        INSERT INTO article (communityID, userID, isAnonymous, title, content)
        VALUES (:articleType, :userId, :isAnonymous, :title, :content)
        """), article)
        return 'success'
    elif method == 'delete' and request.method == 'GET':
        userID = request.args.get('userID')
        articleID = request.args.get('articleID')
        articleType = request.args.get('articleType')

        app.db.execute(
        """
        DELETE from article where userID=%s and articleId=%s and communityID=%s
        """, (userID,articleID,articleType))
        return 'success'
    elif method == 'articleList' and request.method == 'GET':
        articleType = request.args.get('articleType')
        articleTime = request.args.get('articleTime')
        if articleTime == 'latest':
            sql = """
            select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
            from article JOIN user_info ON article.userID = user_info.userID
            where communityID=%s
            order by writtenTime desc limit 25
            """
            rows = app.db.execute(sql, (articleType)).fetchall()
        else:
            # 동시에 쓰는건 나중에 생각하자
            sql = """
            select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
            from article JOIN user_info ON article.userID = user_info.userID
            where communityID=%s and writtenTime < %s
            order by writtenTime desc limit 25
            """
            rows = app.db.execute(sql, (articleType, articleTime)).fetchall()
        articles = [{'articleId': row[0], 'isAnonymous': row[1], 'content':row[2][:25], 'title':row[3][:20],
        'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':row[7], 'nickName':row[8]} for row in rows]
        return json.dumps(articles)
    elif method == 'hotArticleList' and request.method == 'GET':
        sql = """
        SELECT articleID, communityID, title, content, heart, reply
        FROM article WHERE heart =
        (SELECT max(heart) FROM article where communityID = %s)
        """
        hot_articles = {}
        for id, name in app.db.execute("select * from community").fetchall():
            hot_article = app.db.execute(sql, id).fetchone()
            if hot_article:
                hot_articles[name] = {"articleID" : hot_article["articleID"], "communityID" : hot_article["communityID"],
                "title" : hot_article["title"][:20], "content" : hot_article["content"][:50],
                "heart" : hot_article["heart"], "reply" : hot_article["reply"]}
    elif method == 'latestArticleList' and request.method == 'GET':
        sql = """
        SELECT articleID, communityID, title, content, heart, reply
        FROM article where communityID = %s order by writtenTime desc limit 1
        """
        latest_articles = {}
        for id, name in app.db.execute("select * from community").fetchall():
            latest_article = app.db.execute(sql, id).fetchone()
            if latest_article:
                latest_articles[name] = {"articleID" : latest_article["articleID"], "communityID" : latest_article["communityID"],
                "title" : latest_article["title"][:20], "content" : latest_article["content"][:50],
                "heart" : latest_article["heart"], "reply" : latest_article["reply"]}


        return json.dumps(latest_articles)





# @app.route('/article', methods=['GET'])
# def article_get():
#     a = app.db.execute('select * from user_info');
#     return 'success'


# 예제 코드
@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    # 로그인 했는지 확인
    if not session.get("logged_in"):
        abort(401)
    # 포맷팅 할 때 ? ? 사용
    g.db.execute('insert into entries (title, text) values (?, ?)',
        [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    manager.run()
