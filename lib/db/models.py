from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Classes/Tables --------------------------------

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    def __repr__(self):
        return f"'\n'Name: {self.name}'\n' Description: {self.description}'\n'"

class Scene(Base):
    __tablename__ = "scenes"
    id = Column(Integer(), primary_key=True)
    scene_num = Column(Integer())
    description = Column(String())
    choice_A = Column(String())
    choice_A_next_scene = Column(Integer())
    choice_B = Column(String())
    choice_B_next_scene = Column(Integer())
    wolf = Column(String())
    # previous_scene_id = Column(Integer, ForeignKey('scenes.id'))
    # previous_scene = relationship('Scene', remote_side=[id])
        
class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    hero_id = Column(Integer(), ForeignKey('characters.id'))
    antagonist_id = Column(Integer(), ForeignKey('characters.id'))
        
class Storyline(Base):
    __tablename__ = "storylines"
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer(), ForeignKey("stories.id"))
    scene_id = Column(Integer(), ForeignKey("scenes.id"))
