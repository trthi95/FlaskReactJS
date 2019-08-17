from flask import Flask

def create_app():
    app = Flask(__name__)

    from .database import init_db
    init_db()
    from .views import main
    app.register_blueprint(main)

    return app