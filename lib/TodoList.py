# File: lib/todo_list.py
class TodoList():
    def __init__(self):
        self.list_of_todos = []
        # self.complete = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.list_of_todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for i in self.list_of_todos:
            if list(i.todo_list.values()) == ([False]):
                incomplete_list.append(i)
        return incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = []
        for i in self.list_of_todos:
            if list(i.todo_list.values()) == ([True]):
                complete_list.append(i)
        return complete_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self.list_of_todos:
            for key, value in i.todo_list.items():
                if value == False:
                    i.todo_list.update({key : True})