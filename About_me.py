import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(
    layout="wide",
    page_title="Hello!",
    page_icon="👋",

    )

st.title("About Me")
st.write("---")

col1, col2 = st.columns(2)

# first column
with col1:
    st.markdown("**Geophysicist & Data Scientist** with 11 years of experience in the oil and gas industry. \
                I worked on projects across international locations including: Azerbaijan, Oman, Egypt, \
                Morocco, Mexico, and U.K.. I enjoy distilling complex concepts into simple, clear terms. \
                 I find it fascinating that combining quantitative and qualitative approaches provides a \
                deeper understanding of the subsurface, as neither can reveal the complete picture on its own.")
    st.markdown(":black_nib: **Name**: Elias Ortiz")
    st.markdown(":male-technologist: **Position**: Senior Geophysicist")
    st.markdown(":earth_americas: **Nationality**: Mexican")
    st.markdown(":round_pushpin: **Location**: Aberdeen")
    st.markdown("📊 **Interests**: Geophysics, Multivariate Statistics,\
                  Data Science & Machine Learning, Product Development")
    st.markdown("👍 **Hobbies**: Skateboarding, Sourdough & Cooking,\
                 Fantasy Premier League (435k 🥲)")

# second column
with col2:
    st.image("images/eq.png")

st.write("---")

# make some space
st.markdown("##")

# bottom image (centered)
c1, c2, c3 = st.columns(3)
with c2:
    st.image(
        "logos/rfd.png"
    )




