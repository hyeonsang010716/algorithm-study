from models import db


class algo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.Text, nullable=False)