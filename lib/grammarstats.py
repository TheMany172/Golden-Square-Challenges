class GrammarStats():
    def __init__(self):
        self.count_good = 0
        self.count_all = 0
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text[-1] in ('!?.'):
            self.count_good += 1 
            self.count_all += 1
            return True
        else:
            self.count_all += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.count_all == 0:
            return "you've not checked anything - moron."
        else:
            return (self.count_good / self.count_all) * 100
