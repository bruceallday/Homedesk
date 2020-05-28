from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title('calculator')
calculator.resizable(0, 0)


# C R E A T I N G  T H E  C L A S S

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()

    # R E P L A C I N G  T H E  T E X T  I N  T H E  O U T P U T  W I N D O W

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    # C A L C L A T I N G  T H E  E X P R E S S I O N  A N D  L O O K I N G  F O R  E R R O R S

    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace('%', '/ 100')

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo('Error', 'Invalid Input')

    # C A L C U L A T I N G  T E N  P E R C E N T

    def calculateTenPercent(self):
        self.percentageExpression = int(self.display.get())

        try:
            self.tenPercentResult = (self.percentageExpression - self.percentageExpression / 10)
            self.replaceText(self.tenPercentResult)
        except:
            messagebox.showinfo('Error', 'Invalid Input')

    # C A L C U L A T I N G  T W E N T Y  P E R C E N T

    def calculateTwentyPercent(self):
        self.TwentyPercentExpression = float(self.display.get())

        try:
            self.TwentyPercentResult = (self.TwentyPercentExpression - self.TwentyPercentExpression / 10 * 2)
            self.replaceText(self.TwentyPercentResult)
        except:
            messagebox.showinfo('Error', 'Invalid Input')

    # C A L C U L A T I N G  T H I R T Y  P E R C E N T

    def calculateThirtyPercent(self):
        self.ThirtyPercentExpression = int(self.display.get())

        try:
            self.ThirtyPercentResult = (self.ThirtyPercentExpression - self.ThirtyPercentExpression / 10 * 3)
            self.replaceText(self.ThirtyPercentResult)
        except:
            messagebox.showinfo('Error', 'Invalid Input')

    # A P P E N D I N G  T O  T H E  D I S P L A Y

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    # C L E A R I N G  T H E  T E X T

    def clearText(self):
        self.replaceText('0')

    # C R E A T I N G  T H E  W I D G E T S

    def createWidgets(self):
        self.display = Entry(self, font=('Helvetica', 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        # F I R S T  R O W

        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=0, command=lambda: self.appendToDisplay('7'))
        self.sevenButton.grid(row=1, column=0, sticky=N+S+E+W)

        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=0, command=lambda: self.appendToDisplay('8'))
        self.eightButton.grid(row=1, column=1, sticky=N+E+S+W)

        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=0, command=lambda: self.appendToDisplay('9'))
        self.nineButton.grid(row=1, column=2, sticky=N+E+S+W)

        self.timesButton = Button(self, font=("Helvetica", 11), text="x", borderwidth=0, command=lambda: self.appendToDisplay('*'))
        self.timesButton.grid(row=1, column=3, sticky=N+E+S+W)

        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=0, command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky=N+E+S+W)

        # S E C O N D  R O W

        self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=0, command=lambda: self.appendToDisplay('4'))
        self.fourButton.grid(row=2, column=0, sticky=N+E+S+W)

        self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=0, command=lambda: self.appendToDisplay('5'))
        self.fiveButton.grid(row=2, column=1, sticky=N+E+S+W)

        self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=0,command=lambda: self.appendToDisplay('6'))
        self.sixButton.grid(row=2, column=2, sticky=N+E+S+W)

        self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=0, command=lambda: self.appendToDisplay('/'))
        self.divideButton.grid(row=2, column=3, sticky=N+E+S+W)

        self.percentageButton = Button(self, font=("Helvetica", 11), text="%", borderwidth=0, command=lambda: self.appendToDisplay('%'))
        self.percentageButton.grid(row=2, column=4, sticky=N+E+S+W)

        # T H I R D    R O W

        self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=0, command=lambda: self.appendToDisplay('1'))
        self.oneButton.grid(row=3, column=0, sticky=N+E+S+W)

        self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=0, command=lambda: self.appendToDisplay('2'))
        self.twoButton.grid(row=3, column=1, sticky=N+E+S+W)

        self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=0, command=lambda: self.appendToDisplay('3'))
        self.threeButton.grid(row=3, column=2, sticky=N+E+S+W)

        self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=0, command=lambda: self.appendToDisplay('-'))
        self.minusButton.grid(row=3, column=3, sticky=N+E+S+W)

        self.equalsButton = Button(self, font=("Helvetica", 11), text="=", borderwidth=0, command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=3, rowspan=2, column=4, sticky=N+E+S+W)

        # F O U R T H    R O W

        self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=0, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)

        self.dotButton = Button(self, font=("Helvetica", 11), text=".", borderwidth=0, command=lambda: self.appendToDisplay('.'))
        self.dotButton.grid(row=4, column=2, sticky=N+E+S+W)

        self.plusButton = Button(self, font=("Helvetica", 11), text="+", borderwidth=0, command=lambda: self.appendToDisplay('+'))
        self.plusButton.grid(row=4, column=3, sticky=N+E+S+W)

        # F I F T H  R O W

        self.tenPercentButton = Button(self, font=('Helvetica', 11), text="- 10%", borderwidth=0, command=lambda: self.calculateTenPercent())
        self.tenPercentButton.grid(row=5, column=0, columnspan=2, sticky=N+E+S+W)

        self.twentyPercentButton = Button(self, font=('Helvetica', 11), text='- 20%', borderwidth=0, command=lambda: self.calculateTwentyPercent())
        self.twentyPercentButton.grid(row=5, column=2, columnspan=2, sticky=N+E+S+W)

        self.thirtyPercentButton = Button(self, font=('Helvetica', 11), text="- 30%", borderwidth=0, command=lambda: self.calculateThirtyPercent())
        self.thirtyPercentButton.grid(row=5, column=4, columnspan=2, sticky=N+E+S+W)


app = Application(calculator).grid()
calculator.mainloop()