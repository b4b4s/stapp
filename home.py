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

col1, col2 = st.columns(2)

# first column
with col1:
    st.subheader(":black_nib: Name: Elias Ortiz")
    st.subheader(":male-technologist: Position: Senior Geophysicist")
    st.subheader(":earth_americas: Nationality: Mexican :flag-mx:")
    st.subheader("round_pushpin: Location: Aberdeen")
    st.subheader("📊 Interests: Geophysics, Multivariate Statistics\
                  Data Science & Machine Learning, Product Development")

with col2:
    st.header("")


st.write("---")



