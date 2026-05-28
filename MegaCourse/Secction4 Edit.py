todos = []

while True:
    #Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit, remove: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            user_input = input('Item to be added todo: ') + '\n'
            todos.append(user_input)
            with open('todos.txt', 'a') as file:
                file.writelines(user_input)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                row = f"{index}--{item}"
                print(row.strip())
        case 'edit':
            number = input('Provide index number: ')
            usernewvalue_input = input('New value to be added to the list: ')

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            print(usernewvalue_input)
            print('old ', todos)
            todos[int(number) - 1] = usernewvalue_input + '\n'
            print('new ', todos)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'remove':
            number = int(input('Provide index number: '))
            todosoremovedvalue = todos[number].strip('\n')
            todos.pop(number)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todosoremovedvalue} was removed from the list."
            print(message)
