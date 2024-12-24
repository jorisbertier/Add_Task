with open("tasks.txt", "r", encoding="utf-8") as file:
    tasks = file.readlines()
    tasks = [t.strip() for t in tasks]

def display_menu():
    print('Manager of tasks')
    print('--------------')
    print('1. See all tasks')
    print('2. Create a task')
    print('3. Delete a task')
    print('4. Modify a task')

display_menu()

menu = int(input('Choose a menu number:'))

# MENU 1 SEE ALL TASKS
def see_all_tasks():
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
    print('List of tasks, please enter the task to delete corretly')

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if not tasks:
        print('No task available to delete')
        return
    
    for i, task in enumerate(tasks, start=1):
        print(f'[{i}]-{task}')
    
    select_task = input('Please select a task to delete:')
    # with open("tasks.txt", "w", encoding="utf-8") as file:
    #     for i, task in enumerate(tasks, start=1):
    #         if select_task == task.strip():
    #             task_found = True
    #             print(f'Deleted task found: {task}')
    #             continue
    #         file.write(task)
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
    print('List of tasks, please enter the task to delete corretly')
    see_all_tasks()

    select_task = input('Please select a task to delete:')
    task_found = False

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            # print(t.strip())
            # print(t)
            if select_task == task.strip():
                task_found = True
                print(f'Deleted task found: {task}')
                continue
            file.write(task)

    if not task_found:
        print('Task not found')
    return

if menu == 1:
    see_all_tasks()
elif menu == 2:
    create_task()
elif menu == 3:
    delete_task()
elif menu == 4:
    print("44444")
else:
    menu = int(input('Choose a menu number:'))