import datetime
from extensions import db


class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String())
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"Event: {self.description}"
