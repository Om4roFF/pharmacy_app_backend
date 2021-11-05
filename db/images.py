import datetime

import sqlalchemy

from db.base import metadata

images = sqlalchemy.Table(
    'images',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('image_url', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)
