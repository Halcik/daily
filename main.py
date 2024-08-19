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
    date = counter[1].split()
    date = datetime(day=int(date[0]), month=int(
            date[1]), year=int(date[2]))
    if date != date_now:
        counter[0] = "0"
        counter[1] = f"{date_now.day} {date_now.month} {date_now.year}\n"
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
            counter[0] = str(int(counter[0]) + 1)
    counter_file = open("counter.txt", "w", encoding='utf-8')
    counter = "  ".join(counter)
    counter_file.write(counter)
    counter_file.close()

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
    print(tasks_tab)
    tasks = open("tasks.txt", "w", encoding='utf-8')
    tasks.writelines(tasks_tab)
    tasks.close()    




if __name__ == '__main__':
    date_now = datetime.now()
    date_now = datetime(day=date_now.day, month=date_now.month, year=date_now.year)
    delete_tasks(date_now)
    #task = new_task()
    #read_tasks(date_now)
    #update_status(date_now)
