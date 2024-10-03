import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Career",
    page_icon=":skateboard:"
    )

st.title("Hobbies")
st.write("---")

video_file = open('images/am.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


st.write("---")
# make some space
st.markdown("##")

# bottom image (centered)
c1, c2, c3 = st.columns(3)
with c2:
    st.image(
        "logos/rfd.png"
    )