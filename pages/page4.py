import streamlit as st

st.title("面试别慌！我陪你一起闯，从容应对！👫💼")

st.image("./streamlitt.jpg", width=680)

st.write("### 杰里盎司！")

with st.sidebar:
    name = st.text_input("请输入23号宇宙的识别码：")
    if name:
        st.write(f"你好,{name}")

column1, column2, column3 = st.columns([1, 2, 1])

with column1:
    password = st.text_input("请输入23号宇宙的密码：", type="password")

with column2:
    paragraph = st.text_area("请输入一段自我介绍：")

with column3:
    age = st.number_input("请输入宇宙初始年龄：", value=20, min_value=0, max_value=160, step=6)
    st.write(f"你的年龄是：{age}岁")

st.divider()
checked = st.checkbox("我同意以上条款")
if checked:
    st.write("感谢你的同意！")

st.divider()
submitted = st.button("提交")
if submitted:
    st.write("提交成功！")
