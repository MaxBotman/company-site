import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("There has to be text here but I dont really know what to type")
st.subheader("Our Team")

df = pd.read_csv("data.csv", sep=",")

col1, empty_1, col2, empty_2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

