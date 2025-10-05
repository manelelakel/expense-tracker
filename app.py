import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title(" Suivie des Depenses ")
df = pd.read_csv("sample_data.csv")
st.subheader("Liste des depenses")
st.dataframe(df)
st.subheader("depenses par categorie")
fig2,ax2=plt.subplots()
df.groupby("Category")["Amount"].sum().plot(kind="bar" ,ax=ax)
st.pyplot(fig)
st.subheader("Depenses par date")
fig2,ax2=plt.subplots()
df.groupby("Date")["Amount"].sum().plot(kind="line", marker="o", ax=ax2)
st.pyplot(fig2)
