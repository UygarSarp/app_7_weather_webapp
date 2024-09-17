import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ", key="place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="kaymac",
                 help="Select number of the days to Forecast")
what = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f"{what} for the next {days} days in {place}")

try:
    if place:
        filtered_data = get_data(place, days)

        if what == "Temperature":
            temp = [i["main"]["temp"]-273.15 for i in filtered_data]
            date = [i["dt_txt"] for i in filtered_data]
            graph = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(graph)

        if what == "Sky":
            resim = [i["weather"][0]["main"] for i in filtered_data]
            # resim = [i.lower() for i in resim]
            date = [i["dt_txt"] for i in filtered_data]
            images = {"Clouds": "imagess/cloud.png", "Clear": "imagess/clear.png",
                      "Rain": "imagess/rain.png", "Snow": "imagess/snow.png"}
            image_paths = [images[i] for i in resim]
            # st.image(image_paths, width=115)
            # st.write(date)
            for i, d in enumerate(image_paths):
                st.image(d, width=115)
                st.text(date[i])
except KeyError:
    st.title(f"""This "{place}" place does not exists.""")
