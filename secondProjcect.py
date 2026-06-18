to_do = []

operations = {
    1 : 'Add task',
    2 : 'Delete task',
    3 : 'View tasks',
    4 : 'Exit',
}

print("Welcome to our To do application")

while True:
    print('opearations : ',operations)
    choice = int(input('Enter idex, what to do'))

    if choice == 1 :
        add_task = input('Enter your task')
        to_do.append(add_task)
        print('Task added')
    elif choice ==2 :
        if len(to_do) == 0:
            print("The to-do list is empty.")
        else:
            del_task = input('Enter task which you want to delete')
            if del_task in to_do:
                to_do.remove(del_task)
                print('Task deleted')
            else:
                print('task not found')
    elif choice == 3:
        if len(to_do) == 0:
            print("The to-do list is empty.")
        else:
            print('Tasks:',to_do)

    elif choice == 4:
        print('Exiting..')
        break
    else :
        print('Invalid choice..')
print(to_do)

