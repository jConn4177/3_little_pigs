from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import Characters, Scenes, Story, Storyline, choice_A_next_scene, choice_B_next_scene
from helpers import *
import time

engine = create_engine('sqlite:///3_little_pigs.db')
session = sessionmaker(bind=engine)()

if __name__ == "__main__":
  
  def main_menu():
    while True:
        print_slowly("3 Little Pigs - choose your own adventure")
        print("""
                                                        (
                                                      (  )
                             .____.            ,-.  __)
             \|/            //====\\        ,-' o `-!|
           .'+^+'.         //======\\    ,-'---------`-.
         .'///|\\\\'.     //========\\    | [+]   [+] |          .-------------.
        //////|\\\\\\\   //|||''''|||\\   |    ___    |         <   huff, puff  >
       /((|||^..^|||))\  |||||^..^|||||   |   |   |   |    //    `--v----------'
        ((|||(oo)|||)    |||||(oo)|||||   |   |'  |   |   |..~~~O
                                                         {   ~vv'
                                                            |
                                                            >O<
                """)
        print("Way back in Once upon a time time, there were three little pigs all siblings. The first little big, Albert, was VERY lazy. He didn't want to work very hard so he wants to build his house out of straw.")
        print("The second little pig, Brenda, worked a little bit harder but was still a little lazy so she wants to build her house out of twigs.")
        print("The third little pig, Charlie, worked very hard and so he wants to build his house out of bricks.")
        print("First you get to pick which pig you'd like to be:")
    
        print("""
            Pigs:
            A = Albert, a straw house
            B = Brenda, a twig house
            C = Charlie, a brick house
            """)
        pigchoice = input('>>> ')
        print("""
              Wolf:
              A = THE Wolf
              B = BB Wolf
              """)
        wolfchoice = input('>>> ')
        set_up_story(pigchoice, wolfchoice)
        main_menu()

        current_scene = scene_4

        while current_scene is not None:
           advance_to_next_scene(current_scene, choice_A_next_scene, choice_B_next_scene)
           current_scene = advance_to_next_scene

 #-----------------------------   

        # moved this to a helper function 
        # print(scene_4.description)
        # print("""
        #        A = choiceA
        #        B = choiceB
        #    """)
        # choice = input('>>> ')
        # if choice == "A":
        #     clear()
        #     print(choice_A_next_scene)
        # if choice == "B":
        #     clear()
        #     print(choice_B_next_scene)

# instead of repeating this with each scene
# #scene_5
#     print(scenes.scene_num.5.description)
#     print("""
#           A = choiceA
#           B = choiceB
#           """)
#     choice = input('>>> ')
#     if choice == "A":
#        clear()
#        print(choice_A_next_scene)
#     if choice == "B":
#        clear()
#        print(choice_B_next_scene)

# #scene_6
#     print(scenes.scene_num.6.description)
#     print("""
#           A = choiceA
#           B = choiceB
#           """)
#     choice = input('>>> ')
#     if choice == "A":
#        clear()
#        print(choice_A_next_scene)
#     if choice == "B":
#        clear()
#        print(choice_B_next_scene)
       