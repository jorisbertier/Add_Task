
def display_menu():
    print('Tasks manager')
    print('--------------')
    print('1. See all tasks')
    print('2. Create a task')
    print('3. Delete a task')
    print('4. Modify a task')
    print('Type 5 to close the program' )

# MENU 1 SEE ALL TASKS
def see_all_tasks():
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            tasks = [t.strip() for t in tasks]
        print(tasks)


# MENU 2 CREATE A TASK
def create_task():
    task = input('Please enter a task:')
    while len(task.strip()) == 0:
        task = input('Please enter a task:')

    if len(task) > 0:
        with open('tasks.txt', 'a', encoding="utf-8") as file:
            file.write(task + '\n' )

# MENU 3 DELETE A TASK
def delete_task():

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if not tasks:
        print('No task available to delete')
        return
    
    print('List of tasks')
    print('---------')
    for i, task in enumerate(tasks, start=1):
        print(f'[{i}]-{task}')
    
    select_task = input('Please select a task to delete:')

    try:
        task_index = int(select_task) - 1
        if task_index < 0 or task_index >= len(tasks):
            print('Invalid task number. Try again')
            select_task = input('Please select a task to delete:')
            return
    except ValueError:
        print("Please enter a valid number.")
        select_task = input('Please select a task to delete:')
        return

    task_delete = tasks.pop(task_index)

    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(tasks)
    print(f"Task deleted : {task_delete.strip()}")

# Menu 4 MODIFY A TASK
def modify_task():
    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if not tasks:
        print('No task available to delete')
        return
    
    print('List of tasks')
    print('---------')
    for i, task in enumerate(tasks, start=1):
        print(f'[{i}]-{task}')
    
    select_task = input('Please select a task to delete:')

    try:
        task_index = int(select_task) - 1
        if task_index < 0 or task_index >= len(tasks):
            print('Invalid task number. Try again')
            select_task = input('Please select a task to delete:')
            return
        modify_task = input(f'Modify task [{task_index}] :')
    except ValueError:
        print("Please enter a valid number.")
        select_task = input('Please select a task to delete:')
        return
    
    tasks[task_index] = modify_task + '\n'

    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print(f"Task modify to: {tasks[task_index].strip()}")

def main():
    display_menu()
    menu = int(input('Choose a menu number:'))
    if menu == 1:
        see_all_tasks()
    elif menu == 2:
        create_task()
    elif menu == 3:
        delete_task()
    elif menu == 4:
        modify_task()
    elif menu == 5:
        print('Tasks manager is close')
        exit()
    else:
        menu = int(input('Choose a menu number:'))

main()