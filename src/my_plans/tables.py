import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    is_active = sa.Column(sa.Boolean)
    is_admin = sa.Column(sa.Boolean)
    password_hash = sa.Column(sa.Text)


class RequestOptions(Base):
    __tablename__ = 'request_options'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    request_name = sa.Column(sa.String)


class Post(Base):
    __tablename__ = 'microblog'

    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    title = sa.Column(sa.String)
    text = sa.Column(sa.Text(350))
    date = sa.Column(sa.Date)


class BaseUser:
    pass