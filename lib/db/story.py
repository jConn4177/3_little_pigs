from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from functions import random_job
from rich.console import Console
from ipdb import set_trace
from rich import print
import sys
import os

engine = create_engine("sqlite:///3_little_pigs.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
console = Console()

# Main Menu -------------------------------------
# add ascii of 3 little pigs
if __name__ == "__main__":
  while True:
    print("3 Little Pigs - choose your own adventure")
    print("Way back in Once upon a time time, there were three little pigs all siblings. The first little big, Albert, was VERY lazy. He didn't want to work very hard so he wants to build his house out of straw.")
    print("The second little pig, Brenda, worked a little bit harder but was still a little lazy so she wants to build her house out of twigs.")
    print("The third little pig, Charlie, worked very hard and so he wants to build his house out of bricks.")
    print("First you get to pick which pig you'd like to be:")
    
    # add ascii of 3 little pigs console.print(""" """)
    print("""
          Pigs:
          A = Albert, a straw house
          B = Brenda, a twig house
          C = Charlie, a brick house
          """)
    choice = input('>>> ')
    if choice == "A":
       clear()
       #go to scene 4 to pick neighbor
    if choice == "B":
       clear()
       #go to scene 4 to pick neighbor
    if choice == "C":
       clear()
       #go to scene 4 to pick neighbor
    else:
       clear()
       print("Please enter a valid option.")

#------------------------------------------------


# Scenes ----------------------------------------

#------------------------------------------------

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
    choice_B = Column(String)
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
    