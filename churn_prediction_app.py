import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
    page_title = "Customer Churn Prediction",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded"
)


# ============================================= Site Layout ===============================================

with st.container(border = True):
  st.image("https://images.unsplash.com/photo-1607453361165-c629a0d1839d?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",width = 600,use_container_width = True)


st.title("Customer Churn Prediction")


tabs = ["👤 User's Details",
        "📊 Dataset Information",
        "🤖 Model Performance"]

tab1,tab2,tab3 = st.tabs(tabs)

# =================================== Tab1 ======================================


with tab1:
  name = st.text_input("Please enter your **Name** :")
  cus_id = st.text_input("Please enter your **Customer ID** :")

  if name:
    st.write(f"Welcome **'{name}'**!")

  sex = st.radio("Enter your **Gender** :",["Male","Female"])

  with st.container(border = True):
    tenure = st.slider("Enter Your **Tenure(Spending Time)** :",0,100,20)

  contract = st.selectbox("Enter your **Contract type** :",['Month-to-month','One year','Two year'])

  st.write("""
  ### **Personal Details**

  ---
  """)


  col1,col2 = st.columns(2)

# ============================== Column 1 ==============================


  with col1:
    with st.container(border = True):
      month_c = st.number_input("Enter your **Monthly Senditure** :",0,200,50)

      total_c = st.number_input("Enter your **Total Spenditure** :",0,10000,500)

      pay_method = st.selectbox("Please enter your **Payment Method** :",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])

      # Here , o is Online
      state = ['Yes','No','No phone service']

      o_security = st.selectbox("Did you have **Online Security** ?",state)

      o_backup = st.selectbox("Did you have **Online Backup** ?",state)


# ============================== Column 2 ==============================


  with col2:
    with st.container(border = True):

      internet_s = st.selectbox("Which **Internet Service** are your having ?",['DSL','Fiber optic','No'])

      dp = st.selectbox("Did you have **Device Protection** ?",state)

      tech_support = st.selectbox("Did you have **Tech Support** ?",state)

      stream_movie = st.selectbox("Did you have **Streaming Movie Subscription** ?",state)
      stream_tv = st.selectbox("Did you have **Streamling TV Subscription** ?",state)


# ============================== Expander ==============================


  with st.expander("**Please also fill this information ->**"):
    with st.container(border = True):

      condition = ["Yes","No"]

      partner = st.selectbox("Is there your **Life Partner** ?",condition)

      senior_c = st.selectbox("Are you a **Senior Citizen** ?",condition)

      if senior_c == "Yes":
        senior_c = 1
      else:
        senior_c = 0

      depend = st.radio("Are you a **Depended** Person ?",condition)

      ml = st.radio("Did you have **Multiple Lines** ?",state)

      ps = st.radio("Did you have a **Phone Service** ?",condition)
        

  if st.button("Predict Customer Churn",type = "primary"):
    st.success("Your Details were stored successfully")
    st.balloons()

  else:
    st.info("Enter the customer details and click Predict Customer Churn")


# ============================================== Author(About Me) ==============================================

with st.sidebar:

    with st.container(border = True):
      st.title(":blue[About Me]")

      st.image("https://media.licdn.com/dms/image/v2/D4D03AQGGR3gc6WIYDA/profile-displayphoto-crop_800_800/B4DaDs9QC8GsAI-/0/1790681876550?e=1795651200&v=beta&t=ZpbSMFPsF6J732OTU7TtVhzrNRnHoHHBQbHZuLWl8N0")

    
    st.write(f"""
    Hello {name} ,
    
    My name is **:blue[Arth Jain]**.\n
    Nice to meet you.

    My social profiles ->
    ----
    """)
    
    with st.container(border = True):

        st.write("""  
        
        - **GitHub**  ->  [You can view the project here](https://github.com/ArthJain123/Customer-Churn-Prediction-ML)

        - **LinkedIn** -> [Connect with me](https://www.linkedin.com/in/arth-jain-278191385)

        """)

    st.write("""
    ----

    It was my **6th Project (Customer Churn Prediction)**

    This project predicts whether a customer
    is likely to stay or leave based on their
    service details and account information.
    
    ```
    Target: Churn Feature
    
    [0] as Customer stays
    [1] as Customer leaves
    ```
    """)


with tab2:

  data = pd.read_csv("Customer_Churn_Prediction.csv")

  st.dataframe(data,use_container_width = True)

  data["TotalCharges"] = pd.to_numeric(data["TotalCharges"],errors = "coerce")

  obj_dtype = data.select_dtypes(include = "object").columns.to_list()
  num_dtype = data.select_dtypes(include = ["int","float"]).columns.to_list()

  st.write(f"""
  
  ### Data Insights
  
  ---

  Features Names with **"Object"** Datatype: 
  {obj_dtype}

  Features Names with **"Numeric"** Datatype:
  {num_dtype}
  """)

