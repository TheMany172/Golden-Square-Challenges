# File: lib/todo.py
class Todo():
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        self.task = task
        self.todo_list = {}
        self.todo_list.update({self.task : False})

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        for key, value in self.todo_list.items():
            if value == False:
                self.todo_list.update({key : True})