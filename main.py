from datetime import datetime
from database import *
import pandas as pd

if __name__ == '__main__':
    path = sys.argv[0][:-12]
    db = create_database(path)
    
    date_now = datetime.now()
    date_now = datetime(day=date_now.day, month=date_now.month, year=date_now.year)