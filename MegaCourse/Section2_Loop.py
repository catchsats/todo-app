userinput = "Enter a todo:"
todos = []

while True:
    todo = input(userinput)
    print(todo.title())
    todos.append(todo)
    print(todos)
    print("Next....")
