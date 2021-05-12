"""Server for SME Impact app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/lessons')
def all_lessons():
    """View all lessons."""

    lessons = crud.get_lessons()
    print(lessons)
    return render_template('all_lessons.html', lessons=lessons)

@app.route('/lessons/<lesson_id>')
def show_lesson(lesson_id):
    """Show details on a particular lesson."""

    lesson = crud.get_lesson_by_id(lesson_id)

    return render_template('lesson_details.html', lesson=lesson)

@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(first_name, last_name, email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/login/, methods=["POST"]')
def process_login():
    """"Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route('/smes')
def all_smes():
    """View all SMEs."""

    smes = crud.get_SMEs()

    return render_template('all_smes.html', smes=smes)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

