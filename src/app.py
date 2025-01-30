import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

# Title of the app
st.title("My Streamlit App")

# Your existing code
st.write("Welcome to my app!")

# If you have other components, you can render them here.
# Example:
number = st.slider("Pick a number", 0, 100)
st.write(f"You picked {number}")

connection = sqlite3.connect('data/Köksglädje.db')

table_names = ['customers', 'products', 'stores', 'transactiondetails', 'transactions']

df = {}
for table in table_names:
    df[table] = pd.read_sql_query(f"SELECT * FROM {table}", connection)

df_customers = df['customers'] 
df_products = df['products']
df_stores = df['stores']
df_td = df['transactiondetails']
df_transactions = df['transactions']

st.dataframe(df_stores)