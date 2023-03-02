import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Supermarket Data")
df = pd.read_csv('./supermarket.csv')
st.subheader('Top 10 Performing Stores')
df.sort_values(["store_sales"], axis=0, ascending=[False], inplace=True)
st.dataframe(df[["store_id","store_sales"]].head(n=10))

st.subheader('Lowest 10 performing stores')
df.sort_values(["store_sales"], axis=0, ascending=[True], inplace=True)
st.dataframe(df[["store_id","store_sales"]].head(n=10))

st.subheader("Available Items in Store")

df.sort_values(["items_available"], axis=0, ascending=[False], inplace=True)
st.dataframe(df[['store_id','items_available']].head(n=10))
st.bar_chart(data=df.head(n=10), x='store_id' , y='items_available')