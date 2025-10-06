def task():
    tasks = []
    print("-----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i}= ")
        tasks.append(task_name)