# date  name  category  duration
from datetime import datetime

def add_task_to_file(task):
    tasks = open("tasks.txt", "a", encoding='utf-8')
    tasks.write("  ".join(task)+"\n")
    tasks.close()

def new_task():
    print("Wpisz datę wykonania zadania według poniższego wzoru:")
    date = input("dzień miesiąc rok\n")
    name = input("Podaj nazwę zadania:\n")
    category = input("Podaj nazwę kategorii:\n")
    duration = input("Podaj, ile czasu trwa wykonanie zadania w min:\n")
    status = "NO"
    id_file = open("id.txt", "r", encoding='utf-8')
    id = str(int(id_file.readline())+1)
    id_file.close()
    id_file = open("id.txt", "w", encoding='utf-8')
    task = [date, id, name, category, duration, status]
    id_file.write(id)
    add_task_to_file(task)
    


def read_tasks(get_date):
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()[1:]
    i = 1
    print("Zadania na dziś:")
    for task in tasks_tab:
        date = task.split()[0:3]
        date = datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]))
        if date==get_date:
            print(i, end=". ")
            print(task.replace("\n", "")[:-3])
            i+=1
    print("\nZaległe:")
    for task in tasks_tab:
        date = task.split()[0:3]
        date = datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]))
        if date<get_date:
            print(i, end=". ")
            print(task.replace("\n", "")[:-3])
            i+=1
    tasks.close()

task = new_task()
date_now = datetime.now()
date_now = datetime(day=date_now.day, month=date_now.month, year=date_now.year)
read_tasks(date_now)