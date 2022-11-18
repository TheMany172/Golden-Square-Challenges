# File: lib/todo_list.py
class TodoList():
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incompletes = []
        for todo in self.todo_list:
            if todo.task_status != True:
                incompletes.append(todo)
        return incompletes

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        completes = []
        for todo in self.todo_list:
            if todo.task_status == True:
                completes.append(todo)
        return completes

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        if self.incomplete() == []:
            raise Exception("All tasks are already complete")

        for todo in self.todo_list:

            if todo.task_status == False:
                todo.task_status = True


