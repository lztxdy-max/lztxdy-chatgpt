import streamlit as st

st.title("面试别慌！我陪你一起闯，从容应对！👫💼")

st.image("./streamlitt.jpg", width=680)

st.write("### 杰里盎司！")

name = st.text_input("请输入23号宇宙的识别码：")
if name:
    st.write(f"你好,{name}")

tab1, tab2, tab3 = st.tabs(["星云", "联系方式", "喜好水果"])
with tab1:
    nebula = st.radio("您的母星位于那片星云？",
             ["苜蓿-168", "黄芪-652", "崇山-758"],
             index=None)
    if nebula:
        st.write(f"你选择的星云是{nebula}")

with tab2:
    contact = st.selectbox("你希望通过什么方式联系？",
                 ["引力波", "黑洞析出电波", "常规宇宙电波", "量子纠缠", "其它"])
    st.write(f"好的，我们会通过{contact}的相关系统联系你，费用若超出预供经费，超出部分费用将由您个人承担！")

with tab3:
    fruits = st.multiselect("你喜欢的水果有那些？",
                            ["苹果", "香蕉", "橙子", "梨子", "西瓜", "葡萄", "其它"])
    for fruit in fruits:
        st.write(f"你选择的水果是{fruit},我们将通过这项选项了解您的星球概况！")

with st.expander("身高信息"):
    height = st.slider("你的身高是多少厘米？", value=170,
              min_value=100, max_value=230, step=1)
    st.write(f"你的身高是{height}厘米")

st.divider()
uploaded_file = st.file_uploader("上传文件", type=["py"])
if uploaded_file:
    st.write(f"你上传的文件是{uploaded_file.name}")
    st.write(f"文件内容如下：{uploaded_file.read()}")
