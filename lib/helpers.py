from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Character, Story
import time

engine = create_engine('sqlite:///db/3_little_pigs.db')
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

def save_pig(character):
    new_story = Story(title="", hero_id=character.id, antagonist_id=None)
    session.add(new_story)
    session.commit()

def save_wolf(character):
    character.antagonist_id = character.id
    session.commit()

def get_pig(pigname):
    pig = session.query(Character).filter(Character.name == pigname).first()
    return pig

def get_wolf(wolfname):
    wolf = session.query(Character).filter(Character.name == wolfname).first()
    return wolf