from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':

  engine = create_engine('sqlite:///development.db')
  session = sessionmaker(bind=engine)()
  print("Session Created...")


  set_trace()