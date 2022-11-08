def count_words(string1):
    if isinstance(string1, str) == False:
        raise Exception("This is not a string!")
    if string1 == "":
        return 0
    return len(string1.split(" "))