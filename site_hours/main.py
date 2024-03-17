from collections import namedtuple

from database import engine, User
from sqlalchemy.orm import Session
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = None


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    name_of_user = messages[7:].replace("(", "").replace(")", "").replace("text=", "").replace("tag=", ""). \
        replace(",", "").replace("'", "").split()[0]
    second_name_of_user = messages[7:].replace("(", "").replace(")", "").replace("text=", "").replace("tag=", ""). \
        replace(",", "").replace("'", "").split()[1]

    with Session(bind=engine) as session:
        user = User(name=name_of_user, fullname=second_name_of_user)
        session.add(user)
        session.commit()

        # user = session.query(User).filter_by(id=2).first()

    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    global messages
    text = request.form['text']
    tag = request.form['tag']

    messages = str(Message(text, tag))
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
