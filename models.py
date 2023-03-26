from datetime import datetime, date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    date_time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_created = db.Column(db.Date, nullable=False, default=date.today)
