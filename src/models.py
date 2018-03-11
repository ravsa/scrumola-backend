#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import (Column, Integer, String)
#  from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound


class BayesianModelMixin(object):
    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)

        return d

    @classmethod
    def _by_attrs(cls, session, **attrs):
        try:
            return session.query(cls).filter_by(**attrs).one()
        except NoResultFound:
            raise
        except SQLAlchemyError:
            session.rollback()
            raise

    @classmethod
    def by_id(cls, session, id):
        try:
            return cls._by_attrs(session, id=id)
        except NoResultFound:
            # What to do here ?
            raise

    @classmethod
    def get_or_create(cls, session, **attrs):
        try:
            return cls._by_attrs(session, **attrs)
        except NoResultFound:
            try:
                o = cls(**attrs)
                try:
                    session.add(o)
                    session.commit()
                except SQLAlchemyError:
                    session.rollback()
                    raise
                return o
            except IntegrityError:  # object was created in the meanwhile by someone else
                return cls._by_attrs(**attrs)


Base = declarative_base(cls=BayesianModelMixin)


class UserStories(Base):
    __tablename__ = 'user_stories'

    id = Column(Integer, primary_key=True)
    author = Column(String(255), unique=True)
    assignees = Column(String(255), unique=True)
    url = Column(String(255))

    user = relationship('User')

    @classmethod
    def by_name(cls, session, name):
        try:
            return cls._by_attrs(session, name=name)
        except NoResultFound:
            # What to do here ?
            raise
