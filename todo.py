# this file is the starting point for a lab to create a to-do list using built-in Python lists
"""module which provides a means for testing the existence of a file"""
from pathlib import Path

def todo_app():
    """start-up function for todo list app"""
    todo_list = [] #create empty list
    file_path = Path('todo.txt') # name of task file
    if file_path.is_file(): # if present, read todo's
        with open('todo.txt', 'r', encoding="utf-8") as todos:
            for todo in todos:
                todo_list.append(todo.strip())
    menu(todo_list)

def update_file(todo_list):
    """Function to write active list to backup file todo.txt"""
    with open('todo.txt', 'w', encoding="utf-8") as todos_file:
        for todo in todo_list: # iterate through list collection
            print(todo,file=todos_file) # or todos_file.write(todo + )
        # TODO: write list out to the file
        # print(todo,file=todos_file) or todos_file.write(todo + '\n')

def menu(todo_list):
    """main loop of todo list app"""
    while True:
        try: #catch any errors and don't let the app crash
            print("\nTo-Do's")

            # TODO: Implement reading list
            counter = 1
            for line in todo_list:
                    print(f'{counter}. {line}')
                    counter += 1

            print("\nTo Do List") # print menu
            print("1. Add Item")
            print("2. Delete Item")
            print("3. Quit\n")
            command = input("Enter Command: ")

            if command[0] == '1': # look at first character of input # TODO: Implement Add Item
                item = input("Enter task description: ")
                todo_list.append(item)
                update_file(todo_list)
            elif command[0] == '2':
                if len(todo_list) != 0:
                    item = input("Enter number of task to delete: ")
                    item_num = int(item[0]) # need a number here
                    for val in range(len(todo_list)):
                        if item_num - 1 == val:
                            todo_list.pop(val) # remove specified task
                            update_file(todo_list)
                else:
                    print("Your todo list is empty!") # duh!
            elif command[0] == '3':
                break # break out of while and terminate program
        except ValueError as e:
            print("Error caught:", e)

if __name__ == '__main__':
    todo_app() # launch app
    # TODO: Change app to be able to pass list on command line
