from tkinter import *
from tkinter import messagebox


toolbar = Tk()
toolbar.title('Depop')
toolbar.resizable(0, 0)
class DepopGraphToolbar(Frame):
    def __init__(self, master)
        Frame.__init__(self, master)
        self.create_widgets()


    # C R E A T I N G  T H E  G U I  I N T E R F A C E

    def create_widgets(self):
        # N E W  I T E M  R O W S

        self.blank1 = Label(self, text='')
        self.blank1.grid(row=0, column=0)

        self.new_item_label = Label(self, text='Sold Item:')
        self.new_item_label.grid(row=1, column=0, sticky=W)

        self.clothing_type = StringVar(self)
        self.clothing_type.set('Hat')

        self.item_dropdown_menu = OptionMenu(self, self.clothing_type, 'Hat', 'Tshirt', 'Shirt', 'Sweater','Jacket', 'Trouser', 'Short', 'Shoes', 'misc')

        self.item_dropdown_menu.grid(row=2, column=0, sticky=E + W)

        self.blank1 = Label(self, text='')
        self.blank1.grid(row=3, column=2)

        # P R I C E  R O W S

        self.price_label = Label(self, text='Sale Price:')
        self.price_label.grid(row=1, column=1, sticky=W)

        self.price_entry = Entry(self)
        self.price_entry.grid(row=2, column=1)

        self.blank2 = Label(self, text='')
        self.blank2.grid(row=6, column=0)

        # D A T E  R O W S

        self.date_label = Label(self, text='Sale Date:')
        self.date_label.grid(row=1, column=2, sticky=W)

        self.date_entry = Entry(self)
        self.date_entry.grid(row=2, column=2)

        self.submit_date_button = Button(self, text='S u b m i t')
        self.submit_date_button.grid(row=3, column=1,columnspan = 2, sticky=N + E + S + W)

        self.blank3 = Label(self, text='')
        self.blank3.grid(row=10, column=0)



        # S T O C K  C O S T  R O W S

        self.new_stock_label = Label(self, text='New Stock Cost:')
        self.new_stock_label.grid(row=5, column=0, sticky=W)

        self.new_stock_entry = Entry(self)
        self.new_stock_entry.grid(row=6, column=0)

        self.new_stock_button = Button(self, text='S u b m i t')
        self.new_stock_button.grid(row=7, column=0, sticky=N + E + S + W)


        # T O T A L  S T O C K  R O W

        self.total_stock_cost_label = Label(self, text='Total Stock Cost:')
        self.total_stock_cost_label.grid(row=5, column=1, sticky=W)

        # T O T A L  S A L E S   R O W

        self.items_sold = Label(self, text='Total Items Sold:')
        self.items_sold.grid(row=7, column=1, sticky=W)

        # T O T A L  S A L E S

        self.items_sold = Label(self, text='Total Sales:')
        self.items_sold.grid(row=6, column=1, sticky=W)

        # N E T  R O W

        self.net_label = Label(self, text='Net:')
        self.net_label.grid(row=8, column=1, sticky=W)

        # G R A P H  C A N V A S


        # I T E M S  S O L D

        #self.blank6 = Label(self, text='')
        #self.blank6.grid(row=0, column=6)

        #self.item__sold_label = Label(self, text='I t e m s  S o l d :')
        #self.item__sold_label.grid(row=1, column=2, sticky= W, padx = 20)

        #self.hat_label = Label(self, text= 'Hats:')
        #self.hat_label.grid(row=2 , column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Tshirts:')
        #self.hat_label.grid(row=3, column=2,  sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Shirts:')
        #self.hat_label.grid(row=4, column=2, sticky=W, padx= 20)

        #self.hat_label = Label(self, text='Sweater:')
        #self.hat_label.grid(row=5, column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Jacket:')
        #self.hat_label.grid(row=6, column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Trouser:')
        #self.hat_label.grid(row=7, column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Shorts:')
        #self.hat_label.grid(row=8, column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='Shoes:')
        #self.hat_label.grid(row=9, column=2, sticky= W, padx= 20)

        #self.hat_label = Label(self, text='misc:')
        #self.hat_label.grid(row=10, column=2, sticky= W, padx= 20)


depop_toolbar = DepopGraphToolbar(toolbar).grid()
toolbar.mainloop()


