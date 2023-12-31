tasks = []

def addTASK ():
    task = input("please enter the task :")
    tasks.append(task)
    print(f"Task '[task]' added to list.")

def listTaks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("current Tasks:")
        for index , task in enumerate(tasks):
            print(F"Task {index}.{task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("choose the task you want to delete :"))
        if taskToDelete >=0 and  taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"task[taskToDelete] has been removed.")
        else:
             print(f"task[taskToDelete] was not found.")
    except:
        print("invalid input.")
if __name__ == "__main__":
   print("Welcome to the to do list app:)")
        WhileTrue:
                print("\n")
                print("please select one of the following option")
                print("_________________________________________")
                print("1. Add a new task")
                print("2. Delete a task")
                print("3. List tasks")
                print("4. Quit")

       choice = input("Enter your choice: ")

       if (choice == "1"):
         addTask()
       elif(choice =="2"):
         deleteTask()
       elif(choice =="3"):
           listTasks()
       elif(choice =="4"):
           break

       else:
           print("invalid input .please try again.")

print("goooood byeeeee")
           
