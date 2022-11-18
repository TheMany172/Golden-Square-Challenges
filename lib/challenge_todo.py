class Todo():
    def __init__(self):
        self.todo_list = []

    def add_todo_item(self, string1):
        self.todo_list.append(string1)

    def return_whole_list(self):
        return self.todo_list

