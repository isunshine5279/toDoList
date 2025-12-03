"""Build simple python to do list app
#that has features
# Add tasks
# View tasks
# Delete tasks
# quit the application
#includes error handling
# aaa

"""


# storage of  tasks
tasks = []

#defining function to show the list of menu
def show_menu():
    #display the menu list 
    print("\n========== Here is our To Do List Menu ==========")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Quit the application")

#defining function to add tasks
def add_tasks():
    new_task = input("\n Please enter a task you want to add: ") #Prompt user to add a new task
    tasks.append(new_task) #Adding new task to the list
    print(f"New task {new_task} added successfully. ")
   # print(tasks)

#Function to view all the tasks in the list
def view_task():
    if len(tasks) == 0:
        print("\n Your task list is empty.")
        return
    
    print("Your task list: ")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
        
#Function to remove all the tasks in the list
def remove_task():

    if len(tasks) == 0:
        print("\n No tasks to delete.")
        return
    
    view_task()

    try:
        choice = int(input("Please enter the task number you want to delete: "))
    except ValueError:
        print("Invalid number entered.")
    
    else:
        if 1<=choice<=len(tasks):
            deleted_task = tasks.pop(choice-1)
            print(f"Task '{deleted_task}' deleted successfully")
        else:
             print("Invalid task number")
    finally:
        print("Delete task operation completed.")
    
    
    

def main():

    '''Main Program loop'''

    print("Welcome to your command line to-do list app!")
    
    while True:
        show_menu()
        
        try:
             choice = int(input("What would you like to get done? "))
        except ValueError:
            
            print("Please enter a valid number from the menu.")
            continue

        if choice == 1:
                add_tasks()
        elif choice == 2:
                view_task()
        elif choice == 3:
                 remove_task()
        elif choice == 4:
             print("Exiting the application.")
             break
        else:
            print("Please choose an option between 1 and 4 for the task you want to implement.")
        
        #finally:
           # print("Task completed. 

#Run the program
                 
main()






    



