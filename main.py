while True:
    user_action = input("Type add,show,edit,complete,exit :-")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todos :-") + ("\n")

            # file = open('todos.txt', 'r') -- Previous 1
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with  open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # The shorter way of doing it
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
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
