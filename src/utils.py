#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

logger = logging.getLogger(__name__)

# Create Postgres Connection Session


class Postgres:
    def __init__(self):
        self.connection = 'postgresql://{user}:{password}@{host}:{port}' \
                          '/{database}?sslmode=disable'. \
            format(user=os.getenv('POSTGRESQL_USER'),
                   password=os.getenv('POSTGRESQL_PASSWORD'),
                   host=os.getenv('POSTGRESQL_HOST'),
                   port=os.getenv('POSTGRESQL_PORT', '5432'),
                   database=os.getenv('POSTGRESQL_DATABASE'))
        engine = create_engine(self.connection)

        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def session(self):
        return self.session
