"""CRUD operations."""

from model import db, User, Lesson, sme, connect_to_db


def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name = first_name, last_name = last_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_sme(first_name, last_name, job_title, email):
    """Create and return a new subject matter expert (sme)."""

    sme = sme(first_name=first_name,
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
