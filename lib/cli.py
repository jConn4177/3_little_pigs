from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Scene, Story, Storyline
from helpers import *
import os

engine = create_engine('sqlite:///db/3_little_pigs.db')
session = sessionmaker(bind=engine)()

CURRENT_STORY = None
CURRENT_SCENE = None

def display_welcome():
     print_slowly("3 Little Pigs - choose your own adventure")

def display_main_menu():

        print_slowly("Way back in Once upon a time time, there were three little pigs, all siblings. The first little big, Albert, was VERY lazy. He didn't want to work very hard so he wants to build his house out of straw.")
        print_slowly("The second little pig, Brenda, worked a little bit harder but was still a little lazy so she wants to build her house out of twigs.")
        print_slowly("The third little pig, Charlie, worked very hard and so he wants to build his house out of bricks.")
        print_kinda_slow("""
                                                          (
                                                           (  )
                                  .____.             ,-.  __)
                 \|/             //====\\         ,-' o `-!|
               .'+^+'.          //======\\     ,-'---------`-.
             .'///|\\\\'.      //========\\     | [+]   [+] |
            //////|\\\\\\\    //|||''''|||\\    |    ___    |
                           /((|||^..^|||))\   |||||^..^|||||    |   |   |   |
            ((|||(oo)|||)     |||||(oo)|||||    |   |'  |   |  
                Albert           Brenda          Charlie                                            
                                                                                             
                """)
        print("First you get to pick which pig you'd like to be:")
        print_kinda_slow("""
               _____
            ^..^     \9
            (oo)_____/
                WW WW              
            
            Pigs:
            A = Albert, a straw house
            B = Brenda, a twig house
            C = Charlie, a brick house
            """)
        pigchoice = input('>>> ')
        handle_pig_choice(pigchoice)

def handle_pig_choice(pigchoice):
    pigname = ""
    if pigchoice.lower() == "a":
        pigname = "Albert"
    elif pigchoice.lower() == "b":
        pigname = "Brenda"
    else:
        pigname = "Charlie"
    pig = get_pig(pigname)
    save_pig(pig)
    print(pig.name)
    choose_your_neighbor(pig)

def choose_your_neighbor(pig):

        print_kinda_slow("""
                               .
                              / V\
                            / `  /
                          <<   |
                          /    |
                        /      |
                      /        |
                     /    \  \ /
                    (      ) | |
            _______ |   _/_  | |
          __________\______)\__)

              Choose your neighbor:
              Wolf:
              A = THE Wolf
              B = BB Wolf
              """)
        wolfchoice = input('>>> ')
        handle_neighbor_choice(pig, wolfchoice)

def handle_neighbor_choice(pig, wolfchoice):
        wolfname=""
        if wolfchoice.lower == "a":
            wolfname = "THE Wolf"
        else:
            wolfname = "BB Wolf"
        wolf = get_wolf(wolfname)
        save_wolf(wolf)
        set_up_story(pig, wolf)

def set_up_story(pig, wolf):
        start_scene = 4
        if (pig.name == "Albert" or pig.name == "Brenda") and wolf.name == "THE Wolf":
             start_scene = 5
        elif (pig.name == "Albert" or pig.name == "Brenda") and wolf.name == "BB Wolf":
             start_scene = 6
        elif pig.name == "Charlie" and wolf.name == "THE Wolf":
             start_scene = 15
        elif pig.name == "Charlie" and wolf.name == "BB Wolf":
             start_scene = 16
        scene_1 = session.query(Scene).filter(Scene.scene_num == start_scene).first()
        story = Story(hero_id = pig.id, antagonist_id = wolf.id)
        #also want the option to go back, deleting the last decision made from the storyline
        session.add(story)
        session.commit()
        storyline = Storyline(story_id = story.id, scene_id = scene_1.id)
        global CURRENT_STORY
        global CURRENT_SCENE
        CURRENT_STORY = story
        CURRENT_SCENE = scene_1
        display_current_scene()

def display_current_scene():
    os.system("clear")
    global CURRENT_SCENE
    global CURRENT_STORY
    print_slowly(CURRENT_SCENE.description)
    print_slowly(f"A - {CURRENT_SCENE.choice_A}")
    print_slowly(f"B - {CURRENT_SCENE.choice_B}")
    print_slowly("C - go back")
    choice = input('>>> ')
    if choice == "C":
         os.system("clear")
         print("Going back")
    elif choice == "A":
        os.system("clear")
        CURRENT_SCENE = session.query(Scene).filter(Scene.scene_num == CURRENT_SCENE.choice_A_next_scene).first()
        Storyline(story_id = CURRENT_STORY.id, scene_id = CURRENT_SCENE.id)
        display_current_scene()
        
    else:
        os.system("clear")
        CURRENT_SCENE = session.query(Scene).filter(Scene.scene_num == CURRENT_SCENE.choice_B_next_scene).first()
        Storyline(story_id = CURRENT_STORY.id, scene_id = CURRENT_SCENE.id)
        display_current_scene()

def the_end():
     pass

#scene 7
#print("""
    
#                         (
#                           )     (
#                    ___...(-------)-....___
#                .-""       )    (          ""-.
#          .-'``'|-._             )         _.-|
#         /  .--.|   `""---...........---""`   |
#        /  /    |                             |
#        |  |    |                             |
#         \  \   |                             |
#          `\ `\ |                             |
#            `\ `|                             |
#            _/ /\                             /
#           (__/  \                           /
#        _..---""` \                         /`""---.._
#     .-'           \                       /          '-.
#    :               `-.__             __.-'              :
#    :                  ) ""---...---"" (                 :
#     '._               `"--...___...--"`              _.'
#       \""--..__                              __..--""/
#        '._     """----.....______.....----"""     _.'
#           `""--..,,_____            _____,,..--""`
#                         `"""----"""`
#  or 
#     ( (
#      ) )
#   ........
#  |        |]
#   \      /    
#    `----'

# """)
# scene 19
    #           (
    #            )  )
    #        ______(____
    #       (___________)
    #       /           \
    #      /             \
    #     |               |
    #  ____\             /____
    # ()____'.__     __.'____()
    #      .'` .'```'. `-.
    #     ().'`       `'.()

if __name__ == "__main__":
    display_welcome()
    while True:
        display_main_menu() 