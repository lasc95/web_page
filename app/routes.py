from flask import render_template, Blueprint, request
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/works')
def works():
    with open('app/static/data/projects_data_works.json') as file:
        projects = json.load(file)
    page = request.args.get('page', 1, type=int)
    per_page = 6 # number of projects per page
    total = len(projects)
    projects = projects[(page - 1) * per_page: page * per_page]
    pagination = {
        'total': total,
        'page': page,
        'per_page': per_page,
        'pages': (total + per_page - 1) // per_page,  # Número total de páginas
    }
    return render_template('works.html', projects=projects, pagination=pagination)

@main.route('/contact')
def contact():
    return render_template('contact.html')
