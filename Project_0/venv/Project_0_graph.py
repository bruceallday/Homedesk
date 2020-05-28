import datetime
#from six.moves import tkinter as Tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import numpy as np

root = Tk()
root.title ('Project_0')
menu = Menu(root)



# CREAING THE TOP MENU BAR
root.config(menu=menu)
submenu = Menu(menu)


# a cascade is a drop down menu)
menu.add_cascade(label='Shop', menu=submenu)


# adding the "nothing command to the drop down items
submenu.add_command(label='Depop')
submenu.add_command(label='Ebay')


# Creating a separator line
submenu.add_separator()


# Making the exit label "do nothing"
submenu.add_command(label='Exit')
calculator_menu = Menu(menu)
# CALCULATOR CASCADE


menu.add_cascade(label='Calculator', menu=calculator_menu)
calculator_menu.add_command(label='Open')  #command=Calculator)
conversion_menu = Menu(menu)


# CONVERSIONS CASCADE
menu.add_cascade(label='Conversions', menu=conversion_menu)
conversion_menu.add_command(label='Body Mass Index')
conversion_menu.add_command(label='Currency')
conversion_menu.add_command(label='Distance')
conversion_menu.add_command(label='Height')
conversion_menu.add_command(label='Kilopascals')
conversion_menu.add_command(label='Time')
conversion_menu.add_command(label='Temperature')


class Depop_Graph(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()



    def create_widgets(self):

        self.new_date = datetime.datetime(2017, 12, 3)
        self.price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        self.date = [self.new_date + datetime.timedelta(weeks=i) for i in range(len(self.price))]

        self.graph = Figure(figsize=(11, 4), dpi=100)
        self.graph.add_subplot(111).plot(self.date, self.price, color= 'c', label='£')
        self.graph.legend()
        self.graph.autofmt_xdate()

        self.canvas = FigureCanvasTkAgg(self.graph, master=root)  # A tk.DrawingArea.
        self.graph.canvas.draw()
        self.graph.canvas.get_tk_widget().pack(side=TOP)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, root)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP)

        self.button = Button(master=root, text="Quit", command=quit)
        self.button.pack(side=RIGHT)

        self.button2 = Button(master=root, text='Toolbar', command=quit)
        self.button2.pack(side=RIGHT)

    def _quit(self):
        self.root.quit()
        self.root.destroy()

depopgraph = Depop_Graph(root).pack()
root.mainloop()
