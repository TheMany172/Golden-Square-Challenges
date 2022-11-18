def get_most_common_letter(text):
    counter = {}
    #print ("starting the for loop...")
    for char in text:
        #print (char)
        counter[char] = counter.get(char, 0) + 1
        #print (counter[char])
    #
    letters = sorted(counter.items(), key=lambda item: item[1], reverse = True)
    #print (letter)
    #return letter
    for letter in letters:
        for most_common in letter:
            print (most_common)
            if str(most_common).isalpha():
                return most_common



print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")