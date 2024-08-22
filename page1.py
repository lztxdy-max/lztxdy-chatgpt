import streamlit as st
import pandas as pd

st.title("💬 庄家通吃，推牌重开！")

st.image("./streamlitt.jpg", width=680)

st.write("## 杰里盎司！")

df = pd.DataFrame({"牌牌号": ["行01", "行02", "行03"],
                   "牌牌室": ["室一", "室二", "室三"],
                   "牌牌数": ["66", "88", "99"]})

st.dataframe(df)
st.divider()
st.table(df)
