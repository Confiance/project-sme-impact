"""CRUD operations."""

from model import db, User, Lesson, Sme, connect_to_db


def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name = first_name, last_name = last_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_sme(first_name, last_name, job_title, email):
    """Create and return a new subject matter expert (sme)."""

    sme = Sme(first_name=first_name,
                  last_name=last_name,
                  job_title=job_title,
                  email=email)

    db.session.add(sme)
    db.session.commit()

    return sme

def create_lesson(lesson_name, publish_date, enrollments):
    """Create and return a new lesson."""
    #creating an object of type Lesson and storing into variable lesson
    lesson = Lesson(lesson_name=lesson_name,
                    publish_date=publish_date,
                    enrollments=enrollments)
    
    db.session.add(lesson)
    db.session.commit()

    return lesson

def get_lessons():
    """Return all lessons."""

    return Lesson.query.all()

def get_SMEs():
    """Return all SMEs."""

    return Sme.query.all()

def get_sme_by_email(email):
    """Return a SME by email."""

    return Sme.query.filter(Sme.email == email).first()

def get_sme_by_id(id):
    """Return a SME by id."""

    return Sme.query.get(id)

def get_lesson_by_id(lesson_id):
    """Return a lesson by primary key."""

    return Lesson.query.get(lesson_id)
