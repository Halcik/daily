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
    end_date = "0 0 0"
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
    print("Zadania na dziś:")
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
    print(counter)
    id = input('Podaj id zadania: ')
    tasks = open("tasks.txt", "r", encoding='utf-8')
    tasks_tab = tasks.readlines()
    tasks.close()
    counter_file.close()
    for task in tasks_tab:
        task = task.split("  ")
        if task[1] == id:
            task[-2] = "YES"
            task[-1] = f"{date_now.day} {date_now.month} {date_now.year}\n"
            task = '  '.join(task)
            tasks_tab[int(id)] = task
            tasks = open("tasks.txt", "w", encoding='utf-8')
            tasks.writelines(tasks_tab)
            tasks.close()


if __name__ == '__main__':
    # task = new_task()
    date_now = datetime.now()
    date_now = datetime(day=date_now.day, month=date_now.month, year=date_now.year)
    read_tasks(date_now)
    #update_status(date_now)
