"""Models for SME Impact app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    fname = db.Column(db.String, unique=False) #there might be users who have the same firstname, so unique set to False
    lname = db.Column(db.String, unique=False)
    password = db.Column(db.String)

    # registrations = a list of registrations per lesson

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class lesson(db.Model): #doublecheck Python convention for class capitalizion
    """A Lesson."""

    __tablename__ = 'lessons'

    lesson_id = db.Column(db.Integer, autoincrement=True, primary_key=True) #should this be string or integer?
    skilljar_lesson_id = db.Column(db.String, unique=True)
    lesson_name = db.Column(db.String) #do we need to specify null or not
    publish_date = db.Column(db.DateTime) #doublecheck caps convention on DateTime
    registrations= db.Column(db.Integer)


    def __repr__(self):
        return f'<Lesson lesson_id={self.lesson_id} lesson_name={self.lesson_name}>'

class SME(db.Model):
    """A SME (subject matter expert)."""

    __tablename__ = 'SMEs' #consider changing to lowercase to align with industry best practices/future consideration

    SME_id = db.Column(db.Integer, autoincrement=True, primary_key=True) #variable names should be lowercase
    email = db.Column(db.String, unique=True)
    fname = db.Column(db.String, unique=False) #there might be SMEs who have the same firstname, so unique set to False
    lname = db.Column(db.String, unique=False)
    jobtitle = db.Column(db.String, unique=False) #SMEs often have the same job title, like Support Engineer or DevOps Engineer

def __repr__(self):
        return f'<SME SME_id={self.SME_id} email={self.email}>'


def connect_to_db(flask_app, db_uri='postgresql:///lessons', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the Impact database')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
