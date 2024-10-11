import streamlit as st
import pandas
from pandas.util import capitalize_first_letter

st.set_page_config(layout="wide")

st.title("The Best Company")

content_info = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. 
Aliquam ante. Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. 
Etiam egestas wisi a erat. Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. 
Morbi scelerisque luctus velit. Cras pede libero, dapibus nec, pretium sit amet, tempor quis. 
Mauris tincidunt sem sed arcu. Duis condimentum augue id magna semper rutrum. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Donec quis nibh at felis congue commodo. Nulla accumsan, elit sit 
amet varius semper, nulla mauris mollis quam, tempor suscipit diam nulla vel leo. 
Nullam sapien sem, ornare ac, nonummy non, lobortis a enim. Aliquam erat volutpat. 
Vivamus luctus egestas leo. Curabitur bibendum justo non orci. In rutrum. Maecenas libero. 
Et harum quidem rerum facilis est et expedita distinctio.
"""

st.write(content_info)
st.subheader("**Our Team**")

col1, col2, col3, col4, col5 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        capital = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(capital)
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[4:8].iterrows():
        capital = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(capital)
        st.write(row["role"])
        st.image("images/"+row["image"])

with col5:
    for index, row in df[8:].iterrows():
        capital = row["first name"].capitalize() + " " + row["last name"].capitalize()
        st.header(capital)
        st.write(row["role"])
        st.image("images/"+row["image"])