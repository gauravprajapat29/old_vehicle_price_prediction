from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import numpy as np
import pickle

def data_get():
      c = Car_Name.current()
      f = Fuel_Type.current()
      t = Transmission.current()
      y = int(Year.get())
      p = float(Present_Price.get())
      d = int(Driven_kms.get())
      l = [[c,f,t,y,p,d]]
      modal_get = open(r"C:\Users\WSCUBETECH\OneDrive\Desktop\data set\project\car.txt","rb")
      modal = pickle.load(modal_get)
      ans = modal.predict(l)
      data = np.around(float(ans[0]),2)
      Selling_Price.config(text=str(data))








win = Tk()
win.config(bg = "#34eb4f")
win.geometry("1200x700")

font = Font(family = "Time New Roman", size = 12)

win.option_add("*TCombobox*Listbox*Font", font)
Label(win,text="Old Vehicle Selling Price",font=("Time New Roman",40,"bold"),
      bg = "#34eb4f").place(x = 255,y=50,height=80,width=690 )



car_name = ['800', 'Activa 3g', 'Activa 4g', 'Bajaj  ct 100',
       'Bajaj Avenger 150', 'Bajaj Avenger 150 street',
       'Bajaj Avenger 220', 'Bajaj Avenger 220 dtsi',
       'Bajaj Avenger Street 220', 'Bajaj Discover 100',
       'Bajaj Discover 125', 'Bajaj Dominar 400', 'Bajaj Pulsar  NS 200',
       'Bajaj Pulsar 135 LS', 'Bajaj Pulsar 150', 'Bajaj Pulsar 220 F',
       'Bajaj Pulsar NS 200', 'Bajaj Pulsar RS200', 'Hero  CBZ Xtreme',
       'Hero  Ignitor Disc', 'Hero Extreme', 'Hero Glamour',
       'Hero Honda CBZ extreme', 'Hero Honda Passion Pro', 'Hero Hunk',
       'Hero Passion Pro', 'Hero Passion X pro', 'Hero Splender Plus',
       'Hero Splender iSmart', 'Hero Super Splendor', 'Honda Activa 125',
       'Honda Activa 4G', 'Honda CB Hornet 160R', 'Honda CB Shine',
       'Honda CB Trigger', 'Honda CB Unicorn', 'Honda CB twister',
       'Honda CBR 150', 'Honda Dream Yuga ', 'Honda Karizma',
       'Hyosung GT250R', 'KTM 390 Duke ', 'KTM RC200', 'KTM RC390',
       'Mahindra Mojo XT300', 'Royal Enfield Bullet 350',
       'Royal Enfield Classic 350', 'Royal Enfield Classic 500',
       'Royal Enfield Thunder 350', 'Royal Enfield Thunder 500',
       'Suzuki Access 125', 'TVS Apache RTR 160', 'TVS Apache RTR 180',
       'TVS Jupyter', 'TVS Sport ', 'TVS Wego', 'UM Renegade Mojave',
       'Yamaha FZ  v 2.0', 'Yamaha FZ 16', 'Yamaha FZ S ',
       'Yamaha FZ S V 2.0', 'Yamaha Fazer ', 'alto 800', 'alto k10',
       'amaze', 'baleno', 'brio', 'camry', 'ciaz', 'city', 'corolla',
       'corolla altis', 'creta', 'dzire', 'elantra', 'eon', 'ertiga',
       'etios cross', 'etios g', 'etios gd', 'etios liva', 'fortuner',
       'grand i10', 'i10', 'i20', 'ignis', 'innova', 'jazz',
       'land cruiser', 'omni', 'ritz', 's cross', 'swift', 'sx4', 'verna',
       'vitara brezza', 'wagon r', 'xcent']
Label(win,text="Vehicle Name",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 100,y=180,height=40,width=200 )
Car_Name_var = StringVar()
Car_Name = ttk.Combobox(win, textvariable=Car_Name_var,font=("Time New Roman",15),width=20,values=car_name)
Car_Name.place(x = 350,y=180,height=40,width=210 )

fuel_type = ['CNG', 'Diesel', 'Petrol']
Label(win,text="Fuel Type",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 650,y=180,height=50,width=200 )
Fuel_Type_var = StringVar()
Fuel_Type = ttk.Combobox(win, textvariable=Fuel_Type_var,font=("Time New Roman",15),values=fuel_type)
Fuel_Type.place(x = 900,y=180,height=40,width=210 )


transmission = ['Automatic', 'Manual']
Label(win,text="Transmission",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 100,y=280,height=40,width=200 )
Transmission_var = StringVar()
Transmission = ttk.Combobox(win, textvariable=Transmission_var,font=("Time New Roman",15),values=transmission)
Transmission.place(x = 350,y=280,height=40,width=210 )

year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
Label(win,text="Year",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 650,y=280,height=50,width=200 )
Year_var = StringVar()
Year = ttk.Combobox(win, textvariable=Year_var,font=("Time New Roman",15),values=year)
Year.place(x = 900,y=280,height=40,width=210 )


Label(win,text="Present Price",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 100,y=380,height=40,width=200 )
Label(win,text="(Lakhs)",font=("Time New Roman",15,"bold"),bg = "#34eb4f").place(x = 100,y=420,height=20,width=200 )
Present_Price = Entry(win,font=("Time New Roman",15))
Present_Price.place(x = 350,y=380,height=40,width=210 )


Label(win,text="Driven kms",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 650,y=380,height=50,width=200 )
Driven_kms = Entry(win,font=("Time New Roman",15))
Driven_kms.place(x = 900,y=380,height=40,width=210 )

Label(win,text="Selling Price",font=("Time New Roman",23,"bold"),bg = "#34eb4f").place(x = 400,y=480,height=40,width=200 )
Label(win,text="(Lakhs)",font=("Time New Roman",15,"bold"),bg = "#34eb4f").place(x = 400,y=520,height=20,width=200 )
Selling_Price = Label(win,text="",font=("Time New Roman",23,"bold"))
Selling_Price.place(x = 610,y=490,height=40,width=210 )

button = Button(win,text="Done",font=("Time New Roman",23,"bold"),command=data_get)
button.place(x = 500,y=580,height=60,width=210 )


win.mainloop()