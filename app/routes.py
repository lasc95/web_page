from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/works')
def works():
    return render_template('works.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
