todos = []
print(type(todos))


while True:
    user_action = input("Type add , show , edit ,exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Type new todo : ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)

        case 'edit':
            number = int(input("Enter the number of todo: "))
            number = number - 1
            new_todos = input("Enter the new todos : ")
            todos[number] = new_todos 
           

        case 'exit':
            break

print("Bye")

