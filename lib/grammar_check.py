
def check_first_character(string1):
    if string1[0] == string1[0].upper():
        return True
    return False

def check_punctuation_mark(string1):
    if string1[-1] in (".?!"):
        return True
    return False
    

def grammar_check(string1):
    if check_punctuation_mark(string1) and check_first_character(string1):
        return "Well done you have used correct punctuation and grammar!"
    elif check_punctuation_mark(string1) == False and check_first_character(string1):
        return "Sorry, you missed the punctuation mark."
    elif check_punctuation_mark(string1) and check_first_character(string1) == False:
        return "Sorry, you missed the capital letter."
    else:
        return "duz yoo evans grammair%"



