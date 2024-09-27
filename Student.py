import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("happy.csv")
title = df.columns.tolist()
title = [word.replace("_", " ").title() for word in title]

st.title("in search of happiness".title())
x_value = st.selectbox("Select the Data for X axis", title[:6])
y_value = st.selectbox("Select the Data for X axis", title[1:6])

st.subheader(f"{x_value} and {y_value}")
figure1 = px.scatter(x=df[x_value.replace(" ", "_").lower()],
                     y=df[y_value.replace(" ", "_").lower()],
                     labels={"x": x_value, "y": y_value})
st.plotly_chart(figure1)
