from functions import get_todos ,write_todos


while True:
    user_action = input("Type add,show,edit,complete,exit :-")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos("new.txt")

        todos.append(todo )

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index}-{item}"
            print(row)


    elif 'edit' in user_action:

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index}-{item}"
            print(row)
        edit_num = int(input("Enter number -"))

        replaced_todos = input("enter new todo")
        todos[edit_num] = replaced_todos + '\n'

        write_todos( todos)

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
            pop_num = int(input("which one is complete:- "))
            todos.pop(pop_num)

            write_todos(todos)
        except IndexError:
            print("No item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not found")


print("Bye Bye")
