from flask import render_template, Blueprint, request
import json
import os

main = Blueprint('main', __name__)

def load_posts():
    with open(os.path.join('app', 'static', 'data', 'posts.json')) as file:
        return json.load(file)

def load_post_content(filename):
    filepath = os.path.join('app', 'static', 'data', 'posts', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return file.read()
    return None

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = load_posts()
    per_page = 5
    total = len(posts)
    paginated_posts = posts[(page - 1) * per_page: page * per_page]
    pagination = {
        'total': total,
        'page': page,
        'per_page': per_page,
        'pages': (total + per_page - 1) // per_page,
    }
    return render_template('blog.html', posts=paginated_posts, pagination=pagination)

@main.route('/post/<int:post_id>')
def post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return render_template('404.html'), 404
    content = load_post_content(post['file'])
    if content is None:
        return render_template('404.html'), 404
    return render_template('post.html', title=post['title'], content=content, post=post)

@main.route('/works')
def works():
    with open(os.path.join('app', 'static', 'data', 'projects_data_works.json')) as file:
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
