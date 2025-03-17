import tkinter as tk
import datetime as dt
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from utils import Utils


class About(tk.Toplevel):
	""" About popup widow to display Bingo general application description """
	def __init__(self, master):
		super().__init__(master)
		self.transient(master)		# make the window transient(transitorio)
		self.grab_set()				# make the window modal
		self.title('Super Family Bingo')
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.close)
		self.utils = Utils()
		self.focus_set()

		# main notebook
		self.nb_about = ttk.Notebook(self)
		self.nb_about.pack(side=tk.TOP, padx=5)

		# frame for information tab
		self.tab_info = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_info, text='Information')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)

		self.img_about = tk.PhotoImage(file='res/bingo.png')
		ttk.Label(self.tab_info, image=self.img_about).pack(side=tk.TOP, pady=30)

		self.lbl_title_info = ttk.Label(self.tab_info, text='Super Family Bingo 1.0.0')
		self.lbl_title_info.pack(side=tk.TOP)
		self.lbl_title_info.configure(font=('Helvatica', 20, 'bold'))

		txt_sys = self.utils.platform_system_desc()  							  # get OS description
		txt_lang = '\nPython {}'.format(self.utils.get_python_version_string())   # get Python version
		# txt_lib = '\nTk {}'. format(self.utils.get_tk_version_str())
		txt_lib = '\nTk {}'.format(self.tk.call('info', 'patchlevel'))			  # get Tk version
		self.lbl_sys = ttk.Label(self.tab_info, justify=tk.CENTER, text='{} {} {}'.format(txt_sys, txt_lang, txt_lib))
		self.lbl_sys.pack(side=tk.TOP, pady=30)
		self.lbl_sys.configure(font=('Helvatica', 10))

		current_year = dt.datetime.now().year
		txt_year = f'Copyright (c) 2019-{current_year}' 
		txt_all = '\n@All rights reserved'
		self.lbl_info_year = ttk.Label(self.tab_info, justify=tk.CENTER, text='{} {}'.format(txt_year, txt_all))
		self.lbl_info_year.pack(side=tk.TOP)
		self.lbl_info_year.configure(font=('Helvatica', 10))
		txt_name = 'Jose De La Cruz'
		self.lbl_info_name = ttk.Label(self.tab_info, text=txt_name, justify=tk.CENTER)
		self.lbl_info_name.pack(side=tk.TOP)
		self.lbl_info_name.configure(foreground='blue', font=('Helvatica', 10))

		# frame for credit tab
		self.tab_credit = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_credit, text='Credits')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)
		
		self.lbl_title_credit = ttk.Label(self.tab_credit, text='Developers')
		self.lbl_title_credit.pack(padx=20, pady=30)
		self.lbl_title_credit.configure(font=('Calibri', 26, 'bold'))

		self.lbl_name_credit1 = ttk.Label(self.tab_credit, text='Jose De La Cruz')
		self.lbl_name_credit1.pack()
		self.lbl_name_credit1.configure(font=('Verdana', 11))
		self.lbl_email_credit1 = ttk.Label(self.tab_credit, text='jldlcv@gmail.com')
		self.lbl_email_credit1.pack()
		self.lbl_email_credit1.configure(foreground='blue', font=('Verdana', 10, 'underline'))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit2 = ttk.Label(self.tab_credit, text='Luis Castillo')
		self.lbl_name_credit2.pack()
		self.lbl_name_credit2.configure(font=('Verdana', 11))
		self.lbl_email_credit2 = ttk.Label(self.tab_credit, text='lcastillovillena@gmail.com')
		self.lbl_email_credit2.pack()
		self.lbl_email_credit2.configure(foreground='blue', font=('Verdana', 10, 'underline'))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit3 = ttk.Label(self.tab_credit, text='Gloria Sánchez')
		self.lbl_name_credit3.pack()
		self.lbl_name_credit3.configure(font=('Verdana', 11))
		self.lbl_email_credit3 = ttk.Label(self.tab_credit, text='glorypaty247@gmail.com')
		self.lbl_email_credit3.pack()
		self.lbl_email_credit3.configure(foreground='blue', font=('Verdana', 10, 'underline'))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit4 = ttk.Label(self.tab_credit, text='Stefano De La Cruz')
		self.lbl_name_credit4.pack()
		self.lbl_name_credit4.configure(font=('Verdana', 11))
		self.lbl_email_credit4 = ttk.Label(self.tab_credit, text='delacruzstefano27@gmail.com')
		self.lbl_email_credit4.pack()
		self.lbl_email_credit4.configure(foreground='blue', font=('Verdana', 10, 'underline'))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit4 = ttk.Label(self.tab_credit, text='Nestor Silva')
		self.lbl_name_credit4.pack()
		self.lbl_name_credit4.configure(font=('Verdana', 11))
		self.lbl_email_credit4 = ttk.Label(self.tab_credit, text='nestor.silva@gmail.com')
		self.lbl_email_credit4.pack()
		self.lbl_email_credit4.configure(foreground='blue', font=('Verdana', 10, 'underline'))

		# frame for license tab
		self.tab_license = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_license, text='License')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)

		self.txt_license = ScrolledText(self.tab_license, undo=True, wrap=tk.WORD, height=27) # width=80
		self.txt_license.pack(side=tk.LEFT)
		self.txt_license.insert('1.0', self.utils.open_text_file('res/license.txt'))
		# make text widget 'read-only'
		self.txt_license.configure(state=tk.DISABLED)

		# close button with image
		self.img_close = tk.PhotoImage(file='res/close.gif')
		tk.Button(
			self, 
			text='Close', 
			image=self.img_close, 
			compound=tk.LEFT, 
			command=self.close
		).pack(side=tk.RIGHT, padx=5, pady=5)


	def close(self):
		""" Close window """
		self.master.focus_set()
		self.destroy()