from flask import current_app as app, render_template
from .models import User

@app.route('/')
def index():
    print("Index route")
    return render_template('index.html')

@app.route('/usuarios')
def users():
    print("Users route")
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/documentos')
def documents():
    print("Documents route")
    users = User.query.all()
    return render_template('documents.html', users=users)