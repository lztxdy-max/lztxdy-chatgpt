import streamlit as st

st.title("面试别慌！我陪你一起闯，从容应对！👫💼")

st.image("./streamlitt.jpg", width=680)

st.write("### 杰里盎司！")

if "a" not in st.session_state:
    st.session_state.a = 0
clicked = st.button("加1")
if clicked:
    st.session_state.a += 1
st.write(st.session_state.a)
print(st.session_state)
