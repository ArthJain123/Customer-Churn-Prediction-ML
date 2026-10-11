import streamlit as st
import numpy as np
import pandas as pd

# ========================================= Customer Details ==========================================

with st.container(border = True):
     st.image("https://i.pinimg.com/736x/16/a9/17/16a91717984d7812f7b11194c0179f7d.jpg",width = 600,use_container_width = True)

st.title("Customer Churn Prediction")

tab1,tab2 = st.tabs(["User's Details **Store Here!**","The DataSet"])

with tab1:
  name = st.text_input("Please Enter Your Name:")
  cus_id = st.text_input("Enter your Customer ID:")

  if name:
    st.write(f"Welcome **'{name}'**!")

  sex = st.radio("Enter your sex:",["Male","Female"])

  with st.container(border = True):
    tenure = st.slider("Enter Your tenure/Spending Time:",0,100,20)

  contract = st.selectbox("Enter your Contract term:",['Month-to-month','One year','Two year'])
