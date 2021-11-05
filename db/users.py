import datetime

import sqlalchemy

from db.base import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('email', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('google_id', sqlalchemy.String),
    sqlalchemy.Column('hashed_password', sqlalchemy.String),
    sqlalchemy.Column('photo_url', sqlalchemy.String),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)
