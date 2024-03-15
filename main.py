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
    task = [date, name, category, duration, status]
    return task

def read_tasks():
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()
    for i, task in enumerate(tasks_tab):
        if i>0:
            print(i, end=". ")
        print(task.replace("\n", ""))
    tasks.close()

task = new_task()
add_task_to_file(task)
read_tasks()