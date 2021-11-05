import datetime

import sqlalchemy

from db.base import metadata

items = sqlalchemy.Table(
    'items',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String, nullable=False,),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('price', sqlalchemy.Integer,),
    sqlalchemy.Column('amount', sqlalchemy.Integer),
    sqlalchemy.Column('category_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'), nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
)
