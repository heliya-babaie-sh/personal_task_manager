from task import  show_task, add_task

name = input("please enter your name : ")
print("welcome", name) 

tasks = []
while True:

    task = input("enter a task or enter exit: ")
    if task == "exit":
        break
    else:
        add_task(task)
        continue

show_task()
        