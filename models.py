from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from app import db
from flask_security import UserMixin, RoleMixin


class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=140))
    created = Column(DateTime, default=datetime.utcnow())
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'Book id: {self.id}, title: {self.title}>'


class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    date_of_birth = Column(DateTime)
    books = relationship("Book", back_populates="author")

    def __init__(self, *args, **kwargs):
        super(Author, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'Author id: {self.id}, name: {self.name}>'


roles_users = db.Table(
    'roles_users',
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id')),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    active = Column(Boolean)
    roles = relationship('Role', secondary=roles_users, back_populates='users')


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(255))
    users = relationship('User', secondary=roles_users, back_populates='roles')


db.create_all()
