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


  col1,col2,col3 = st.columns(3)

  with col1:
    with st.container(border = True):
      month_c = st.number_input("Enter your **Monthly Senditure**",0,200,50)

      total_c = st.number_input("Enter your **Total Spenditure**",0,10000,500)

      pay_method = st.selectbox("Please enter your **Payment Method**",['Electronic check','Mailed check','Bank transfer(automatic)','Credit card(automatic)'])

      # Here , o is Online
      o_security = st.selectbox("Did you have **Online Security** ?",['Yes','No','No phone service'])

      o_backup = st.selectbox("Did you have **Online Backup** ?",['Yes','No','No phone service'])



  with col2:
    with st.container(border = True):
      partner = st.selectbox("Is there your **Life Partner**:",["Yes","No"])

      senior_c = st.selectbox("Are you a **Senior Citizen**:",["Yes","No"])

      if senior_c == "yes":
        x = 1
      else:
        x = 0

      depend = st.radio("Are you a **Depended** Person ?:",["Yes","No"])

      ml = st.radio("Did you have **Multiple Lines** ?",['Yes','No','No phone service'])

      ps = st.radio("Did you have a **Phone Service** ?",["Yes","No"])



  with col3:
    with st.container(border = True):

      internet_s = st.selectbox("Which **Internet Service** are your having ?:",['DSL','Fiber optic','No'])

      dp = st.selectbox("Are you have **Device Protection** ?",['Yes','No','No phone service'])

      tech_support = st.selectbox("Did you have **Tech Support** ?",['Yes','No','No phone service'])

      stream_movie = st.selectbox("Did you have **Streaming Movie Subscription** ?",['Yes','No','No phone service'])
      stream_tv = st.selectbox("Did you have **Streamling TV Subscription** ?",['Yes','No','No phone service'])


# ============================================== Author(About Me) ==============================================

with st.sidebar:

     st.header("About Me")
    
     st.image("https://media.licdn.com/dms/image/v2/D4D03AQGGR3gc6WIYDA/profile-displayphoto-crop_800_800/B4DaDs9QC8GsAI-/0/1790681876550?e=1793232000&v=beta&t=gU_2TjebvQ7q9jDCwPdQ3WfwX0nVp3BwBb3uwY5y3WM",width = 250)



     st.markdown(f"""
     Hello {name} !!!

     Myself **Arth Jain**

     About Me: 
     **GitHub link** -> [Click Here](https://github.com/ArthJain123/Customer-Churn-Prediction-ML) \n
     **Linkedin Profile** -> [Connect with me](https://www.linkedin.com/in/arth-jain-278191385)

     It was my 6th Project
     **"Customer Churn Prediction"**.

     For this project
     I have to predict
     from a given data that
     wheather a Customer will Stay/Churn or Leave/No Churn.

     The Targetting Feature(y) is **"Churn"**
     where "Yes" indicates Customer Leave
     and "No" indicates Customer Stay.

     """)
