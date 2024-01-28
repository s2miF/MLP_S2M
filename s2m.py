# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle as pi
import streamlit as st
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeRegressor

lm = pi.load(open('/Users/SamiFahad/anaconda3/envs/s2mi_streamlit/trained_model.sav', 'rb'))

def predict (input_data):
    
    input_as_np = np.array(input_data)
    input_resh = input_as_np.reshape(1,-1)
    pre = lm.predict(input_resh)    
    if (pre > 50):
        return "the price is Highest"
    else:
        return "the price is lowest"

    return(pre)

def main():
    st.title("Games Predict web app")

    name = st.text_input("what do like sport or pokemon?")
    if name == 'sport':
        name = 1
    else:
        name = 0
    
    Platform = st.text_input("What is the platform wii or nes")
    if Platform == 'wii':
        Platform = 18
    
    else:
        Platform = 8

    Genre = st.text_input("the genre is sport or Action?")
    if Genre == 'Action':
        Genre = 11

    else:
        Genre = 3

    Publisher = st.text_input("the Publisher is Nintendo or Take-Two Interactive?")
    if Publisher == 'Nintendo':
        Publisher = 16

    else:
        Publisher = 7
    
    Year = st.number_input("what is the Year?",step=1)
    NA_Sales = 20.0
    EU_Sales = 18.1
    JP_Sales = 7.99
    Other_Sales = 12.1
    
    # code for pediction 
    dignosis = ''
    # creating a button for perdiction
    if st.button('Games test Result'):
        dignosis = predict([name,Platform,Genre,Publisher,Year,NA_Sales,EU_Sales,JP_Sales,Other_Sales])
        print("the price is :",dignosis)

        
    st.success(dignosis)
    
if __name__=='__main__':
    main()
