from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from models import Characters, Scenes, Story, Storyline

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.02)
        # time.sleep(0)
    print()

def print_kinda_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()

def print_rapidly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.004)
        # time.sleep(0)
    print()






    


# def passenger_command(user_input):
#     if user_input.lower() == "all":
#         print_slowly("*" * 10 + " All Passengers " + "*" * 10)
#         show_all_passengers()
#     elif user_input.lower() == "booked":
#         print_slowly("*" * 10 + " Booked Passengers " + "*" * 10)
#         show_booked_passengers()
#         while True:
#             print_slowly("Select an option:")
#             print_slowly("1 => \tRebook a passenger on a different flight")
#             print_slowly("2 => \tGo back to the passengers menu")
#             print_slowly("3 => \tGo back to the main menu")
#             awaiting_input = input()
#             if awaiting_input == "1":
#                 print_slowly("Enter the passenger ID to rebook them on a flight (I sure hope they make it in time):")
#                 passenger_id = input()
#                 re_book_passenger(passenger_id)
#             elif awaiting_input == "2":
#                 break
#             elif awaiting_input == "3":
#                 return "exit"
#             else:
#                 print_slowly("Invalid selection. Come on... there are only three choices.")
#     elif user_input.lower() == "awaiting":
#         print_slowly("*" * 10 + " Passengers Awaiting Flights " + "*" * 10)
#         show_awaiting_passengers()
#         while True:
#             print_slowly("Select an option:")
#             print_slowly("1 => \tBook a passenger on a flight")
#             print_slowly("2 => \tGo back to the passengers menu")
#             print_slowly("3 => \tGo back to the main menu")
#             awaiting_input = input()
#             if awaiting_input == "1":
#                 print_slowly("Enter the passenger ID to book them on a flight:")
#                 passenger_id = input()
#                 book_passenger(passenger_id)
#             elif awaiting_input == "2":
#                 break
#             elif awaiting_input == "3":
#                 return "exit"
#             else:
#                 print_slowly("Invalid selection. Come on... there are only three choices.")
#     elif user_input.lower() == "exit":
#         return "exit"
#     else:
#         print_slowly("Invalid command. Please try again or type 'exit' to return to the main menu:")



# greeting_image = """
#          ___________                |
#         |CLI Airport|               |
#          ```````````                |
#                                   .-'-.
#                                  ' ___ '
#                        ---------'  .-.  '---------
#        _________________________'  '-'  '_________________________
#         ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
#                       \    /  ||/   H   \||  \    /
#                        '--'   OO   O|O   OO   '--'
# """
