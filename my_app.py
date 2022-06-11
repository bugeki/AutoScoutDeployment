import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;"> Car Price Prediction App </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)



import datetime
today=st.date_input( '', datetime.datetime.now())

#sidebar header
st.sidebar.header('Car Price Calculator')

# make model
make_model=st.sidebar.selectbox("Make & Model", ["Audi A1", "Audi A3", "Opel Astra", "Opel Corsa", "Opel Insignia", "Renault Clio", "Renault Duster", "Renault Espace"])

#Age
age = st.sidebar.number_input("Age:",min_value=0)

# Gearing Type
Gearing_Type=st.sidebar.selectbox("Gearing Type", ["Manual", "Automatic", "Semi-automatic"])

#Km
km=st.sidebar.number_input("Km:",min_value=0, step=500)


#Fuel
Fuel=st.sidebar.selectbox("Fuel", ["Benzine", "Diesel","LPG/CNG"])


#hp_kW
hp_kW=st.sidebar.number_input("HP:",min_value=0, step=5)


import pickle
model = pickle.load(open('autoscout_lasso_model', 'rb'))

my_dict = {
    "hp_kW": hp_kW,
    "km": km,
    "age":age,
    "make_model": make_model,
    "Gearing_Type": Gearing_Type,
    "Fuel": Fuel,
}

my_dict=pd.DataFrame.from_dict([my_dict])
my_dict=pd.get_dummies(my_dict)


columns_name=['hp_kW', 'km', 'age', 'make_model_Audi A1', 'make_model_Audi A3',
       'make_model_Opel Astra', 'make_model_Opel Corsa',
       'make_model_Opel Insignia', 'make_model_Renault Clio',
       'make_model_Renault Duster', 'make_model_Renault Espace',
       'Gearing_Type_Automatic', 'Gearing_Type_Manual',
       'Gearing_Type_Semi-automatic', 'Fuel_Benzine', 'Fuel_Diesel',
       'Fuel_LPG/CNG']
my_dict = my_dict.reindex(columns=columns_name, fill_value=0)


if st.sidebar.button("Predict"):
    pred = model.predict(my_dict)
    st.success("The estimated value of the car is €{:.0f}. ".format(pred[0]))
st.sidebar.info("Please fill the form")



