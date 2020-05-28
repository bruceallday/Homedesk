from tkinter import *
from tkinter import messagebox

distance = Tk()
distance.title("D I S T A N C E")
distance.resizable(0, 0)


class DistanceConverter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    # D I S T A N C E  C O N V E R S I O N  F U N C T I O N S

    # M E T E R S

    def Meters_Meters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get())
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number")
            self.distance_input.delete(0, END)

    def Meters_Kilometers(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 0.001
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def Meters_Miles(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 0.000621371
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def Meters_LightYears(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 0.00000000000000010570, ('...')
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    # K I L O M E T E R S

    def KiloMeters_KiloMeters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get())
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def KiloMeters_Meters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1000
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def KiloMeters_Miles(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1.069
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def KiloMeters_LightYears(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 0.00000000000000010570, ('...')
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    # M I L E S

    def Miles_miles(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get())
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def Miles_Meters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1609.34
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def Miles_KiloMeters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1.069
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def Miles_LightYears(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1609.34 * 0.000000000000106, ("...")
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    # L I G H T  Y E A R S

    def lightyears_lightyears(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get())
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def lightyears_Meters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 9460730472580800.00, ('...')
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def lightyears_KiloMeters(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1000 * 9460730472580800
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    def LightYears_miles(self):
        try:
            self.distance_output.delete(0, END)
            self.converted_distance = float(self.distance_input.get()) * 1.069 * 9460730472580800, ("...")
            self.distance_output.insert(0, self.converted_distance)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.distance_input.delete(0, END)

    # C H E C K I N G  F O R  C O R E S P O N D I N G  D I S T A N C E

    def convert_dis(self):
        if self.from_distance.get() == 'Meters' and self.to_distance.get() == 'Meters':
            self.Meters_Meters()
        elif self.from_distance.get() == 'Meters' and self.to_distance.get() == 'Kilometers':
            self.Meters_Kilometers()
        elif self.from_distance.get() == 'Meters' and self.to_distance.get() == 'Miles':
            self.Meters_Miles()
        elif self.from_distance.get() == 'Meters' and self.to_distance.get() == 'Light Years':
            self.Meters_LightYears()

        elif self.from_distance.get() == 'Kilometers' and self.to_distance.get() == 'Kilometers':
            self.KiloMeters_KiloMeters()
        elif self.from_distance.get() == 'Kilometers' and self.to_distance.get() == 'Meters':
            self.KiloMeters_Meters()
        elif self.from_distance.get() == 'Kilometers' and self.to_distance.get() == 'Miles':
            self.KiloMeters_Miles()
        elif self.from_distance.get() == 'Kilometers' and self.to_distance.get() == 'Light Years':
            self.KiloMeters_LightYears()

        elif self.from_distance.get() == 'Miles' and self.to_distance.get() == 'Miles':
            self.Miles_miles()
        elif self.from_distance.get() == 'Miles' and self.to_distance.get() == 'Meters':
            self.Miles_Meters()
        elif self.from_distance.get() == 'Miles' and self.to_distance.get() == 'Kilometers':
            self.Miles_KiloMeters()
        elif self.from_distance.get() == 'Miles' and self.to_distance.get() == 'Light Years':
            self.Miles_LightYears()

        elif self.from_distance.get() == 'Light Years' and self.to_distance.get() == 'Light Years':
            self.lightyears_lightyears()
        elif self.from_distance.get() == 'Light Years' and self.to_distance.get() == 'Meters':
            self.lightyears_Meters()
        elif self.from_distance.get() == 'Light Years' and self.to_distance.get() == 'Kilometers':
            self.lightyears_KiloMeters()
        elif self.from_distance.get() == 'Light Years' and self.to_distance.get() == 'Miles':
            self.LightYears_miles()

    # C R E A T I N G  T H E  G U I  I N T E R F A C E

    def create_widgets(self):

        # F I R S T  R O W

        self.from_label = Label(self, text="From: ")
        self.from_label.grid(row=0, sticky=E)

        self.from_distance = StringVar(self)
        self.from_distance.set("Meters")

        self.distance_from_selection = OptionMenu(self, self.from_distance, 'Meters', 'Kilometers', 'Miles', 'Light Years')
        self.distance_from_selection.grid(row=0, column=1, sticky=N + E + S + W)

        self.distance_input = Entry(self)
        self.distance_input.grid(row=0, column=2)

        # S E C O N D  R O W

        self.to_label = Label(self, text="To: ")
        self.to_label.grid(row=1, sticky=E)

        self.to_distance = StringVar(self)
        self.to_distance.set("Kilometers")

        self.distance_to_selection = OptionMenu(self, self.to_distance, 'Meters', 'Kilometers', 'Miles', 'Light Years')
        self.distance_to_selection.grid(row=1, column=1, sticky=N + E + S + W)

        self.distance_output = Entry(self)
        self.distance_output.grid(row=1, column=2)

        # T H I R D  R O W

        self.go_button = Button(self, text='Go', command=lambda: self.convert_dis())
        self.go_button.grid(row=2, column=0, columnspan=3, sticky=N + E + S + W)


distance_converter = DistanceConverter(distance).grid()
distance.mainloop()



