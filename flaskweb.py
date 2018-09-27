import os
from app.models import Post, Tag
from flask_migrate import Migrate
from app import db, create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Post=Post, Tag=Tag)