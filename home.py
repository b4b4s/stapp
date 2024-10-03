import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(
    layout="wide",
    page_title="Elias",
    page_icon=":skateboard:",

    )

st.title("About Me")
st.write("---")

col1, col2 = st.columns(2)

# first column
with col1:
    st.markdown(":black_nib: **Name**: Elias Ortiz")
    st.markdown(":male-technologist: **Position**: Senior Geophysicist")
    st.markdown(":earth_americas: **Nationality**: Mexican")
    st.markdown(":round_pushpin: **Location**: Aberdeen")
    st.markdown("📊 **Interests**: Geophysics, Multivariate Statistics,\
                  Data Science & Machine Learning, Product Development")
    st.markdown("👍 **Hobbies**: Skateboarding, Sourdough & Cooking,\
                 Fantasy Premier League (435k 🥲)")

with col2:
    st.image("images/eq.png")


st.write("---")



