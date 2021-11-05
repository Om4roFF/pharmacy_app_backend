import datetime

import sqlalchemy

from db.base import metadata

category = sqlalchemy.Table(
    'categories',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('category_name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('image_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('images.id'), nullable=False,),
    sqlalchemy.Column('section_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('sections.id'), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)
