from ipdb import set_trace
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from rich.console import Console
from models import Characters, Scenes, Story, Storyline
from helpers import *

engine = create_engine("sqlite:///3_little_pigs.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
console = Console()

# Main Menu -------------------------------------
# add ascii of 3 little pigs
if __name__ == "__main__":
  
  while True:
    print_slowly("3 Little Pigs - choose your own adventure")
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

# Characters------------------------------------

Albert = Characters(name="Albert", description="Pig, straw house")
Brenda = Characters(name="Brenda", description= "Pig, twig house")
Charlie = Characters(name="Charlie", description= "Pig, brick house")
THE_Wolf = Characters(name="THE Wolf", description="Theodore Harold Edgar Wolf")
BB_Wolf = Characters(name="BB Wolf", description="Big Bad Wolf")

# Scenes ---------------------------------------

1 = Scenes(scene_num=4, description="")