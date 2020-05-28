from tkinter import *
from tkinter import messagebox

currency = Tk()
currency.title('C U R R E N C Y')
currency.resizable(0, 0)


class CurrencyConverter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()


    # C U R R E N C Y  C O N V E R S I O N  F U N C T I O N S

    # G B P

    def GBP_GBP(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get())
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', "That's not a number!")
            self.currency_from.delete(0, END)

    def GBP_USD(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 1.4635
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def GBP_EURO(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 1.14
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def GBP_YEN(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 105.79
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    # U S D

    def USD_USD(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get())
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def USD_GBP(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.72
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def USD_EURO(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.81
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def USD_YEN(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 105.79
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    # E U R O

    def EURO_EURO(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get())
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def EURO_GBP(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.88
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def EURO_USD(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 1.23
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def EURO_YEN(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 131.05
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    # Y E N

    def YEN_YEN(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get())
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def YEN_GBP(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.0067
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def YEN_USD(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.0095
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    def YEN_EURO(self):
        try:
            self.currency_to.delete(0, END)
            self.converted_currency = float(self.currency_from.get()) * 0.0077
            self.converted_currency = str("{0:.2f}".format(self.converted_currency))
            self.currency_to.insert(0, self.converted_currency)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number!')
            self.currency_from.delete(0, END)

    # C H E C K I N G  F O R  C O R E S P O N D I N G  C U R R E N C I E S

    def convert(self):
        if self.from_currencies.get() == 'GBP' and self.to_currencies.get() == 'USD':
            self.GBP_USD()
        elif self.from_currencies.get() == 'GBP' and self.to_currencies.get() == 'EURO':
            self.GBP_EURO()
        elif self.from_currencies.get() == 'GBP' and self.to_currencies.get() == 'YEN':
            self.GBP_YEN()
        elif self.from_currencies.get() == 'GBP' and self.to_currencies.get() == 'GBP':
            self.GBP_GBP()

        elif self.from_currencies.get() == 'USD' and self.to_currencies.get() == 'GBP':
            self.USD_GBP()
        elif self.from_currencies.get() == 'USD' and self.to_currencies.get() == 'EURO':
            self.USD_EURO()
        elif self.from_currencies.get() == 'USD' and self.to_currencies.get() == 'YEN':
            self.USD_YEN()
        elif self.from_currencies.get() == 'USD' and self.to_currencies.get() == 'USD':
            self.USD_USD()

        elif self.from_currencies.get() == 'EURO' and self.to_currencies.get() == 'GBP':
            self.EURO_GBP()
        elif self.from_currencies.get() == 'EURO' and self.to_currencies.get() == 'USD':
            self.EURO_USD()
        elif self.from_currencies.get() == 'EURO' and self.to_currencies.get() == 'YEN':
            self.EURO_YEN()
        elif self.from_currencies.get() == 'EURO' and self.to_currencies.get() == 'EURO':
            self.EURO_EURO()

        elif self.from_currencies.get() == 'YEN' and self.to_currencies.get() == 'GBP':
            self.YEN_GBP()
        elif self.from_currencies.get() == 'YEN' and self.to_currencies.get() == 'USD':
            self.YEN_USD()
        elif self.from_currencies.get() == 'YEN' and self.to_currencies.get() == 'EURO':
            self.YEN_EURO()
        elif self.from_currencies.get() == 'YEN' and self.to_currencies.get() == 'YEN':
            self.YEN_YEN()

    # C R E T I N G  T H E  G U I  I N T E R F A C E

    def create_widgets(self):

        # F I R S T  R O W

        self.from_label = Label(self, text='From:')
        self.from_label.grid(row=0, sticky=E)

        self.from_currencies = StringVar(self)
        self.from_currencies.set('GBP')

        self.currency_from_selection = OptionMenu(self, self.from_currencies, 'GBP', 'USD', 'EURO', 'YEN')
        self.currency_from_selection.grid(row=0, column=1, sticky=N + E + S + W)

        self.currency_from = Entry(self)
        self.currency_from.grid(row=0, column=2)

        # S E C O N D  R O W

        self.to_label = Label(self, text='To:')
        self.to_label.grid(row=1, sticky=E)

        self.to_currencies = StringVar(self)
        self.to_currencies.set('USD')

        self.currency_to_selection = OptionMenu(self, self.to_currencies, 'GBP', 'USD', 'EURO', 'YEN')
        self.currency_to_selection.grid(row=1, column=1, sticky=N + E + S + W)

        self.currency_to = Entry(self)
        self.currency_to.grid(row=1, column=2)

        # T H I R D  R O W

        self.go_button = Button(self, text='Go', command=lambda: self.convert())
        self.go_button.grid(row=2, column=1, columnspan=2, sticky=N + E + S + W)


currency_converter = CurrencyConverter(currency).grid()
currency.mainloop()