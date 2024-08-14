import streamlit as st
import pandas as pd

st.title("面试别慌！我陪你一起闯，从容应对！👫💼")

st.image("./streamlitt.jpg", width=680)

st.write("## 杰里盎司！")

df = pd.DataFrame({"牌牌号": ["行01", "行02", "行03"],
                   "牌牌室": ["室一", "室二", "室三"],
                   "牌牌数": ["66", "88", "99"]})

st.dataframe(df)
st.divider()
st.table(df)
