import streamlit as st
import pandas as pa

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Balakrishna Thumma")
    content = """Hi, I am Balakrishna Thumma, and I am a Seasoned Senior Software Engineer with 9 years of experience in full-stack development, project management, and system optimization. Proficient in PHP, Laravel, YII,  NodeJs, and front-end technologies like VueJs, and React.js; adept at automating processes and enhancing software functionality, seeking a Senior Software Engineer role to leverage expertise in developing robust solutions and leading technical teams
    """
    st.info(content)

message = """The date you became a resident of Canada is the date you established significant residential ties in Canada. This date is usually when you arrived in Canada.
Significant residential ties include"""

st.write(message)

cola, empty_col, colb = st.columns([1.5, 0.5, 1.5])

data = pa.read_csv("data.csv", sep=";")
with cola:
    for index, row in data[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write("[Source Code](" + row['url'] + ")")

with colb:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
