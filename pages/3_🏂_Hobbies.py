import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Career",
    page_icon=":skateboard:"
    )

st.title("Hobbies")
st.write("---")
st.subheader("Skateboarding")

# tabs
tab1, tab2 = st.tabs(["Amazing 🤯", "Real 🥲"])

with tab1:
    video_file = open('images/am.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(
        video_bytes,
        end_time=7
        )

with tab2:
    video_file2 = open('images/sk.mp4', 'rb')
    video_bytes2 = video_file2.read()
    st.video(
        video_bytes2
        )


st.write("---")
# make some space
st.markdown("##")

# bottom image (centered)
c1, c2, c3 = st.columns(3)
with c2:
    st.image(
        "logos/rfd.png"
    )