# Step 1: Load Important Module
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
# This streamlit is for web based application project


# Web Page Code
st.title("Health Insurance Prediction")
img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO8RypBfeV6p2SBEbbcH6iR5TeLH1fP9p1VZnDEI29pw&s=10'
st.image(img_url)


# Step 2: Load Insurance Data
url = 'https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv'
df = pd.read_csv(url)

# Step 3: EDA: Exploratory Data Analysis
df.drop("Customer_ID", axis = 1, inplace = True)

df['Previous_Insurance'] = df['Previous_Insurance'].map({'No':0, 'Yes':1})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'No':0, 'Yes':1})

# Step 4: Divide dataset into features and targets
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Step 5: Divide data into training and testing part
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.3)

# Step 6: Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Show Data Sample
st.write(df.head())
# Create Side Bar for user input Form
st.sidebar.title("Fill Customer Details")
st.sidebar.image(img_url)

all_ans = []
for index, col_name in enumerate(X.columns):
  min_v = X[col_name].min()
  max_v = X[col_name].max()
  if col_name != "Previous_Insurance":
    value = st.sidebar.slider(f"Select value for {col_name}", min_value = min_v, max_value = max_v)
  else:
    value = st.sidebar.number_input(f"Select value for {col_name} {{0:No, 1:Yes}}:")

  all_ans.append(value)

ud = {j:all_ans[i] for i,j in enumerate(x.colimns)}
user_df = pd.DataFrame(all_ans, columns = X.columns)
st.write(user_df)

#===================================Prediction===================================

if st.button("Click to Predict"):
  with st.spinner("Predicting"):
    import time
    time.sleep(2)
final_ans = model.predict([all_ans])[0]
if final_ans == 0:
  st.info("❌Customer will not buy the insurance❌")
else:
  st.success("✅Customer will buy the insurance✅")


