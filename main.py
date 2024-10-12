from datetime import datetime
from database import *
import pandas as pd
import sqlite3

def read_tasks(db, today):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"Select t.name, c.name FROM tasks as t INNER JOIN category as c ON t.category_id=c.id WHERE t.date_t='{today.year}-{today.month}-{today.day}';")
    tasks = cursor.fetchall()

    for task in tasks:
        print(task[0], task[1])
    


    #print("Zadania na dziś:")
    #df = pd.read_sql(f"Select t.name, c.name FROM tasks as t INNER JOIN category as c ON t.category_id=c.id WHERE t.date_t='{today.year}-{today.month}-{today.day}';", conn)
    #print(df)

if __name__ == '__main__':
    path = sys.argv[0][:-8]
    db = create_database(path) #return absolute path to the database
    
    today = datetime.now()
    today = datetime(day=today.day, month=today.month, year=today.year)
    read_tasks(db, today)