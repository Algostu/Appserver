#-*-coding:utf-8-*-
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing

app = Flask(__name__)

# FLASKR_SETTINGS 라는 파일로 부터 대문자 변수 값을 읽어온다.
app.config.from_object('FLASKR_SETTINGS')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# DB 초기화 하는 코드
# 파이썬 쉘에서 직접 실행 해 줘야 한다.
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

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
    app.run(host='0.0.0.0')
