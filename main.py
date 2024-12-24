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
def create_a_task():
    task = input('Please enter a task:')
    while len(task.strip()) == 0:
        task = input('Please enter a task:')

    if len(task) > 0:
        with open('tasks.txt', 'a', encoding="utf-8") as file:
            file.write(task + '\n' )



if menu == 1:
    see_all_tasks()
elif menu == 2:
    create_a_task()
elif menu == 3:
    print("33333")
elif menu == 4:
    print("44444")
else:
    menu = int(input('Choose a menu number:'))