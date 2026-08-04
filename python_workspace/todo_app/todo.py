import os
import time

print("--- TODO ---")
tasks = []

def list_menu():
    print("\n1. Add task")
    print("2. Remove task")
    print("3. Update task")
    print("4. List tasks")
    print("0. Exit")

def add_task(task):
    tasks.append(task)

def delete_task(index):
    tasks.pop(index)

def list_tasks(task_list):
    print("\nTasks")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")

def update_tasks(index):
    tasks.pop(index)
    new_task = input("New task: ")
    tasks.insert(index, new_task)

def control_empty():
    if tasks == []:
        print("\nTask list is empty!"
        "\nReturning main menu!")
        return True

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
        


while True:
    clear_terminal()
    list_menu()
    menu = input("\nMenu: ")
    
    while menu == "1":
        clear_terminal()
        print("ADD TASK")
        list_tasks(tasks)
        print("\nEnter '0' to return to the main menu")    

        new_task = input("Task: ")

        if new_task == "0":
            clear_terminal()
            break

        add_task(new_task)
        


    while menu == "2":
        clear_terminal()
        print("REMOVE TASK")
        if control_empty():
            time.sleep(2)
            clear_terminal()
            break

        list_tasks(tasks)
        print("\nEnter '0' to return to the main menu")
        removed_task = input("Enter the number of task will be removed: ")

        if removed_task == "0":
            clear_terminal()
            break

        if int(removed_task) > len(tasks) or int(removed_task) < 1:
            print("\nInvalid number!")
            continue

        remove_index = int(removed_task)
        remove_index -= 1
        delete_task(remove_index)
        print("\nTask removing!")
        time.sleep(1)
        print("Task removed!")
        time.sleep(0.2)

    while menu == "3":
        clear_terminal()
        print("UPDATE TASK")
        if control_empty():
            time.sleep(2)
            clear_terminal()
            break

        list_tasks(tasks)
        print("\nEnter '0' to return to the main menu")
        updated_task = input("Enter the number of task will be updated: ")

        if updated_task == "0":
            clear_terminal()
            break

        if int(updated_task) > len(tasks) or int(updated_task) < 1:
            print("\nInvalid number!")
            continue

        updated_task_index = int(updated_task)
        updated_task_index -= 1
        update_tasks(updated_task_index)
        print("Task being updated.")
        time.sleep(1)
        print("Done!")
        time.sleep(0.5)

    while menu == "4":
        clear_terminal()
        list_tasks(tasks)
        exit_listing = input("Enter '0' to return main menu")

        if exit_listing != "0":
            print("Invalid input!")
            time.sleep(1)
            continue
        else:
            break

    if menu == "0":
        break