def make_snippet(string1):
    if isinstance(string1, str) == False:
        raise Exception("This is not a string!")
    else:
        lst = string1.split(" ")
        if len(lst) > 5:
            return ' '.join(lst[0:5]) + "..."
        return string1