import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Muat model yang sudah disimpan
with open ('logistic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Tampilan utama aplikasi
st.title("Prediksi Spesies Ikan menggunakan Logistic Regression")

# Input untuk fitur prediksi
length = st.number_input("Panjang", min_value=0.0, step=0.1)
weight = st.number_input("Berat", min_value=0.0, step=0.1)
w_l_ratio = st.number_input("Rasio Berat-Panjang", min_value=0.0, step=0.1)

if st.button("Prediksi"):
    prediction = model.predict([[length, weight, w_l_ratio]])
    st.success(f'Prediksi Spesies: {prediction[0]}')