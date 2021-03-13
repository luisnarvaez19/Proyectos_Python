from flask import request, make_response
from com import app
from com.run import db
from com.web_services.models import User


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'POST':
        """return the information for <user_id>"""
        username = request.form.get('user')
        print(f'El user es: {username}')
        email = request.form.get('email')
        if username and email:
            new_user = User(
                username=username,
                email=email
            )
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
            return make_response(f"{new_user} successfully created!")


@app.route('/')
def hello_world():
    return 'Hello, World Anabel!'

