import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = 'Enter todo', key='todo')
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todo'])

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            #list_box = sg.Listbox(values=functions.get_todos(), key='todos',
             #                     enable_events=True, size=[45, 10])
            window['todos'].update(values=todos)
        case 'Edit':
            todos = functions.get_todos()
            for i in todos:
                print(i)
            print(todos)
            old_value = values['todos']

            new_value = values['todo'] + '\n'
            print('old_value', old_value)
            index = todos.index(old_value[0])
            todos[index] = new_value
            window['todos'].update(values=todos)
        case 'Complete':
            todos = functions.get_todos()
            old_value = values['todos']
            index = todos.index(old_value[0])
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Exit':
            exit()

        case sg.WIN_CLOSED:
            break
window.close()