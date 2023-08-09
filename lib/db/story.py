from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from functions import random_job
from rich.console import Console
from ipdb import set_trace
from rich import print
import sys
import os

engine = create_engine("sqlite:///little_pigs.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
console = Console()

# Main Menu -------------------------------------

# Classes/Tables --------------------------------

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
    name = Column(String)
    level = Column(Integer)
    salary = Column(Integer)
    def __repr__(self):
        return f"'\n'Employee ID: {self.id}'\n' Name: {self.name}'\n' Level: {self.level}'\n' Salary: ${self.salary} '\n'"
        id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    salary = Column(Integer)
    def __repr__(self):
        return f"'\n'Employee ID: {self.id}'\n' Name: {self.name}'\n' Level: {self.level}'\n' Salary: ${self.salary} '\n'"
    