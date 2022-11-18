from lib.challenge_diaryentry import *
# # Diary class
class Diary():
    def __init__(self):
        self.entry_list = []
    
# No needed arguments - will want a list or something to store the entries

    def add_entry(self, diary_entry):
        self.entry_list.append(diary_entry)


# def diary_entries(self):
# -takes none
# - should return all of our diary entries - as a list

    def select_best_entry_to_read(self, wpm, time):
        words_can_read = wpm * time 
        readable_entries = []
        for object_in_diary in self.entry_list:
            if len(object_in_diary.formatted.split(' ')) <= words_can_read:
                readable_entries.append(object_in_diary)
        return readable_entries


    def find_mobile_phone(self):
        numbers = []
        print("LOOK HERE PLEASE")
        working_string = ''
        for item_in_list in self.entry_list:
            working_string += (f" {item_in_list.formatted}")
        new_list = working_string.split(' ')
        for i in new_list:
            if i == '':
                pass
            elif i[0] == '0' and len(i) == 11 and i.isnumeric():
                numbers.append(i)
        return numbers 

            
        print(new_list)
            #for i in working_string:
             #   print(i)
                #if i[0] == '0' and len(i) == 11:
                    # numbers.append(i)
        print(working_string)
        #splitting = self.entry_list.formatted.split(' ')
      #  mystring = ' '.join(map(str, self.entry_list.formatted))
       # print(mystring)

        # for list_item in self.entry_list:
        #     for i in list_item.formatted.split(' ') 
                #if i[0] == '0' and len(i) == 11:
        #       if i[] == '0' and len(list_item.formatted) == 11:
        #         numbers.append(list_item)


        # for i in splitting:
        #     if i[0] == '0' and len(i) == 11:
        #         numbers.append(i)
        # return numbers

# - takes nothing
# - should return a list - of the numbers - in all entries
