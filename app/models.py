from app import db

class Tag(db.Model):
    __table__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64), unique=True)
    posts = db.relationship('Post', backref='tag')

class Post(db.Model):
    __table__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, index=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    def __repr__(self):
        return '<Post %r>' % self.title