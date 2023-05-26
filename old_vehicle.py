import streamlit as st
import numpy as np
import pickle

def price_find(car_name_,fuel_type_,transmission_,year_,Present_Price_,Driven_kms_):
    l = [[car_name_, fuel_type_, transmission_, int(year_), float(Present_Price_), int(Driven_kms_)]]
    modal_get = open("car.txt", "rb")
    modal = pickle.load(modal_get)
    ans = modal.predict(l)
    data = np.around(float(ans[0]), 2)
    if data > 0 :
        return data
    else :
        return ""

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
fuel_type = ['CNG', 'Diesel', 'Petrol']

transmission = ['Automatic', 'Manual']
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


st.title("Old Vehicle Selling Price")

col1,col2 = st.columns(2,gap="medium")
with col1 :
    car_name_var = st.selectbox("Car Name",car_name)
    car_name_index = car_name.index(car_name_var)
with col2 :
    fuel_type_var = st.selectbox("Fuel Type",fuel_type)
    fuel_type_index = fuel_type.index(fuel_type_var)

col3,col4 = st.columns(2,gap="medium")

with col3 :
    transmission_var = st.selectbox("Transmission",transmission)
    transmission_index = transmission.index(transmission_var)
with col4 :
    year_var = st.selectbox("Year",year)

col5,col6 = st.columns(2,gap="medium")

with col5 :
    Present_Price_var = st.text_input("Present Price (Lakhs)")
with col6 :
    Driven_kms_var = st.text_input("Driven kms")

col7,col8,col9,col10 = st.columns(4,gap="medium")


col11,col12,col13,col14,col15 = st.columns(5,gap="medium")

result = ""
with col13 :
    done  = st.button("DONE")
    if done :
        result = price_find(car_name_index,fuel_type_index,transmission_index,year_var,Present_Price_var,Driven_kms_var)

with col8 :
    st.markdown("Selling Price (Lakhs)")
with col9 :
    st.subheader(f"{result}")
    
