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

scene_4 = Scenes(
   scene_num=4, 
   description="Choose your neighbor:", 
   choice_A="THE Wolf", 
   choice_A_next_scene=5, 
   choice_B="BB Wolf", 
   choice_B_next_scene=6
   )
# if Albert or Brenda go to scene (5,6)
# if Charlie go to scene (15, 16)
scene_5 = Scenes(
   scene_num=5, 
   description="You moved into your new neighborhood and build your house. Minutes later there's a knock at your door. Do you:", 
   choice_A="open door", 
   choice_A_next_scene=7, 
   choice_B="refuse", 
   choice_B_next_scene=8, 
   wolf="THE Wolf"
   )
scene_6 = Scenes(
   scene_num=6, 
   description="You moved into your new neighborhood and build your house. Minutes later there's a knock at your door. It's your neighbor BB Wolf. He introduces himself 'Hello neighbor, I'm Mr. BB Wolf. Little pig! Little pig! Let me in! Let me in!' Do you:", 
   choice_A="open door", 
   choice_A_next_scene=9, 
   choice_B="refuse", 
   choice_B_next_scene=10, 
   wolf="BB Wolf"
   )
scene_7 = Scenes(
   scene_num=7, 
   description="It's your neighbor THE Wolf. He introduces himself 'Hello neighbor, I'm Theodore Harold Edgar Wolf. So sorry to bother you but could you spare some hot tea? I seem to find myself with a cold and have run out.' You invite the wolf in for tea and end up talking. He is actually vegetarian and doesn\'t eat meat. You now have a friend for life. THE END", 
   choice_A="back to main menu", 
   wolf="THE Wolf"
   )
scene_8 = Scenes(
   scene_num=8, 
   description="It's your neighbor THE Wolf. He introduces himself 'Hello neighbor, I'm Theodore Harold Edgar Wolf. So sorry to bother you but could you spare some hot tea? I seem to find myself with a cold and AAACHOOOO!' He sneezes a great sneeze and destroys your brand new house! It scares you so you run to your sibling\'s house. But you have two. Which one will you run to?", 
   choice_A="other lazy sibling", 
   choice_A_next_scene=11, 
   choice_B="Charlie's", 
   choice_B_next_scene=15, 
   wolf="THE Wolf"
   )
scene_9 = Scenes(
   scene_num=9, 
   description="It's your neighbor BB Wolf. He introduces himself 'Hello neighbor, I'm Mr. Big Bad Wolf. And I have come for dinner. You are my dinner.' He EATS YOU! THE END", 
   choice_A="back to main menu", 
   wolf="BB Wolf"
   )
scene_10 = Scenes(
    scene_num=10, 
   description="You say 'No! No! No! Not by hairs on my chinny chin chin!' BB Wolf shows his teeth and says, 'I am Mr. Big Bad Wolf! Let me in or I'll HUFF and I'll PUFF and I'll blow your house down.' So he huffs and puffs and the blows the house down! He goes to bite you but you escape and run to your siblings house. But you have two. Which one will you run to?", 
   choice_A="other lazy sibling", 
   choice_A_next_scene=13, 
   choice_B="Charlie's", 
   choice_B_next_scene=15, 
   wolf="BB Wolf"
   )
scene_11 = Scenes(
    scene_num=11, 
    description="You get to their house and run inside. Shortly there's a knock at your door:", 
    choice_A="open door", 
    choice_A_next_scene=7, 
    choice_B="refuse", 
    choice_B_next_scene=12, 
    wolf="THE Wolf"
    )
scene_12 = Scenes(
    scene_num=12, 
    description="It's your neighbor THE Wolf. He introduces himself 'Hello neighbor, I'm Theodore Harold Edgar Wolf. So sorry to bother you but could you spare some hot tea? I seem to find myself with a cold and AAACHOOOO!' He sneezes a great sneeze and destroys your brand new house! It scares you both so much so you run to your Charlie's house.", 
    choice_A="go to Charlie's", 
    choice_A_next_scene=15, 
    wolf="THE Wolf"
    )
scene_13 = Scenes(
    scene_num=13, 
    description="You get to their house and run inside. Minutes later there's a knock at your door. It's your neighbor BB Wolf. He introduces himself 'Hello neighbor, I'm Mr. BB Wolf. Little pig! Little pig! Let me in! Let me in!' Do you:", 
    choice_A="open door", 
    choice_A_next_scene=9, 
    choice_B="refuse", 
    choice_B_next_scene=14, 
    wolf="BB Wolf"
    )
scene_14 = Scenes(
    scene_num=14, 
    description="You say 'No! No! No! Not by hairs on my chinny chin chin!' BB Wolf shows his teeth and says, 'I am the Big Bad Wolf! Let me in or I'll HUFF and I'll PUFF and I'll blow your house down.' So he huffs and puffs and the blows the house down! He goes to bite you but you escape and run to your Charlie's house.", 
    choice_A="go to Charlie's", 
    choice_A_next_scene=15, 
    wolf="BB Wolf"
    )
scene_15 = Scenes(
    scene_num=15, 
    description="At Charlie's house, there's a knock at your door:", 
    choice_A="open door", 
    choice_A_next_scene=7, 
    choice_B="refuse", 
    choice_B_next_scene=17, 
    wolf="THE Wolf"
    )
scene_16 = Scenes(
    scene_num=16, 
    description="At Charlie's house, there's a knock at your door.  It's your neighbor BB Wolf. He introduces himself 'Hello neighbor, I'm BB Wolf. Little pig! Little pig! Let me in! Let me in!' Do you:", 
    choice_A="ope door", 
    choice_A_next_scene=9, 
    choice_B="refuse", 
    choice_B_next_scene=18, 
    wolf="BB Wolf"
    )
scene_17 = Scenes(
    scene_num=17, 
    description="It's your neighbor THE Wolf. He introduces himself 'Hello neighbor, I'm Theodore Harold Edgar Wolf. So sorry to bother you but could you spare some hot tea? I seem to find myself with a cold and AAACHOOOO!' He sneezes a great sneeze. Nothing happens. You peek your head out the door and you invite the wolf in for tea and end up talking. He\'s actually vegetarin and doesn\'t eat meat. You now have a friend for life. THE END", 
    choice_A="return to main menu", 
    wolf="THE Wolf"
    )
scene_18 = Scenes(    
    scene_num=18, 
    description="You say 'No! No! No! Not by hairs on my chinny chin chin!' BB Wolf shows his teeth and says, 'I am Mr. Big Bad Wolf! Let me in or I'll HUFF and I'll PUFF and I'll blow your house down.' So he huffs and puffs and nothing happens. He keeps huffing and puffing but he can't blow the house down. Finally he'so out of breath that he can't huff and puff anymore. So he stopped to rest. He decides to climb onto the roof and finally get these pigs for good. You hear him climbing onto the roof. Do you: ", 
    choice_A="make a blazing fire in your fireplace under a big pot of water", 
    choice_A_next_scene=19, 
    choice_B="don't make a fire", 
    choice_B_next_scene=20, 
    wolf="BB Wolf"
    )
scene_19 = Scenes(
    scene_num=19, 
    description="BB Wolf comes down the chimney and plop! he falls into the boiling water. You slam the lid on. And boil the wolf up and you and your siblings have a have wolf stew for dinner. THE END", 
    choice_A="return to main menu", 
    wolf="BB Wolf"
    )
scene_20 = Scenes(
   scene_num=20,
   description="BB Wolf comes down the chimney and EATS YOU AND YOUR SIBLINGS! THE END"
    )