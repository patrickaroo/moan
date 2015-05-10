#!/usr/bin/env python

from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey, MetaData, BigInteger, PickleType, Boolean, Text
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

import datetime

import socket
hostname = socket.gethostname()

# Standard database connection infrastructure
Base = declarative_base()

# Using SQLite for now to cut down on daemon overhead, Echo not necessary but I like to look at it
db = create_engine('sqlite:///moan.db', echo=False)

# Open the session
metadata = MetaData(db)
Session = sessionmaker(bind=db)
session = Session()


### Tables!
class Moan(Base):
    __tablename__ = 'moans'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    user = Column(Integer)
    time = Column(DateTime)

    def __repr__(self):
        return str(self.__dict__)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

if __name__ == "__main__":
    Base.metadata.create_all(db)


