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