while True:
    user_action = input("Type add,show,edit,complete,exit :-")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todos :-") + ("\n")

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
        case 'complete':
            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
            pop_num = int(input("which one did you complete:-"))
            todos.pop(pop_num)
        case 'edit':
            for item in todos:
                print(item)
            edit_num = int(input("which one do you like to edit:-"))

            replaced_todos = input("New todos :- ")
            todos[edit_num] = replaced_todos
        case 'exit':
            break

print("Bye Bye")
