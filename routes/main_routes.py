from datetime import datetime

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from extension import db
from model import Message


main = Blueprint('main', __name__)


@main.route('/')
def index():
    items = [
        {'name': 'apple', 'featured': True},
        {'name': 'banana', 'featured': False},
        {'name': 'orange', 'featured': False},
    ]
    return render_template(
        'index.html',
        items=items,
        server_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )


@main.route('/users')
def users():
    users_list = ['Alice', 'Bob', 'Charlie', 'Dana']
    return render_template('users.html', users=users_list)


@main.route('/greet')
@main.route('/greet/<name>')
def greet(name=None):
    name = name or request.args.get('name', 'friend')
    return render_template(
        'greet.html',
        name=name,
    )


@main.route('/greet-plain/<name>')
def greet_plain(name):
    return f'Hello, {name}!'


@main.route("/ken/<name>")
def ken(name = 'default') : 
    return f'halo {name}'

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['user_name']
        message = request.form['user_message']

        new_message = Message(name=name, message=message)
        db.session.add(new_message)
        db.session.commit()
        flash(f'Thank you, {name}! Your message has been saved to the database.')
        return redirect(url_for('main.contact'))

    return render_template('contact.html')


@main.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        text = request.form.get('text', '')
        current_app.logger.info('You posted: %s', text)
        flash(f'You posted: {text}')
        return redirect(url_for('main.echo'))

    return render_template(
        'echo.html',
        server_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )

