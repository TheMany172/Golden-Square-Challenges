class Todo_Tracker():
    def __init__(self):
        self.todo_list = []

    def add(self, str1):
        self.todo_list.append(str1)

    def return_all(self):
        return self.todo_list

    def mark_complete(self, task_to_remove):
        if task_to_remove in self.todo_list:
            self.todo_list.remove(task_to_remove)
        else:
            raise Exception("This task does not exist :-(")