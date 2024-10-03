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

col1, col2, col3 = st.columns(3)

# first column
with col1:
    st.header("")

with col2:
    st.header("")

with col3:
    st.header("")

st.write("---")

st.subheader(
    ":black_nib: Name: Elias Ortiz"
    ":male-technologist: Position: Senior Geophysicist"
    ":earth_americas: Nationality: Mexican :flag-mx:"
)

