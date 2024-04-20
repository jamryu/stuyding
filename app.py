import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("./data.csv")

st.title("H1 DRAM 공정 DX")


# Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "메뉴선택",
#     ("Email", "Home phone", "Mobile phone")


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "메뉴 선택",
        ("ECO STATUS 조회", "PCCB")
    )
    
if add_radio == 'ECO STATUS 조회':
    eco_num = st.selectbox(
        'ECO NUMBER',
        (df['eco'])
    )
    
    
    
    
    
    st.dataframe(df, use_container_width=False)

if add_radio == 'PCCB':
    PCCB_ITEM = st.selectbox(
        'PCCB item',
        ('선택하세요','MC','MOLD','M.OX')
    )
    




