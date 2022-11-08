#def estimated_reading_time(block of text)

#Parameters: (a single string, that represents the block of text)

#Returns: a string that shows an estimated time to read that block of text. 
#eg, ‘This block will take x minutes approx’). If we need to round - to 2 dec places

#Side effects: No other side effects desired

def divide_by(num):
    return num/200

def get_len(string1):
    lst = string1.split(" ")
    return len(lst)

def estimated_time(string1):
    length = get_len(string1)
    time = divide_by(length)
    return time

def estimated_reading_time(string1):
    return f"This will take you approximately {estimated_time(string1)} minutes to read."