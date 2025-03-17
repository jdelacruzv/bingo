import random


class Bingo:
    """ Class Bingo. Works as the application model """
    def __init__(self):
        self.first_item = 0
        # create list
        self.list_init = []
        # add items to list
        for i in range(1, 76):
            self.list_init.append(i)
        # shuffle(barajar) list
        random.shuffle(self.list_init)


    def get_first_item(self):
        """ Get first item in list """
        # get first item
        self.first_item = self.list_init[0]
        self.get_letter_item()
        # remove item obtained
        self.list_init.pop(0)
        return self.first_item


    def get_letter_item(self):
        """ Get letter from list item """
        letter = ''
        if 1 <= self.first_item <= 15:
            letter = 'B'
        if 16 <= self.first_item <= 30:
            letter = 'I'
        if 31 <= self.first_item <= 45:
            letter = 'N'
        if 46 <= self.first_item <= 60:
            letter = 'G'
        if 61 <= self.first_item <= 75:
            letter = 'O'
        return letter
