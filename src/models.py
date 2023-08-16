import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20))
    lenght = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    diameter = Column(Integer)
    rotation = Column(Integer)
    terrain = Column(String(20))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship(Starships)

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), unique=True)
    starships = relationship(Starships)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), unique=True)
    planets = relationship(Planets)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), unique=True)
    characters = relationship(Characters)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), index=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True)
    favorite_character = Column(Integer, ForeignKey('favorite_characters.id'))
    characters = relationship(Characters)
    favorite_planet = Column(Integer, ForeignKey('favorite_planets.id'))
    planets = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
