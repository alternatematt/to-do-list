from tkinter import *
import tkinter as tk

class myGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root,text="To Do List", font=("Aerial",18))
        self.label.pack(padx=20,pady=20)

        #button
        
        self.addtaskbtn = tk.Button(self.root,text="Add Task",font=("Aerial",12))
        self.addtaskbtn.pack(padx=10,pady=10)
        
        self.viewtaskbtn = tk.Button(self.root,text="View Task",font=("Aerial",12))
        self.viewtaskbtn.pack(padx=10,pady=10)
        
        self.deletetaskbtn = tk.Button(self.root,text="Delete Task",font=("Aerial",12))
        self.deletetaskbtn.pack(padx=10,pady=10)
        
        self.quitbtn = tk.Button(self.root,text="Quit",font=("Aerial",12),command=self.root.destroy)
        self.quitbtn.pack(padx=10,pady=10)


        self.root.mainloop()
    
    

myGUI()
        


"""
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
        tasktodelete = tasktodelete + 1 #fixed index
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

"""