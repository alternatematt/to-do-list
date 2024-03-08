tasks = []

def addTask():
    task = input("Please enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added to list")

def listTask():
    if not tasks:
        print("Empty list of tasks")
    else:
        print("Current Tasks: ")
        for i, task in enumerate(tasks):
            i = i+1
            print(f"Task #{i}. {task}")

def deleteTask():
    listTask()

    try:
        tasktodelete = int(input("Select # to delete: "))
        if(tasktodelete>=0 and tasktodelete < len(tasks)):
            tasks.pop(tasktodelete)
            print(f"Task {tasktodelete} was deleted successfully ")
        else:
            print(f"Task #{tasktodelete} was not found")
    
    except:
        print("Invalid input.")
    




if __name__ == "__main__":
    ##create a loop to run the app
    print("Welcome!")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice = input("Enter you choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Try again.. ")

    print("Cya")