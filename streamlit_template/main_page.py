import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer or kart stats")

link = '<a href="https://tylerbarty.github.io/github_assignment/" target="_self" a>To my Github Pages Site</a>'
st.markdown(link, unsafe_allow_html=True)