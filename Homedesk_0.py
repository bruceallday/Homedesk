#                                          H O M E D E S K
#                                  Written by Bruce M Pouncey 2017 - 2018

import datetime
from tkinter import *
from tkinter import messagebox, Tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import numpy as np
import pickle

style.use('ggplot')
root = Tk()
root.title('Project_0')
root.resizable(0, 0)

# G R A P H  D A T A

price_list = []

new_date_list = []

Save_Variables = []

date_list = []

Shop_data = {}

Stock_Cost = {}

f = Figure(figsize=(10, 4), dpi=100)
graph = f.add_subplot(111)

# G R A P H  C L A S S

class Depop_Graph(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.submenu = Menu(self.menu)
        self.calculator_menu = Menu(self.menu)

        # C A L C U L A T O R  C A S C A D E
        self.menu.add_cascade(label='Calculator', menu=self.calculator_menu)
        self.calculator_menu.add_command(label='Open', command=lambda: Calculator())
        self.conversion_menu = Menu(self.menu)

        # C O N V E R S I O N  C A S C A D E
        self.menu.add_cascade(label='Conversions', menu=self.conversion_menu)
        self.conversion_menu.add_command(label='Body Mass Index', command=lambda: BodyMassIndex())
        self.conversion_menu.add_command(label='Currency', command=lambda: CurrencyConverter())
        self.conversion_menu.add_command(label='Distance', command=lambda: DistanceConverter())
        self.conversion_menu.add_command(label='Height', command=lambda: HeightConverter())
        self.conversion_menu.add_command(label='Temperature', command=lambda: TempConverter())
        self.conversion_menu.add_command(label='Time', command=lambda: TimeConverter())

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, root)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP)

        self.button2 = Button(master=root, text='Toolbar', command=lambda: DepopGraphToolbar())
        self.button2.pack(side=RIGHT)

# G R A P H  T O O L B A R  C L A S S

class DepopGraphToolbar(Toplevel, Depop_Graph):

    def __init__(self):
        Toplevel.__init__(self)
        self.create_toolbar_widgets()

    def save_function(self):
        #self.hats()
        with open('Graph_New_Save_1.dat', 'ab') as f:
            pickle.dump([Stock_Cost, Shop_data, Save_Variables, price_list, new_date_list ,Depop_Graph, DepopGraphToolbar], f, protocol=2)
            messagebox.showinfo('', 'S a v e d!')

    def load_function(self):
        with open('Graph_New_Save_1.dat', 'rb') as f:
            while True:
                try:
                    Stock_Cost, Shop_data, Save_Variables, price_list, new_date_list, Depop_Graph, DepopGraphToolbar = pickle.load(f)
                    graph.bar(new_date_list, price_list, color='c', label='£')

                    self.sales_display.delete(0, END)
                    self.sales_display.insert(0, Save_Variables[0])
#
                    self.total_items_sold_display.delete(0, END)
                    self.total_items_sold_display.insert(0, Save_Variables[1])

                    self.net_display.delete(0, END)
                    self.net_display.insert(0, Stock_Cost['updated_net'])

                    self.stock_cost_display.delete(0, END)
                    self.stock_cost_display.insert(0, Stock_Cost['newstock'])

                    self.hats_count_row.delete(0, END)
                    self.hats_price_row.delete(0, END)

                    #self.append_data()

                    self.hats_count_row.insert(0, Shop_data['hatcount'])
                    self.hats_price_row.insert(0, Shop_data['hatprice'])

                    self.tshirt_count_row.delete(0, END)
                    self.tshirt_price_row.delete(0, END)

                    self.tshirt_count_row.insert(0, Shop_data['Tshirtcount'])
                    self.tshirt_price_row.insert(0, Shop_data['Tshirtprice'])

                    self.shirt_count_row.delete(0, END)
                    self.shirt_price_row.delete(0, END)

                    self.shirt_count_row.insert(0, Shop_data['shirtcount'])
                    self.shirt_price_row.insert(0, Shop_data['shirtprice'])

                    self.sweater_count_row.delete(0, END)
                    self.sweater_price_row.delete(0, END)

                    self.sweater_count_row.insert(0, Shop_data['sweatercount'])
                    self.sweater_price_row.insert(0, Shop_data['sweaterprice'])

                    self.jackets_count_row.delete(0, END)
                    self.jackets_price_row.delete(0, END)

                    self.jackets_count_row.insert(0, Shop_data['jacketcount'])
                    self.jackets_price_row.insert(0, Shop_data['jacketprice'])

                    self.trouser_count_row.delete(0, END)
                    self.trouser_price_row.delete(0, END)

                    self.trouser_count_row.insert(0, Shop_data['trousercount'])
                    self.trouser_price_row.insert(0, Shop_data['trouserprice'])

                    self.shorts_count_row.delete(0, END)
                    self.shorts_price_row.delete(0, END)

                    self.shorts_count_row.insert(0, Shop_data['shortscount'])
                    self.shorts_price_row.insert(0, Shop_data['shortsprice'])

                    self.shoes_count_row.delete(0, END)
                    self.shoes_price_row.delete(0, END)

                    self.shoes_count_row.insert(0, Shop_data['shoescount'])
                    self.shoes_price_row.insert(0, Shop_data['shoesprice'])

                    self.misc_count_row.delete(0, END)
                    self.misc_price_row.delete(0, END)

                    self.misc_count_row.insert(0, Shop_data['misccount'])
                    self.misc_price_row.insert(0, Shop_data['miscprice'])

                except EOFError:
                    break

    def get_new_date_data(self):
        try:
            self.new_date = str(self.date_entry.get())
            date_list.append(self.new_date)
            self.get_new_price_data()
        except ValueError:
            messagebox.showinfo('E R R O R', 'Please use YYYY-MM-DD')
            self.date_entry.delete(0, END)
            self.date_entry.insert(0, 0)
            price_list.pop()
            new_date_list.pop()

    def get_new_price_data(self):
        try:
            self.new_price = float(self.price_entry.get())
            price_list.append(self.new_price)
            self.get_postage_data()
        except ValueError:
            messagebox.showinfo('E R R O R', 'Incorrect Price')
            self.price_entry.delete(0, END)
            self.price_entry.insert(0, 0)
            price_list.pop()
            new_date_list.pop()

    def draw_graph(self):
        for i in range(len(date_list)):
            if i not in new_date_list:
                new_date_list.append(datetime.datetime.strptime(date_list[i], "%Y-%m-%d"))

        date_list.clear()
        graph.bar(new_date_list, price_list, color='c', label='£')

    def get_postage_data(self):
        try:
            self.new_postage_price = float(self.postage_entry.get())
            self.draw_graph()
            self.get_new_sales()
        except:
            messagebox.showinfo('E R R O R', 'Incorrect Postage')
            self.postage_entry.delete(0, END)
            self.postage_entry.insert(0, 0)
            price_list.pop()
            new_date_list.pop()

    def get_new_sales(self):
        self.newsale = float(self.sales_display.get())
        self.newsale = self.newsale + float(self.price_entry.get())
        Save_Variables.insert(0, self.newsale)
        self.get_new_item()

    def get_new_item(self):
        self.item_count = int(self.total_items_sold_display.get())
        self.item_count = self.item_count + 1
        Save_Variables.insert(1, self.item_count)
        self.get_new_net()

    def get_new_net(self):
        self.current_net = float(self.net_display.get())
        self.new_net_item = float(self.price_entry.get())
        self.minus_TP = self.new_net_item * 0.10
        self.final_net = self.new_net_item - self.minus_TP
        self.minus_OP = self.final_net * 0.03
        self.final_net_1 = self.final_net - self.minus_OP
        self.final_net_2 = self.final_net_1 - float(self.new_postage_price)
        self.final_net_3 = self.final_net_2 - 0.22
        self.new_net_total = (self.current_net) + (self.final_net_3)
        Save_Variables.insert(2, self.new_net_total)
        self.insert_sales()

    def insert_sales(self):
        self.sales_display.delete(0, END)
        self.sales_display.insert(0, Save_Variables[0])
        self.insert_item()

    def insert_item(self):
        self.total_items_sold_display.delete(0, END)
        self.total_items_sold_display.insert(0, Save_Variables[1])
        self.insert_new_net()

    def insert_new_net(self):
        self.net_display.delete(0, END)
        self.net_display.insert(0, Save_Variables[2])

        self.ammend_total_stock_cost()

    def ammend_total_stock_cost(self):
        try:
            self.newstock = float(self.new_stock_entry.get())
            self.newstock = self.newstock + float(self.stock_cost_display.get())

            self.newstock = float(self.new_stock_entry.get())
            self.newstock = self.newstock + float(self.stock_cost_display.get())
            Stock_Cost['newstock'] = self.newstock

            self.stock_cost_display.delete(0, END)
            self.stock_cost_display.insert(0, Stock_Cost['newstock'])

            self.updated_net = float(self.net_display.get()) - float(self.new_stock_entry.get())
            Stock_Cost['updated_net'] = self.updated_net

            self.net_display.delete(0, END)
            self.net_display.insert(0, Stock_Cost['updated_net'])

            self.new_stock_entry.delete(0, END)
            self.new_stock_entry.insert(0, 0)


        except ValueError:
            messagebox.showinfo('E R R O R ', 'Incorrect Stock Price')
            self.new_stock_entry.delete(0, END)

    def append_data(self):
        self.hats()

    def hats(self):
        try:
            self.hatcount = int(self.hats_count_row.get())
            self.hatprice = float(self.hats_price_row.get())
            if self.clothing_type.get() == 'Hat':
                self.hatcount = self.hatcount + 1
                self.hatprice = self.hatprice + float(self.item_price_entry.get())

                Shop_data['hatcount'] = self.hatcount
                Shop_data['hatprice'] = self.hatprice

                self.hats_count_row.delete(0, END)
                self.hats_price_row.delete(0, END)

                self.hats_count_row.insert(0, Shop_data['hatcount'])
                self.hats_price_row.insert(0, Shop_data['hatprice'])

            else:
                Shop_data['hatcount'] = self.hatcount
                Shop_data['hatprice'] = self.hatprice

                self.hats_count_row.delete(0, END)
                self.hats_price_row.delete(0, END)

                self.hats_count_row.insert(0, Shop_data['hatcount'])
                self.hats_price_row.insert(0, Shop_data['hatprice'])

            self.tshirt()


        except ValueError:
                messagebox.showinfo('E r r o r', 'Incorrect Item Price')
                self.item_price_entry.delete(0, END)

    def tshirt(self):
        try:
            self.Tshirtcount = int(self.tshirt_count_row.get())
            self.Tshirtprice = float(self.tshirt_price_row.get())
            if self.clothing_type.get() == 'Tshirt':
                self.Tshirtcount = self.Tshirtcount + 1
                self.Tshirtprice = self.Tshirtprice + float(self.item_price_entry.get())

                Shop_data['Tshirtcount'] = self.Tshirtcount
                Shop_data['Tshirtprice'] = self.Tshirtprice

                self.tshirt_count_row.delete(0, END)
                self.tshirt_price_row.delete(0, END)

                self.tshirt_count_row.insert(0, Shop_data['Tshirtcount'])
                self.tshirt_price_row.insert(0, Shop_data['Tshirtprice'])
            else:
                Shop_data['Tshirtcount'] = self.Tshirtcount
                Shop_data['Tshirtprice'] = self.Tshirtprice

                self.tshirt_count_row.delete(0, END)
                self.tshirt_price_row.delete(0, END)

                self.tshirt_count_row.insert(0, Shop_data['Tshirtcount'])
                self.tshirt_price_row.insert(0, Shop_data['Tshirtprice'])

            self.shirt()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def shirt (self):
        try:
            self.shirtcount = int(self.shirt_count_row.get())
            self.shirtprice = float(self.shirt_price_row.get())
            if self.clothing_type.get() == 'Shirt':
                self.shirtcount = self.shirtcount + 1
                self.shirtprice = self.shirtprice + float(self.item_price_entry.get())

                Shop_data['shirtcount'] = self.shirtcount
                Shop_data['shirtprice'] = self.shirtprice

                self.shirt_count_row.delete(0, END)
                self.shirt_price_row.delete(0, END)

                self.shirt_count_row.insert(0, Shop_data['shirtcount'])
                self.shirt_price_row.insert(0, Shop_data['shirtprice'])

            else:
                Shop_data['shirtcount'] = self.shirtcount
                Shop_data['shirtprice'] = self.shirtprice

                self.shirt_count_row.delete(0, END)
                self.shirt_price_row.delete(0, END)

                self.shirt_count_row.insert(0, Shop_data['shirtcount'])
                self.shirt_price_row.insert(0, Shop_data['shirtprice'])

            self.sweater()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def sweater(self):
        try:
            self.sweatercount = int(self.sweater_count_row.get())
            self.sweaterprice = float(self.sweater_price_row.get())
            if self.clothing_type.get() == 'Sweater':
                self.sweatercount = self.sweatercount + 1
                self.sweaterprice = self.sweaterprice + float(self.item_price_entry.get())

                Shop_data['sweatercount'] = self.sweatercount
                Shop_data['sweaterprice'] = self.sweaterprice

                self.sweater_count_row.delete(0, END)
                self.sweater_price_row.delete(0, END)

                self.sweater_count_row.insert(0, Shop_data['sweatercount'])
                self.sweater_price_row.insert(0, Shop_data['sweaterprice'])

            else:
                Shop_data['sweatercount'] = self.sweatercount
                Shop_data['sweaterprice'] = self.sweaterprice

                self.sweater_count_row.delete(0, END)
                self.sweater_price_row.delete(0, END)

                self.sweater_count_row.insert(0, Shop_data['sweatercount'])
                self.sweater_price_row.insert(0, Shop_data['sweaterprice'])

            self.jackets()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def jackets(self):
        try:
            self.jacketcount = int(self.jackets_count_row.get())
            self.jacketprice = float(self.jackets_price_row.get())
            if self.clothing_type.get() == 'Jacket':
                self.jacketcount = self.jacketcount + 1
                self.jacketprice = self.jacketprice + float(self.item_price_entry.get())

                Shop_data['jacketcount'] = self.jacketcount
                Shop_data['jacketprice'] = self.jacketprice

                self.jackets_count_row.delete(0, END)
                self.jackets_price_row.delete(0, END)

                self.jackets_count_row.insert(0, Shop_data['jacketcount'])
                self.jackets_price_row.insert(0, Shop_data['jacketprice'])

            else:
                Shop_data['jacketcount'] = self.jacketcount
                Shop_data['jacketprice'] = self.jacketprice

                self.jackets_count_row.delete(0, END)
                self.jackets_price_row.delete(0, END)

                self.jackets_count_row.insert(0, Shop_data['jacketcount'])
                self.jackets_price_row.insert(0, Shop_data['jacketprice'])

            self.trouser()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def trouser(self):
        try:
            self.trousercount = int(self.trouser_count_row.get())
            self.trouserprice = float(self.trouser_price_row.get())
            if self.clothing_type.get() == 'Trouser':
                self.trousercount = self.trousercount + 1
                self.trouserprice = self.trouserprice + float(self.item_price_entry.get())

                Shop_data['trousercount'] = self.trousercount
                Shop_data['trouserprice'] = self.trouserprice

                self.trouser_count_row.delete(0, END)
                self.trouser_price_row.delete(0, END)

                self.trouser_count_row.insert(0, Shop_data['trousercount'])
                self.trouser_price_row.insert(0, Shop_data['trouserprice'])

            else:
                Shop_data['trousercount'] = self.trousercount
                Shop_data['trouserprice'] = self.trouserprice

                self.trouser_count_row.delete(0, END)
                self.trouser_price_row.delete(0, END)

                self.trouser_count_row.insert(0, Shop_data['trousercount'])
                self.trouser_price_row.insert(0, Shop_data['trouserprice'])

            self.shorts()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def shorts(self):
        try:
            self.shortscount = int(self.shorts_count_row.get())
            self.shortsprice = float(self.shorts_price_row.get())
            if self.clothing_type.get() == 'Shorts':
                self.shortscount = self.shortscount + 1
                self.shortsprice = self.shortsprice + float(self.item_price_entry.get())

                Shop_data['shortscount'] = self.shortscount
                Shop_data['shortsprice'] = self.shortsprice

                self.shorts_count_row.delete(0, END)
                self.shorts_price_row.delete(0, END)

                self.shorts_count_row.insert(0, Shop_data['shortscount'])
                self.shorts_price_row.insert(0, Shop_data['shortsprice'])

            else:
                Shop_data['shortscount'] = self.shortscount
                Shop_data['shortsprice'] = self.shortsprice

                self.shorts_count_row.delete(0, END)
                self.shorts_price_row.delete(0, END)

                self.shorts_count_row.insert(0, Shop_data['shortscount'])
                self.shorts_price_row.insert(0, Shop_data['shortsprice'])

            self.shoes()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def shoes(self):
        try:
            self.shoescount = int(self.shoes_count_row.get())
            self.shoesprice = float(self.shoes_price_row.get())
            if self.clothing_type.get() == 'Shoes':
                self.shoescount = self.shoescount + 1
                self.shoesprice = self.shoesprice + float(self.item_price_entry.get())

                Shop_data['shoescount'] = self.shoescount
                Shop_data['shoesprice'] = self.shoesprice

                self.shoes_count_row.delete(0, END)
                self.shoes_price_row.delete(0, END)

                self.shoes_count_row.insert(0, Shop_data['shoescount'])
                self.shoes_price_row.insert(0, Shop_data['shoesprice'])

            else:
                Shop_data['shoescount'] = self.shoescount
                Shop_data['shoesprice'] = self.shoesprice

                self.shoes_count_row.delete(0, END)
                self.shoes_price_row.delete(0, END)

                self.shoes_count_row.insert(0, Shop_data['shoescount'])
                self.shoes_price_row.insert(0, Shop_data['shoesprice'])

            self.misc()

        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def misc(self):
        try:
            self.misccount = int(self.misc_count_row.get())
            self.miscprice = float(self.misc_price_row.get())
            if self.clothing_type.get() == 'misc':
                self.misccount = self.misccount + 1
                self.miscprice = self.miscprice + float(self.item_price_entry.get())

                Shop_data['misccount'] = self.misccount
                Shop_data['miscprice'] = self.miscprice

                self.misc_count_row.delete(0, END)
                self.misc_price_row.delete(0, END)

                self.misc_count_row.insert(0, Shop_data['misccount'])
                self.misc_price_row.insert(0, Shop_data['miscprice'])

            else:
                Shop_data['misccount'] = self.misccount
                Shop_data['miscprice'] = self.miscprice

                self.misc_count_row.delete(0, END)
                self.misc_price_row.delete(0, END)

                self.misc_count_row.insert(0, Shop_data['misccount'])
                self.misc_price_row.insert(0, Shop_data['miscprice'])


        except ValueError:
            messagebox.showinfo('E r r o r', 'Incorrect Item Price')
            self.item_price_entry.delete(0, END)

    def data_window(self):

        self.window_2 = Toplevel(self)
        self.window_2.title('Sales Data')
        self.window_2.resizable(0, 0)

        # I T E M  D R O P  M E N U

        self.new_item_label = Label(self.window_2, text='New Item:')
        self.new_item_label.grid(row=0, column=0, sticky=W)
        self.new_item_pricelabel = Label(self.window_2, text="Sale Price £:")
        self.new_item_pricelabel.grid(row=0, column = 1, sticky= W)

        self.clothing_type = StringVar(self.window_2)
        self.clothing_type.set('Hat')

        self.item_dropdown_menu = OptionMenu(self.window_2, self.clothing_type, 'Hat', 'Tshirt', 'Shirt', 'Sweater',
                                             'Jacket', 'Trouser', 'Shorts', 'Shoes', 'misc')
        self.item_dropdown_menu.grid(row=1, column=0, sticky=E + W)

        self.item_price_entry = Entry(self.window_2)
        self.item_price_entry.grid(row = 1, column = 1)
        self.item_price_entry.insert(0, 0)

        self.submit_item_button = Button(self.window_2, text = 'S u b m i t', command= lambda: self.append_data())
        self.submit_item_button.grid(row=1, column = 2, sticky= N + S + E + W)

        # H A T S  R O W

        self.hats_label = Label(self.window_2, text='Hat £:')
        self.hats_label.grid(row=2, column=0, sticky=E)

        self.hats_price_row = Entry(self.window_2)
        self.hats_price_row.grid(row = 2, column=1)
        self.hats_price_row.insert(0, 0)

        self.hats_count_row = Entry(self.window_2)
        self.hats_count_row.grid(row=2, column=2)
        self.hats_count_row.insert(0, 0)

        # T S H I R T  R O W

        self.Tshirt_label = Label(self.window_2, text='Tshirt £:')
        self.Tshirt_label.grid(row=3, column=0, sticky=E)

        self.tshirt_price_row = Entry(self.window_2)
        self.tshirt_price_row.grid(row =3, column = 1)
        self.tshirt_price_row.insert(0, 0)

        self.tshirt_count_row = Entry(self.window_2)
        self.tshirt_count_row.grid(row=3, column=2)
        self.tshirt_count_row.insert(0, 0)

        # S H I R T  R O W

        self.Shirt_label = Label(self.window_2, text='Shirt £:')
        self.Shirt_label.grid(row=4, column=0, sticky=E)

        self.shirt_price_row = Entry(self.window_2)
        self.shirt_price_row.grid(row = 4, column= 1)
        self.shirt_price_row.insert(0, 0)

        self.shirt_count_row = Entry(self.window_2)
        self.shirt_count_row.grid(row = 4, column = 2)
        self.shirt_count_row.insert(0, 0)

        # S W E A T E R  R O W

        self.sweater_label = Label(self.window_2, text='Sweater £:')
        self.sweater_label.grid(row=5, column=0, sticky=E)

        self.sweater_price_row = Entry(self.window_2)
        self.sweater_price_row.grid(row = 5, column = 1)
        self.sweater_price_row.insert(0, 0)

        self.sweater_count_row = Entry(self.window_2)
        self.sweater_count_row.grid(row= 5, column = 2)
        self.sweater_count_row.insert(0, 0)

        # J A C K E T S  R O W

        self.jackets_label = Label(self.window_2, text='Jackets £:')
        self.jackets_label.grid(row=6, column=0, sticky=E)

        self.jackets_price_row = Entry(self.window_2)
        self.jackets_price_row.grid(row=6, column = 1)
        self.jackets_price_row.insert(0, 0)

        self.jackets_count_row = Entry(self.window_2)
        self.jackets_count_row.grid(row= 6, column = 2)
        self.jackets_count_row.insert(0, 0)


        # T R O U S E R  R O W

        self.trouser_label = Label(self.window_2, text='Trouser £:')
        self.trouser_label.grid(row=7, column=0, sticky=E)

        self.trouser_price_row = Entry(self.window_2)
        self.trouser_price_row.grid(row= 7, column = 1)
        self.trouser_price_row.insert(0, 0)

        self.trouser_count_row = Entry(self.window_2)
        self.trouser_count_row.grid(row= 7, column = 2)
        self.trouser_count_row.insert(0, 0)

        # S H O R T S  R O W

        self.shorts_label = Label(self.window_2, text='Shorts £:')
        self.shorts_label.grid(row=8, column=0, sticky=E)

        self.shorts_price_row = Entry(self.window_2)
        self.shorts_price_row.grid(row= 8, column = 1)
        self.shorts_price_row.insert(0, 0)

        self.shorts_count_row = Entry(self.window_2)
        self.shorts_count_row.grid(row=8, column= 2)
        self.shorts_count_row.insert(0, 0)

        # S H O E S  R O W

        self.shoes_label = Label(self.window_2, text='Shoes £:')
        self.shoes_label.grid(row=9, column=0, sticky=E)

        self.shoes_price_row = Entry(self.window_2)
        self.shoes_price_row.grid(row= 9, column = 1)
        self.shoes_price_row.insert(0, 0)

        self.shoes_count_row = Entry(self.window_2)
        self.shoes_count_row.grid(row= 9, column = 2)
        self.shoes_count_row.insert(0, 0)

        # M I S C   R O W

        self.misc_label = Label(self.window_2, text='misc £:')
        self.misc_label.grid(row=10, column=0, sticky=E)

        self.misc_price_row = Entry(self.window_2)
        self.misc_price_row.grid(row = 10, column = 1)
        self.misc_price_row.insert(0, 0)

        self.misc_count_row = Entry(self.window_2)
        self.misc_count_row.grid(row= 10, column = 2)
        self.misc_count_row.insert(0, 0)

    def create_toolbar_widgets(self):

        # N E W  I T E M  R O W S
        self.blank1 = Label(self, text='')
        self.blank1.grid(row=0, column=0)


        # P O S T A G E  R O W S

        self.postage = Label(self, text=' Postage Price: £')
        self.postage.grid(row=3, column=0, sticky = W)

        self.postage_entry = Entry(self)
        self.postage_entry.grid(row= 4, column = 0)
        self.postage_entry.insert(0, 0)

        # P R I C E  R O W S

        self.price_label = Label(self, text='New Day Total: £')
        self.price_label.grid(row=1, column=1, sticky=W)

        self.price_entry = IntVar(self)
        self.price_entry = Entry(self)
        self.price_entry.grid(row=2, column=1)
        self.price_entry.insert(0, 0)

        self.blank2 = Label(self, text='')
        self.blank2.grid(row=6, column=0)

        # D A T E  R O W S

        self.date_label = Label(self, text='Sale Date:')
        self.date_label.grid(row=1, column=2, sticky=W)

        self.date_label = StringVar(self)
        self.date_entry = Entry(self)
        self.date_entry.grid(row=2, column=2)
        self.date_entry.insert(0, 'YYYY-MM-DD')

        self.submit_date_button = Button(self, text='S u b m i t', command=lambda:self.get_new_date_data())
        self.submit_date_button.grid(row=4, column = 1, columnspan = 2, sticky=N + E + S + W)


        # S T O C K  C O S T  R O W S

        self.new_stock_label = Label(self, text='New Stock Cost: £')
        self.new_stock_label.grid(row=5, column=0, sticky=W)

        self.new_stock_entry = Entry(self)
        self.new_stock_entry.grid(row=6, column=0)
        self.new_stock_entry.insert(0, 0)

        self.new_stock_button = Button(self, text='S u b m i t', command = lambda:self.ammend_total_stock_cost())
        self.new_stock_button.grid(row=7, column=0, sticky=N + E + S + W)

        # T O T A L  S T O C K  R O W

        self.total_stock_cost_label = Label(self, text='Total Stock Cost: £')
        self.total_stock_cost_label.grid(row=5, column=1, sticky=E)

        # T O T A L  S A L E S   R O W

        self.items_sold = Label(self, text='Total Items Sold:')
        self.items_sold.grid(row=7, column=1, sticky=E)

        # T O T A L  S A L E S

        self.items_sold = Label(self, text='Total Sales: £')
        self.items_sold.grid(row=6, column=1, sticky=E)

        # N E T  R O W

        self.net_label = Label(self, text='Net: £')
        self.net_label.grid(row=8, column=1, sticky=E)

        # S A L E S  D A T A  R O W

        self.data_button = Button(self, text='S h o p  d a t a', command=lambda: self.data_window())
        self.data_button.grid(row=8, column=0, sticky=N + S + E + W)

        # T O T A L  R O W

        self.stock_cost_display = Entry(self)
        self.stock_cost_display.grid(row= 5, column =2)
        self.stock_cost_display.insert(0, 0)

        self.sales_display = Entry(self)
        self.sales_display.grid(row= 6, column = 2)
        self.sales_display.insert(0, 0)

        self.total_items_sold_display = Entry(self)
        self.total_items_sold_display.grid(row = 7, column= 2)
        self.total_items_sold_display.insert(0, 0)

        self.net_display = Entry(self)
        self.net_display.grid(row = 8, column = 2)
        self.net_display.insert(0, 0)

        self.save_button = Button(self, text= 'S A V E', command= lambda: self.save_function())
        self.save_button.grid(row = 9, column = 2)

        self.load_button = Button(self, text= 'L O A D', command = lambda: self.load_function())
        self.load_button.grid(row = 10, column = 2 )

# C A L C U L A T O R  C L A S S

class Calculator(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
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

        self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=0,
                                  command=lambda: self.appendToDisplay('7'))
        self.sevenButton.grid(row=1, column=0, sticky=N + S + E + W)

        self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=0,
                                  command=lambda: self.appendToDisplay('8'))
        self.eightButton.grid(row=1, column=1, sticky=N + E + S + W)

        self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=0,
                                 command=lambda: self.appendToDisplay('9'))
        self.nineButton.grid(row=1, column=2, sticky=N + E + S + W)

        self.timesButton = Button(self, font=("Helvetica", 11), text="x", borderwidth=0,
                                  command=lambda: self.appendToDisplay('*'))
        self.timesButton.grid(row=1, column=3, sticky=N + E + S + W)

        self.clearButton = Button(self, font=("Helvetica", 11), text="C", borderwidth=0,
                                  command=lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky=N + E + S + W)

        # S E C O N D  R O W

        self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=0,
                                 command=lambda: self.appendToDisplay('4'))
        self.fourButton.grid(row=2, column=0, sticky=N + E + S + W)

        self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=0,
                                 command=lambda: self.appendToDisplay('5'))
        self.fiveButton.grid(row=2, column=1, sticky=N + E + S + W)

        self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=0,
                                command=lambda: self.appendToDisplay('6'))
        self.sixButton.grid(row=2, column=2, sticky=N + E + S + W)

        self.divideButton = Button(self, font=("Helvetica", 11), text="/", borderwidth=0,
                                   command=lambda: self.appendToDisplay('/'))
        self.divideButton.grid(row=2, column=3, sticky=N + E + S + W)

        self.percentageButton = Button(self, font=("Helvetica", 11), text="%", borderwidth=0,
                                       command=lambda: self.appendToDisplay('%'))
        self.percentageButton.grid(row=2, column=4, sticky=N + E + S + W)

        # T H I R D    R O W

        self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=0,
                                command=lambda: self.appendToDisplay('1'))
        self.oneButton.grid(row=3, column=0, sticky=N + E + S + W)

        self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=0,
                                command=lambda: self.appendToDisplay('2'))
        self.twoButton.grid(row=3, column=1, sticky=N + E + S + W)

        self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=0,
                                  command=lambda: self.appendToDisplay('3'))
        self.threeButton.grid(row=3, column=2, sticky=N + E + S + W)

        self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=0,
                                  command=lambda: self.appendToDisplay('-'))
        self.minusButton.grid(row=3, column=3, sticky=N + E + S + W)

        self.equalsButton = Button(self, font=("Helvetica", 11), text="=", borderwidth=0,
                                   command=lambda: self.calculateExpression())
        self.equalsButton.grid(row=3, rowspan=2, column=4, sticky=N + E + S + W)

        # F O U R T H    R O W

        self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=0,
                                 command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)

        self.dotButton = Button(self, font=("Helvetica", 11), text=".", borderwidth=0,
                                command=lambda: self.appendToDisplay('.'))
        self.dotButton.grid(row=4, column=2, sticky=N + E + S + W)

        self.plusButton = Button(self, font=("Helvetica", 11), text="+", borderwidth=0,
                                 command=lambda: self.appendToDisplay('+'))
        self.plusButton.grid(row=4, column=3, sticky=N + E + S + W)

        # F I F T H  R O W

        self.tenPercentButton = Button(self, font=('Helvetica', 11), text="- 10%", borderwidth=0,
                                       command=lambda: self.calculateTenPercent())
        self.tenPercentButton.grid(row=5, column=0, columnspan=2, sticky=N + E + S + W)

        self.twentyPercentButton = Button(self, font=('Helvetica', 11), text='- 20%', borderwidth=0,
                                          command=lambda: self.calculateTwentyPercent())
        self.twentyPercentButton.grid(row=5, column=2, columnspan=2, sticky=N + E + S + W)

        self.thirtyPercentButton = Button(self, font=('Helvetica', 11), text="- 30%", borderwidth=0,
                                          command=lambda: self.calculateThirtyPercent())
        self.thirtyPercentButton.grid(row=5, column=4, columnspan=2, sticky=N + E + S + W)

# B M I  C L A S S

class BodyMassIndex(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.create_widgets()

    def CalculateBMI(self):

        try:
            self.answer_output.delete(0, END)
            self.answer = float(self.weight_entry.get()) / float(self.height_entry.get()) / float(
                self.height_entry.get())
            self.answer_output.insert(0, self.answer)
        except ValueError:
            messagebox.showinfo('ERROR', 'That is not a number! ;)')
            self.answer_output.delete(0, END)
            self.weight_entry.delete(0, END)
            self.height_entry.delete(0, END)

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

# C U R R E N C Y  C L A S S

class CurrencyConverter(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
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

# D I S T A N C E  C L A S S

class DistanceConverter(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
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

        self.distance_from_selection = OptionMenu(self, self.from_distance, 'Meters', 'Kilometers', 'Miles',
                                                  'Light Years')
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

# H E I G H T  C L A S S

class HeightConverter(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
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

# T E M P E R A T U R E  C L A S S

class TempConverter(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
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

# T I M E  C L A S S

class TimeConverter(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
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

depopgraph = Depop_Graph(root).pack()
root.mainloop()

# © 2018 Bruce M Pouncey All rights reserved
