from flask import Flask,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
import sqlite3
from flask import g

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

db_name='test.db'
class say(FlaskForm):
    word = StringField('what do you wang say?',validators=[Required()])
def a():
    form = say()
    word=form.word
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
                word            TEXT   NOT NULL''')

    cursor = c.execute('INSERT INTO COMPANY(WORD)VALUES(?)')
    conn.commit()
    cursor = c.execute("SELECT  NAME,WORD from COMPANY")
    for i in cursor:
        print(WORD="")
    conn.close()


@app.route('/',methods = ['GET','POST'])
def index():
    form=say()
    word=None
    if form.validate_on_submit():
        a()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()