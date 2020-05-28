from tkinter import *
from tkinter import messagebox

temp = Tk()
temp.title('T E M P E R A T U R E')
temp.resizable(0, 0)


class TempConverter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()


    # C E L S I U S

    def C_C(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get())
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def C_F(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) * 1.8 + 32
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def C_K(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) + 273.15
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

            # F A H R E N H E I T

    def F_F(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get())
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def F_C(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) - 32
            self.converted_temp = self.converted_temp * 5 / 9
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def F_K(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) + 459.67
            self.converted_temp = self.converted_temp * 5 / 9
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

        # K E L V I N

    def K_K(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get())
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def K_C(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) - 273.15
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    def K_F(self):
        try:
            self.temp_output.delete(0, END)
            self.converted_temp = int(self.temp_input.get()) * 9 / 5 - 459.67
            self.temp_output.insert(0, self.converted_temp)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.temp_input.delete(0, END)

    # C H E C K I N G  F O R  C O R E S P O N D I N G  T E M P

    def convert_t(self):
        if self.from_temp.get() == 'Celsius' and self.to_temp.get() == 'Celsius':
            self.C_C()
        elif self.from_temp.get() == 'Celsius' and self.to_temp.get() == 'Fahrenheit':
            self.C_F()
        elif self.from_temp.get() == 'Celsius' and self.to_temp.get() == 'Kelvin':
            self.C_K()

        if self.from_temp.get() == 'Fahrenheit' and self.to_temp.get() == 'Celsius':
            self.F_C()
        elif self.from_temp.get() == 'Fahrenheit' and self.to_temp.get() == 'Fahrenheit':
            self.F_F()
        elif self.from_temp.get() == 'Fahrenheit' and self.to_temp.get() == 'Kelvin':
            self.F_K()

        if self.from_temp.get() == 'Kelvin' and self.to_temp.get() == 'Celsius':
            self.K_C()
        elif self.from_temp.get() == 'Kelvin' and self.to_temp.get() == 'Fahrenheit':
            self.K_F()
        elif self.from_temp.get() == 'Kelvin' and self.to_temp.get() == 'Kelvin':
            self.K_K()

    # B U I L D I N G  G U I  I N T E R F A C E

    def create_widgets(self):

        # F I R S T  R O W

        self.from_label = Label(self, text='From:')
        self.from_label.grid(row=0, sticky=E)

        self.from_temp = StringVar(self)
        self.from_temp.set('Celsius')

        self.from_temp_selection = OptionMenu(self, self.from_temp, 'Celsius', 'Fahrenheit', 'Kelvin')
        self.from_temp_selection.grid(row=0, column=1, sticky=N + S + E + W)

        self.temp_input = Entry(self)
        self.temp_input.grid(row=0, column=2)

        # S E C O N D  R O W

        self.to_label = Label(self, text='To:')
        self.to_label.grid(row=1, sticky=E)

        self.to_temp = StringVar(self)
        self.to_temp.set('Fahrenheit')

        self.to_temp_selection = OptionMenu(self, self.to_temp, 'Celsius', 'Fahrenheit', 'Kelvin')
        self.to_temp_selection.grid(row=1, column=1, sticky=N + S + E + W)

        self.temp_output = Entry(self)
        self.temp_output.grid(row=1, column=2)

        # T H I R D  R O W
        self.go_button = Button(self, text='Go', command=lambda: self.convert_t())
        self.go_button.grid(row=2, column=0, columnspan=3, sticky=N + S + E + W)


temp_converter = TempConverter(temp).grid()
temp.mainloop()