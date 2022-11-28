import streamlit as st
import pickle
import pandas as pd
import numpy as np

car_mpg = pickle.load(open('car_mpg.pkl','rb'))

st.title('Car Mileage Prediction')

col1,col2,col3,col4 = st.columns(4)
# cylinder=8,displacement=206,horsepower=200,weight=1900,modelyear=70,origin=2

with col1:
    cd = st.number_input('Cylinder')
with col2:
    disp = st.number_input('Displacement')
with col3:
    hp = st.number_input('Horsepower')
with col4:
    wt = st.number_input('weight')

col5,col6 = st.columns(2)

with col5:
    yr = st.number_input('Model Year')
with col6:
    org = st.number_input('Origin [choose 1:America 2:Europe 3:Asia]')

if st.button('Predict Mileage'):
    cylinder = cd
    displacement = disp
    horsepower = hp
    weight = wt
    year = yr
    origin = org

    df = pd.DataFrame(
        {'cylinders': [cylinder], 'displacement': [displacement], 'horsepower': horsepower, 'weight': [weight],
         'model year': [year], 'origin': [origin]})
    # st.table(df)
    result =car_mpg.predict(df)
    st.header("Predicted new mileage for above values is "+ str(int(result[0])))