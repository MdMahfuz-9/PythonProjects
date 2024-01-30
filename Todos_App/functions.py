def get_todos(filepath = 'todos.txt'): #In side the perenthesis is the defult
    """ Read a file and return the list of to-do items """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos( todos_arg, filepath = "todos.txt"):  # save the new todos to the file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
