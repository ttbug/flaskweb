from flask import render_template
from app.models import Post
from . import home

@home.route('/')
def index():
    return render_template('/home/home.html')