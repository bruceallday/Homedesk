from tkinter import *
from tkinter import messagebox

height = Tk()
height.title('H E I G H T')
height.resizable(0, 0)


class HeightConverter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()


    # C O N V E R S I O N   F U N C T I O N S

    # I N C H E S

    def inches_inches(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get())
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.height_input.delete(0, END)

    def inches_feet(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.8333
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.height_input.delete(0, END)

    def inches_cm(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 2.54
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.height_input.delete(0, END)

    def inches_meters(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.0254
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    # F E E T

    def feet_feet(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get())
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'that is not a number')
            self.height_input.delete(0, END)

    def feet_inches(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 12
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    def feet_cm(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 30.48
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    def feet_meters(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.3048
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    # C E N T I M E T R E

    def cm_cm(self):
        try:
            self.height_out.delete(0, END)
            self.converted_height = int(self.height_input.get())
            self.height_output.inserr(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    def cm_inches(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.393701
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.height_input.delete(0, END)

    def cm_feet(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.0328084
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'Thats is not a number')
            self.height_input.delete(0, END)

    def cm_meters(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 0.01
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    # M E T E R S

    def meter_meter(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get())
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    def meter_inches(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 39.3701
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    def meter_feet(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 3.28084
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.height_input.delete(0, END)

    def meter_cm(self):
        try:
            self.height_output.delete(0, END)
            self.converted_height = int(self.height_input.get()) * 100
            self.height_output.insert(0, self.converted_height)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number')
            self.height_input.delete(0, END)

    # C H E C K I N G  F O R  C O R E S P O N D I N G  H E I G H T

    def convert_h(self):
        if self.from_height.get() == 'Inches' and self.to_height.get() == 'Inches':
            self.inches_inches()
        elif self.from_height.get() == 'Inches' and self.to_height.get() == 'Feet':
            self.inches_feet()
        elif self.from_height.get() == 'Inches' and self.to_height.get() == 'Cm':
            self.inches_cm()
        elif self.from_height.get() == 'Inches' and self.to_height.get() == 'Meters':
            self.inches_meters()

        elif self.from_height.get() == 'Feet' and self.to_height.get() == 'Feet':
            self.feet_feet()
        elif self.from_height.get() == 'Feet' and self.to_height.get() == 'Inches':
            self.feet_inches()
        elif self.from_height.get() == 'Feet' and self.to_height.get() == 'Cm':
            self.feet_cm()
        elif self.from_height.get() == 'Feet' and self.to_height.get() == 'Meters':
            self.feet_meters()

        elif self.from_height.get() == 'Cm' and self.to_height.get() == 'Cm':
            self.cm_cm()
        elif self.from_height.get() == 'Cm' and self.to_height.get() == 'Inches':
            self.cm_inches()
        elif self.from_height.get() == 'Cm' and self.to_height.get() == 'Feet':
            self.cm_feet()
        elif self.from_height.get() == 'Cm' and self.to_height.get() == 'Meters':
            self.cm_meters()

        elif self.from_height.get() == 'Meters' and self.to_height.get() == 'Meters':
            self.meter_meter()
        elif self.from_height.get() == 'Meters' and self.to_height.get() == 'Inches':
            self.meter_inches()
        elif self.from_height.get() == 'Meters' and self.to_height.get() == 'Feet':
            self.meter_feet()
        elif self.from_height.get() == 'Meters' and self.to_height.get() == 'Cm':
            self.meter_cm()

    # C R E A T I N G T H E  G U I  I N T E R F A C E

    def create_widgets(self):

        # F I R S T  R O W

        self.from_label = Label(self, text='From:')
        self.from_label.grid(row=0, sticky=E)

        self.from_height = StringVar(self)
        self.from_height.set('Inches')

        self.height_from_selection = OptionMenu(self, self.from_height, 'Inches', 'Feet', 'Cm', 'Meters')
        self.height_from_selection.grid(row=0, column=1, sticky=N + S + E + W)

        self.height_input = Entry(self)
        self.height_input.grid(row=0, column=2)

        # S E C O N D  R O W

        self.to_label = Label(self, text='To:')
        self.to_label.grid(row=1, sticky=E)

        self.to_height = StringVar(self)
        self.to_height.set('Feet')

        self.height_to_selection = OptionMenu(self, self.to_height, 'Inches', 'Feet', 'Cm', 'Meters')
        self.height_to_selection.grid(row=1, column=1, sticky=N + S + E + W)

        self.height_output = Entry(self)
        self.height_output.grid(row=1, column=2)

        # T H I R D  R O W

        self.go_button = Button(self, text='Go', command=lambda: self.convert_h())
        self.go_button.grid(row=2, column=0, columnspan=3, sticky=N + S + E + W)


height_converter = HeightConverter(height).grid()
height.mainloop()