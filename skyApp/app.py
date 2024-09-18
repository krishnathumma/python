import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forcast App")
place = st.text_input("Place:")
days = st.slider("Forcast Days:", min_value=1, max_value=5, help="select the number of forcast days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} days in {place}")

if place:

    filtered_data = backend.get_data(place, days)

    if filtered_data != "city not found":
        if options == "Temperature":
            temperature = [dict["main"]["temp"] /10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "Y": "Temperature (C)"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in filtered_data ]
            st.image(images_path, width=115)
    else:
        st.write("Please Check Entered City Name !")
