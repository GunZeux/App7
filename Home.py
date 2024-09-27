import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Place:", key="place", placeholder="Enter a Location")
days = st.slider("Forecast Days:", min_value=1, max_value=5, key="days",
                 help="Select the number of forcast Days")
view = st.selectbox("Select data to view:", ["Temperature", "Sky"], key="view")

st.subheader(f"{view} for the next {days} days(s) in {location}")

if location:
    try:
        filtered_data = get_data(location, days, view)
        if view == "Temperature":
            final_data = [sub_val["main"]["temp"]/10 for sub_val in filtered_data]
            date = [sub_val["dt_txt"] for sub_val in filtered_data]
            figure = px.line(x=date, y=final_data,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        else:
            final_data = [sub_val["weather"][0]["main"] for sub_val
                          in filtered_data]
            image_list = [f"images/{name}.png" for name in final_data]
            st.image(image_list, width=115)
    except KeyError:
        st.warning("Invalid Location")