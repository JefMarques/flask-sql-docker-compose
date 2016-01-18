# -*- coding: utf-8 -*-
from flask.ext.bcrypt import check_password_hash, generate_password_hash
from sqlalchemy import types, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(types.Integer, primary_key=True)
    username = Column(types.String(50), unique=True, nullable=False)
    password = Column(types.String(255), nullable=False)
    email = Column(types.String(50), unique=True, nullable=True)
    is_active = Column(types.Boolean, nullable=False, default=True)
    is_admin = Column(types.Boolean, nullable=False, default=False)

    def __init__(self, username, password, email=None):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_admin(self):
        return self.is_admin

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, new_password):
        self.password = self.hash_password(new_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
