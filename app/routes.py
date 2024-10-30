from flask import current_app as app, render_template

@app.route('/')
def index():
    print("Index route")
    return render_template('index.html')