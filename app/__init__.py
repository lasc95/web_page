from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    return app
