import os
import tkinter as tk
from tkinter import ttk, messagebox
from about import About
from gtts import gTTS 
from playsound3 import playsound


class Gui(tk.Tk):
    """ Class that works as the application view """
    def __init__(self, main):
        super().__init__()

        # check platform (SO) & set zoom status
        platform = self.tk.call('tk', 'windowingsystem')
        self.wm_state('zoomed') if platform == 'win32' else self.attributes('-zoomed', 1)
        
        # add title to application
        self.title('Super Family Bingo')

        # add icon to application
        self.iconphoto(True, tk.PhotoImage(file='res/bingo.png'))

        # close window with the 'X' button
        self.protocol("WM_DELETE_WINDOW", self.exit_app)

        # background
        self.config(bg='gray14')
        
        # communicates with the main.py
        self.main = main

        # header title frame
        self.frm_title = tk.Frame(self, bg='gray20')
        self.frm_title.pack(side=tk.TOP, fill=tk.X)
        tk.Label(self.frm_title, text='CONTROL PANEL', bg='gray20', 
            fg='white', font=('Consola', 35, 'bold')).pack(pady=10)

        # bingo matrix frame
        self.frm_array = tk.Frame(self, bg='gray14')
        self.frm_array.pack(side=tk.LEFT, fill=tk.Y, padx=70, pady=25)

        # add letters to matrix frame
        tk.Label(self.frm_array, text='B', bg='gray14', fg='yellow',
            font=('Consola', 50, 'bold')).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.frm_array, text='I', bg='gray14', fg='yellow',
            font=('Consola', 50, 'bold')).grid(row=1, column=0, padx=5, pady=5)

        tk.Label(self.frm_array, text='N', bg='gray14', fg='yellow',
            font=('Consola', 50, 'bold')).grid(row=2, column=0, padx=5, pady=5)
        
        tk.Label(self.frm_array, text='G', bg='gray14', fg='yellow',
            font=('Consola', 50, 'bold')).grid(row=3, column=0, padx=5, pady=5)
        
        tk.Label(self.frm_array, text='O', bg='gray14', fg='yellow',
            font=('Consola', 50, 'bold')).grid(row=4, column=0, padx=5, pady=5)

        # game counter variables
        self.ini = 0
        self.fin = 75

        # dictionary that stores number and generated label as key:value
        self.lbl = {}

        # add labels(numbers) to matrix frame
        self.row_x = 0
        self.col_y = 1
        for i in range(1, 76):
            self.lbl[i] = tk.Label(self.frm_array, text=i, bg='gray14', fg='white', font=('Consola', 30, 'bold')) 
            self.lbl[i].grid(row=self.row_x, column=self.col_y, padx=5, pady=30)
            self.col_y += 1
            if self.col_y == 16:
                self.row_x += 1
                self.col_y = 1

        # bar separator
        ttk.Separator(self, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, pady=25)

        # operation buttons frame
        self.frm_operations = tk.Frame(self, bg='gray14')
        self.frm_operations.pack(side=tk.LEFT, fill=tk.Y, padx=60, pady=25)

        # number of moves
        self.lbl_exit_number = tk.Label(self.frm_operations, text='PLAYS: 0/75', bg='gray14', 
            fg='white', font=('Consola', 12, 'bold'))
        self.lbl_exit_number.grid(row=0, column=0, pady=25)

        # bingo letter 
        self.lbl_letter = tk.Label(self.frm_operations, text='?', bg='gray14', fg='yellow',
            font=('Consola', 70, 'bold'))
        self.lbl_letter.grid(row=1, column=0)
        
        # bingo number
        self.lbl_number = tk.Label(self.frm_operations, text='?', bg='gray14', fg='yellow',
            font=('Consola', 70, 'bold'))
        self.lbl_number.grid(row=2, column=0)

        # play button
        self.btn_play = tk.Button(self.frm_operations, text='[ PLAY ]', width=12, bg='black', 
            fg='white', font='bold', command=self.play_bingo)
        self.btn_play.grid(row=3, column=0, pady=15)
        self.btn_play.focus()

        # reset button
        tk.Button(self.frm_operations, text='[ RESET ]', width=12, bg='green', fg='white', 
            font='bold', command=self.reset_play).grid(row=4, column=0, pady=15)

        # about button
        tk.Button(self.frm_operations, text='[ ABOUT ]', width=12, bg='blue', fg='white', 
            font='bold', command=self.window_about).grid(row=5, column=0)

        # exit button
        tk.Button(self.frm_operations, text='[ EXIT ]', width=12, bg='purple', fg='white', 
            font='bold', command=self.exit_app).grid(row=6, column=0, pady=15)

  
    def play_counter(self):
        """ Show play counter """
        self.ini += 1
        self.fin -= 1
        self.lbl_exit_number['text'] = 'PLAYS: {}/{}'.format(self.ini, self.fin)
        if self.ini == 75:
            self.btn_play.configure(state=tk.DISABLED)

  
    def change_foreground(self):
        """ Change text color of labels(numbers) """
        for i in range(1, 76):
            if self.lbl_number['text'] == i:
                self.lbl[i].configure(fg='yellow')

  
    def text_to_speech(self):
        """ Convert text to speech """
        text_all = self.lbl_letter['text'] + str(self.lbl_number['text'])
        tts = gTTS(text=text_all, lang='es-es')
        tts.save('res/output.mp3')
        playsound('res/output.mp3')
        os.remove('res/output.mp3')


    def play_bingo(self):
        """ Click button [ PLAY ] """
        self.lbl_number['text'] = self.main.call_get_item()
        self.lbl_letter['text'] = self.main.call_get_letter()
        self.play_counter()
        self.change_foreground()
        self.text_to_speech()


    def reset_play(self):
        """ Restart game """
        value = messagebox.askquestion('Super Family Bingo', 'Do you want to play again?')
        if value == 'yes':
            self.destroy()
            os.system('python "main.py"')
            #os.system('main.pyw')


    def window_about(self):
        """ Shows about window """
        About(self)


    def exit_app(self):
        """ Exit Bingo """
        value = messagebox.askquestion('Super Family Bingo', 'Do you want to exit?')
        if value == 'yes':
            self.destroy()


    def start_mainloop(self):
        """ Run the main window loop """
        self.mainloop()
