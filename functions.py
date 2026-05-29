FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """return the todo list from the text file"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)
