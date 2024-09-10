def get_todos(filepath='todos.txt'):
    """ Read a file and return to do list items. """
    with open(filepath, 'r') as text:
        todos_local = text.readlines()
    return todos_local

def write_todos(todos_ags, filepath='todos.txt'):
    """ Open a metioned file and write the given
    todo list item into it. """
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_ags)


print(__name__)
# if __name__ == "__task__":
#     print("Hello")


