"""Models for sme Impact app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    first_name = db.Column(db.String, unique=False) #there might be users who have the same firstname, so unique set to False
    last_name = db.Column(db.String, unique=False)
    password = db.Column(db.String)

    # enrollments = a list of enrollments per lesson

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
      
class Lesson(db.Model): #doublecheck Python convention for class capitalizion
    """A Lesson."""

    __tablename__ = 'lessons'

    lesson_id = db.Column(db.Integer, autoincrement=True, primary_key=True) #should this be string or integer?
    skilljar_lesson_id = db.Column(db.String, unique=True)
    lesson_name = db.Column(db.String) #do we need to specify null or not
    publish_date = db.Column(db.DateTime) #doublecheck caps convention on DateTime
    enrollments= db.Column(db.Integer)


    def __repr__(self):
        return f'<Lesson lesson_id={self.lesson_id} lesson_name={self.lesson_name}>'

class Sme(db.Model): #confirmed on https://www.python.org/dev/peps/pep-0008/#class-names that class names use CapWords convention
    """A SME (subject matter expert)."""

    __tablename__ = 'smes' #consider changing to lowercase to align with industry best practices/future consideration

    sme_id = db.Column(db.Integer, autoincrement=True, primary_key=True) #variable names should be lowercase
    email = db.Column(db.String,nullable =False, unique=True)
    first_name = db.Column(db.String, nullable =False, unique=False) #there might be smes who have the same firstname, so unique set to False
    last_name = db.Column(db.String, nullable =False, unique=False)
    job_title = db.Column(db.String, nullable =False, unique=False) #smes often have the same job title, like Support Engineer or DevOps Engineer

    def __repr__(self):
        return f'<sme sme_id={self.sme_id} email={self.email}>'


def connect_to_db(flask_app, db_uri='postgresql:///lessons', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the Subject Matter Expert Impact database')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
