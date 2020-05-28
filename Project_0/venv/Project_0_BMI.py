from tkinter import *
from tkinter import messagebox

bmi = Tk()
bmi.title('B M I')
bmi.resizable(0, 0)


class BodyMassIndex(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    def CalculateBMI(self):

        try:
            self.answer_output.delete(0, END)
            self.answer = float(self.weight_entry.get()) / float(self.height_entry.get()) / float(self.height_entry.get())
            self.answer_output.insert(0, self.answer)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number! ;)')
        finally:
            self.answer.delete(0, END)

    def create_widgets(self):

        # F I R S T  R O W

        self.weight = Label(self, text='Enter Your Weight In Kilos:')
        self.weight.grid(row=0, sticky=E)

        self.weight_entry = Entry(self)
        self.weight_entry.grid(row=0, column=1)

        # S E C O N D  R O W

        self.height = Label(self, text='Enter Your Height In Meters:')
        self.height.grid(row=1, sticky=E)

        self.height_entry = Entry(self)
        self.height_entry.grid(row=1, column=1)

        # T H I R D  R O W

        self.go_button = Button(self, text='GO', command=lambda: self.CalculateBMI())
        self.go_button.grid(row=2, column=0, columnspan=2, sticky=N + E + S + W)

        # F O U R T H  R O W

        self.bmi_answer_label = Label(self, text='Your BMI Is!')
        self.bmi_answer_label.grid(row=3, sticky=E)

        self.answer_output = Entry(self)
        self.answer_output.grid(row=3, column=1)


bmi_calculator = BodyMassIndex(bmi).grid()
bmi.mainloop()