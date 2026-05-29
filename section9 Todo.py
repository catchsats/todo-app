import time

from functions import get_todos, write_todos
todos = []

while True:
    now = time.strftime('%d-%m-%Y %H:%M:%S')
    #Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit, remove: ")
    user_action = user_action.strip()


    if user_action.startswith('add') or user_action.startswith('new') :
        user_input = user_action[4:] + ' ' + now + '\n'
        todos.append(user_input)
        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            row = f"{index}--{item}"
            print(row.strip())
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1
            usernewvalue_input = input('New value to be added to the list: ')
            todos = get_todos('todos.txt')
            todos[int(number) - 1] = usernewvalue_input + " " + now + '\n'
            print('new ', todos)
            write_todos(todos)
        except ValueError:
            print("Invalid input, Enter a number followed by edit")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[7:])
            todosoremovedvalue = todos[number].strip('\n')
            todos.pop(number)
            write_todos(todos)
            message = f"Todo {todosoremovedvalue} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break