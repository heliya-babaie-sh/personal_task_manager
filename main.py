name = input("please enter your name : ")
print("welcome", name)
tasks = []
while True:

    task = input("enter a task or enter exit: ")
    if task == "exit":
        break
    else:
        tasks.append(task)
        continue
        