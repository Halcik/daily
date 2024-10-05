# date  name  category  duration
from datetime import datetime
from pathlib import Path
import sys


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
    end_date = "1 1 2000"
    id_file = open("id.txt", "r", encoding='utf-8')
    id = str(int(id_file.readline())+1)
    id_file.close()
    id_file = open("id.txt", "w", encoding='utf-8')
    task = [date, id, name, category, duration, status, end_date]
    id_file.write(id)
    add_task_to_file(task)


def read_tasks(date_now):
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()[1:]
    i = 1
    print("\nZadania na dziś:")
    for task in tasks_tab:
        task = task.split("  ")
        date = task[0].split()
        date = datetime(day=int(date[0]), month=int(
            date[1]), year=int(date[2]))
        if date == date_now:
            if task[5]=="NO":
                status = "☐"
            else:
                status = "☑"
            print(f"{i}.{status} [id {task[1]}] {task[2]} ({task[3]}) - {task[4]} min.")
            i += 1
    print("\nZaległe:")
    for task in tasks_tab:
        task = task.split("  ")
        date = task[0].split()
        date = datetime(day=int(date[0]), month=int(
            date[1]), year=int(date[2]))
        if date < date_now:
            if task[5]=="NO":
                status = "☐"
            else:
                status = "☑"
            print(f"{i}.{status} [id {task[1]}] {task[2]} ({task[3]}) z {task[0].replace(' ', '.')} - {task[4]} min.")
            i += 1
    tasks.close()


def update_status(date_now):
    counter_file = open("counter.txt", "r", encoding='utf-8')
    counter = counter_file.readline().split("  ")
    id = input('Podaj id zadania do zaktualizowania: ')
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()
    tasks.close()
    counter_file.close()
    for i, task in enumerate(tasks_tab):
        task = task.split("  ")
        if task[1] == id:
            task[-2] = "YES"
            task[-1] = f"{date_now.day} {date_now.month} {date_now.year}\n"
            task = '  '.join(task)
            tasks_tab[i] = task
            tasks = open("tasks.txt", "w", encoding='utf-8')
            tasks.writelines(tasks_tab)
            tasks.close()
            counter[0] = str(int(counter[0]) + 1)
    counter_file = open("counter.txt", "w", encoding='utf-8')
    counter = "  ".join(counter)
    counter_file.write(counter)
    counter_file.close()
    display_n_done()


def delete_tasks(date_now):
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()
    tasks.close()
    for i, task in enumerate(tasks_tab[1:]):
        task = task.split("  ")
        date = task[-1].split()
        date = datetime(day=int(date[0]), month=int(
            date[1]), year=int(date[2]))
        if task[-2] == "YES" and date != date_now:
            tasks_tab[i+1] = ""
    tasks = open("tasks.txt", "w", encoding='utf-8')
    tasks.writelines(tasks_tab)
    tasks.close()
    counter_file = open("counter.txt", "r", encoding='utf-8')
    counter = counter_file.readline().split("  ")
    counter_file.close()
    date = counter[1].split()
    date = datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]))
    if date != date_now:
        counter[0] = "0"
        counter[1] = f"{date_now.day} {date_now.month} {date_now.year}\n"
    counter_file = open("counter.txt", "w", encoding='utf-8')
    counter = "  ".join(counter)
    counter_file.write(counter)
    counter_file.close()


def display_n_done():
    counter_file = open("counter.txt", "r", encoding='utf-8')
    counter = counter_file.readline().split("  ")[0]
    print(f"\n~ Liczba wykonanych dzisiaj zadań: {counter} ~")

def check_files():
    path = sys.argv[0][:-12]
    files = ('counter.txt', 'id.txt', 'tasks.txt')
    contents = ('0  1 1 2000', '0', 'date  id  name  category  duration  status  end_date\n')
    for i, file in enumerate(files):
        file = Path(path, file)
        if file.exists():
            continue
        create = open(file.name, "w")
        create.write(contents[i])
        create.close()


if __name__ == '__main__':
    check_files()
    date_now = datetime.now()
    date_now = datetime(day=date_now.day, month=date_now.month, year=date_now.year)
    delete_tasks(date_now)
    print("Cześć!")
    read_tasks(date_now)
    while True:
        print("\nWybierz opcję:\n[1] Dodaj zadanie\n[2] Ukończ zadanie\n[3] Pokaż zadania\n[4] Pokaż liczbę zrobionych zadań\n[5] Wyłącz program")
        option = int(input())
        match option:
            case 1:
                new_task()
            case 2:
                update_status(date_now)
            case 3:
                read_tasks(date_now)
            case 4:
                display_n_done()
            case 5:
                break
        
