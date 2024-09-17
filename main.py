import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ", key="place")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, key="kaymac",
                 help="Select number of the days to Forecast")
what = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f"{what} for the next {days} days in {place}")


def get_data(day):
    dates = ["12", "131", "156"]
    temp = [1, 2, 4]
    temp = [i * day for i in temp]
    return dates, temp


d, t = get_data(days)
graph = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(graph)
