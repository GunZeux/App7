import streamlit as st


st.title("Weather Forecast for the Next Days")
location = st.text_input("Place:", key="place", placeholder="Enter a Location")
days = st.slider("Forecast Days:", min_value=1, max_value=5, key="days",
                 help="Select the number of forcast Days")
view = st.selectbox("Select data to view:", ["Temperature", "Sky"], key="view")

st.subheader(f"{view} for the next {days} days(s) in {location}")

