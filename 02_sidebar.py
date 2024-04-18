import streamlit as st

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    st.write(add_radio)

with st.container(border=True):
    st.write("This is inside the container created using with notation")
    st.write(add_radio)

st.write(add_radio)
