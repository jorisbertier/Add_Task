task = input('Please enter a task:')


while len(task.strip()) == 0:
    task = input('Please enter a task:')

if len(task) > 0:
    with open('tasks.txt', 'a', encoding="utf-8") as file:
        file.write(task + '\n' )

with open("tasks.txt", "r", encoding="utf-8") as file:
    tasks = file.readlines()

tasks_cleaned = [t.strip() for t in tasks]
print(tasks_cleaned)
