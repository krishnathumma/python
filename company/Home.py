import streamlit as st
import pandas as pa

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """You become a temporary resident when you are legally authorized by Immigration, Refugees and Citizenship Canada to enter Canada for temporary purposes,
such as a visitor, student, worker or temporary resident permit holder. You were given a confirmation document (such as a visitor record, a temporary resident
permit, or a study permit) that shows a start date and an expiry date.
As a temporary resident (as defined in the Immigration and Refugee protection Act), you or your spouse or common-law partner must meet both of the following
requirements for Canada child benefit (CCB) purposes only
"""
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

data = pa.read_csv("data.csv")

with col1:
    for index, row in data[:4].iterrows():
        print(row)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in data[4:8].iterrows():
        print(row)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])  

with col3:
    for index, row in data[8:12].iterrows():
        print(row)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])              