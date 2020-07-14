from datetime import datetime

from line_app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Integer, nullable=False)
    line_user_id = db.Column(db.String(255), index=True, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, status, line_user_id):
        self.status = status
        self.line_user_id = line_user_id

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'line_user_id': self.line_user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }