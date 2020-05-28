from tkinter import *
from tkinter import messagebox

time = Tk()
time.title('T I M E')
time.resizable(0, 0)


class TimeConverter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    # C O N V E R S I O N  F U N C T I O N S

    # S E C O N D S

    def SEC_SEC(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get())
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def SEC_MIN(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.0166667
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def SEC_HOUR(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.000277778
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def SEC_DAY(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.0000115741
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    # M I N U T E S

    def MIN_MIN(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get())
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def MIN_SEC(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 60
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def MIN_HOUR(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.0166667
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def MIN_DAY(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.000694444
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    # H O U R S

    def HOUR_HOUR(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get())
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def HOUR_SEC(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 3600
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def HOUR_MIN(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 60
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def HOUR_DAY(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 0.0416667
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    # D A Y S

    def DAY_DAY(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get())
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def DAY_SEC(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 86400
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def DAY_MIN(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 1440
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    def DAY_HOUR(self):
        try:
            self.time_output.delete(0, END)
            self.converted_time = float(self.time_input.get()) * 24
            self.time_output.insert(0, self.converted_time)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.time_input.delete(0, END)

    # C H E C K I N G  F O R  C O R R E S P O N D I N G  T I M E

    def convert_time(self):

        # S E C O N D S

        if self.from_time.get() == 'Seconds' and self.to_time.get() == 'Seconds':
            self.SEC_SEC()
        elif self.from_time.get() == 'Seconds' and self.to_time.get() == 'Minutes':
            self.SEC_MIN()
        elif self.from_time.get() == 'Seconds' and self.to_time.get() == 'Hours':
            self.SEC_HOUR()
        elif self.from_time.get() == 'Seconds' and self.to_time.get() == 'Days':
            self.SEC_DAY()

        # M I N U T E S

        if self.from_time.get() == 'Minutes' and self.to_time.get() == 'Seconds':
            self.MIN_SEC()
        elif self.from_time.get() == 'Minutes' and self.to_time.get() == 'Minutes':
            self.MIN_MIN()
        elif self.from_time.get() == 'Minutes' and self.to_time.get() == 'Hours':
            self.MIN_HOUR()
        elif self.from_time.get() == 'Minutes' and self.to_time.get() == 'Days':
            self.MIN_DAY()

        # H O U R S

        if self.from_time.get() == 'Hours' and self.to_time.get() == 'Seconds':
            self.HOUR_SEC()
        elif self.from_time.get() == 'Hours' and self.to_time.get() == 'Minutes':
            self.HOUR_MIN()
        elif self.from_time.get() == 'Hours' and self.to_time.get() == 'Hours':
            self.HOUR_HOUR()
        elif self.from_time.get() == 'Hours' and self.to_time.get() == 'Days':
            self.HOUR_DAY()

        # D A Y S

        if self.from_time.get() == 'Days' and self.to_time.get() == 'Seconds':
            self.DAY_SEC()
        elif self.from_time.get() == 'Days' and self.to_time.get() == 'Minutes':
            self.DAY_MIN()
        elif self.from_time.get() == 'Days' and self.to_time.get() == 'Hours':
            self.DAY_HOUR()
        elif self.from_time.get() == 'Days' and self.to_time.get() == 'Days':
            self.DAY_DAY()

    def create_widgets(self):

        # F I R S T  R O W

        self.from_label = Label(self, text='From:')
        self.from_label.grid(row=0, sticky=E)

        self.from_time = StringVar(self)
        self.from_time.set('Seconds')

        self.time_from_selection = OptionMenu(self, self.from_time, 'Seconds', 'Minutes', 'Hours', 'Days')
        self.time_from_selection.grid(row=0, column=1, sticky=N + S + E + W)

        self.time_input = Entry(self)
        self.time_input.grid(row=0, column=2)

        # S E C O N D  R O W

        self.to_label = Label(self, text='To:')
        self.to_label.grid(row=1, sticky=E)

        self.to_time = StringVar(self)
        self.to_time.set('Minutes')

        self.time_to_selection = OptionMenu(self, self.to_time, 'Seconds', 'Minutes', 'Hours', 'Days')
        self.time_to_selection.grid(row=1, column=1, sticky=N + S + E + W)

        self.time_output = Entry(self)
        self.time_output.grid(row=1, column=2)

        # T H I R D R O W
        self.go_button = Button(self, text='Go', command=lambda: self.convert_time())
        self.go_button.grid(row=2, column=0, columnspan=3, sticky=N + S + E + W)


time_converter = TimeConverter(time).grid()
time.mainloop()