from flask import current_app as app, render_template

@app.route('/')
def index():
    print("Index route")
    return render_template('index.html')

@app.route('/usuarios')
def users():
    print("Users route")
    return render_template('users.html')

@app.route('/documentos')
def documents():
    print("Documents route")
    return render_template('documents.html')