from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Scene, Story, Storyline
from helpers import *
import os

engine = create_engine('sqlite:///db/3_little_pigs.db')
#some how i disconnected my database!?
session = sessionmaker(bind=engine)()

CURRENT_STORY = None
CURRENT_SCENE = None

def display_welcome():
     print_kinda_slow(r"""
                                
                                
                             ____    _      _ _   _   _        _____ _           
                            |___ \  | |    (_) | | | | |      |  __ (_)          
                              __) | | |     _| |_| |_| | ___  | |__) |  __ _ ___ 
                             |__ <  | |    | | __| __| |/ _ \ |  ___/ |/ _` / __|
                             ___) | | |____| | |_| |_| |  __/ | |   | | (_| \__ \
                            |____/  |______|_|\__|\__|_|\___| |_|   |_|\__, |___/
                                                                        __/ |    
                                                                        |___/     

                                        choose your own adventure
                  
                                                                             (
                                                                            (  )
                                                    .____.             ,-.  __)
                                  \||/             //====\\         ,-' o `-!|
                                .'+^^+'.          //======\\     ,-'---------`-.
                              .'///||\\\\'.      //========\\     | [+]   [+] |
                             //////||\\\\\\\    //|||''''|||\\    |    ___    |
                            /((|||^..^|||))\    |||||^..^|||||    |   |   |   |
                             ((|||(oo)|||))     |||||(oo)|||||    |   |'  |   |  
                                 Albert             Brenda           Charlie                                            
                          
                    
                  """)

def display_main_menu():

        print_slowly("Way back in Once upon a time time, there were three little pigs, all siblings."
                     ) 
        
        print_slowly("The first little pig, Albert, was VERY lazy. He didn't want to work very hard so he wants to build his house out of straw."
                     )
        
        print_slowly("The second little pig, Brenda, worked a little bit harder but was still a little lazy so she wants to build her house out of twigs."
                     )
        
        print_slowly("The third little pig, Charlie, worked very hard and so he wants to build his house out of bricks."
                     )
        #need to format text so it's more enjoyable to read

        print("First pick which pig you'd like to be:"
              )
        
        print_kinda_slow(r"""
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

        print_kinda_slow(r"""
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
        if wolfchoice.lower() == "a":
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
        session.add(story)
        session.commit()
        storyline = Storyline(story_id = story.id, scene_id = scene_1.id)
        global CURRENT_STORY
        global CURRENT_SCENE
        CURRENT_STORY = story
        CURREN_SCENE = scene_1
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
        #  session.query(Storyline).filter_by(scene_id=CURRENT_SCENE.id).delete()
        #  previous_scene = CURRENT_SCENE.previous_scene
        #  if previous_scene:
        #       CURRENT_SCENE = previous_scene
        #       CURRENT_STORY.storyline.pop()
        #       session.commit()
        #  else:
              
        #       print("No previous scene to go back to.") 
              #neeed to somehow connect to Storyline or add a previous scene column to storyline?
         display_current_scene()
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
    #if choiceA == "back to main menu":
    # print(""" THE END- but in ascii - need to find """)
    #then choose the title of your story, commit to Story in title
    # then can to back to main_menu
    # should this be in a function like below? the_end?
    # print(r"""
    #   _______ _    _ ______   ______ _   _ _____  
#      |__   __| |  | |  ____| |  ____| \ | |  __ \ 
#         | |  | |__| | |__    | |__  |  \| | |  | |
#         | |  |  __  |  __|   |  __| | . ` | |  | |
#         | |  | |  | | |____  | |____| |\  | |__| |
#         |_|  |_|  |_|______| |______|_| \_|_____/ 
#  or

#  .----------------.  .----------------.  .----------------.   .----------------.  .-----------------. .----------------. 
# | .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |
# | |  _________   | || |  ____  ____  | || |  _________   | | | |  _________   | || | ____  _____  | || |  ________    | |
# | | |  _   _  |  | || | |_   ||   _| | || | |_   ___  |  | | | | |_   ___  |  | || ||_   \|_   _| | || | |_   ___ `.  | |
# | | |_/ | | \_|  | || |   | |__| |   | || |   | |_  \_|  | | | |   | |_  \_|  | || |  |   \ | |   | || |   | |   `. \ | |
# | |     | |      | || |   |  __  |   | || |   |  _|  _   | | | |   |  _|  _   | || |  | |\ \| |   | || |   | |    | | | |
# | |    _| |_     | || |  _| |  | |_  | || |  _| |___/ |  | | | |  _| |___/ |  | || | _| |_\   |_  | || |  _| |___.' / | |
# | |   |_____|    | || | |____||____| | || | |_________|  | | | | |_________|  | || ||_____|\____| | || | |________.'  | |
# | |              | || |              | || |              | | | |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------' 
# or 
#
#  ____  _  _  ____    ____  __ _  ____ 
# (_  _)/ )( \(  __)  (  __)(  ( \(    \
#   )(  ) __ ( ) _)    ) _) /    / ) D (
#  (__) \_)(_/(____)  (____)\_)__)(____/
# or

                                                             
# ,--------.,--.  ,--.,------.    ,------.,--.  ,--.,------.   
# '--.  .--'|  '--'  ||  .---'    |  .---'|  ,'.|  ||  .-.  \  
#    |  |   |  .--.  ||  `--,     |  `--, |  |' '  ||  |  \  : 
#    |  |   |  |  |  ||  `---.    |  `---.|  | `   ||  '--'  / 
#    `--'   `--'  `--'`------'    `------'`--'  `--'`-------'  
# or

                                                             



                                              
                                    # """)
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