from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///3_little_pigs.db')
session = sessionmaker(bind=engine)()

Base = declarative_base()
# Classes/Tables should be in models.py? --------------------------------

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    def __repr__(self):
        return f"'\n'Name: {self.name}'\n' Description: {self.description}'\n'"

class Scenes(Base):
    __tablename__ = "scenes"
    id = Column(Integer, primary_key=True)
    scene_num = Column(Integer)
    description = Column(String)
    choice_A = Column(String)
    choice_A_next_scene = Column(Integer)
    choice_B = Column(String)
    choice_B_next_scene = Column(Integer)
    # def __repr__(self):
    #     return f"'\n'Scene Number: {self.scene_num}'\n' description: {self.description}'\n' Choice A: {self.choice_A}'\n' Choice B: {self.choice_B} '\n'"
        
class Story(Base):
    __tablename__ = "story"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    hero_id = Column(Integer)
    antagonist_id = Column(Integer)
    # def __repr__(self):
    #     return f"'\n'Title: {self.title}'\n' Hero: {self.hero_id}'\n' Antagonist: {self.antagonist_id}'\n'"
        
class Storyline(Base):
    __tablename__ = "storyline"
    id = Column(Integer, primary_key=True)
    story_id = Column(Integer)
    scene_id = Column(Integer)
    # def __repr__(self):
    #     return f"'\n'Employee ID: {self.id}'\n' Name: {self.name}'\n' Level: {self.level}'\n' Salary: ${self.salary} '\n'"