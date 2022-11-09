'''
1. function name will be check_todo
2. 1 argument which will be a string
3. Return a boolean - return True if #TODO exists, otherwise return False
4. No side effects
'''

def todo_check(string1):
    if "#TODO" in string1:
        return True
    else:
        return False