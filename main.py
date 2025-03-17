from bingo import Bingo
from gui import Gui
from utils import Utils


class Main:
    """ Class that works as the application controller """
    def __init__(self):
        self.utils = Utils()
        self.bingo = Bingo()
        self.gui = Gui(self)


    def call_get_item(self):
        """ Call method Bingo class """
        return self.bingo.get_first_item()


    def call_get_letter(self):
        """ Call method Bingo class """
        return self.bingo.get_letter_item()


    def open_text_file(self, filename):
        """ Call method Utils class """
        return self.utils.open_text_file(filename)


    def main_gui(self):
        """ Call method Gui class """
        self.gui.start_mainloop()


if __name__ == '__main__':
    main = Main()
    main.main_gui()