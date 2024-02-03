FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH): #In side the perenthesis is the defult
    """ Read a file and return the list of to-do items """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos( todos_arg, filepath = FILEPATH):  # save the new todos to the file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __main__ == "__main__":
    print("hello")
    print(get_todos())
    '''This block of code will only 
    be exicuted when this file is run as main'''