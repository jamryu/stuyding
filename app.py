import streamlit as st
import pandas as pd
import numpy as np


st.title("H1 DRAM 공정 DX")

eco = pd.read_csv("./eco_list.csv")
# eco 오름차순으로 필터링 필요
lot = pd.read_csv('./lot_list.csv')


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "메뉴 선택",
        ("ECO STATUS 조회", "PCCB")
    )
    
# ==============ECO STATUS WIDGET 동작 ===============
if add_radio == 'ECO STATUS 조회':
    # ECO LIST SELEC BOX
    eco_num = st.selectbox(
        'Choose ECO number',
        (eco['eco'])
    )
    
    # ECO 진행 LOT STATUS 반환
    st.dataframe(lot[lot['eco_num']==eco_num])
    ### wafer_id 까지 나와서 너무 많음.. 회사 status 데이터는 lot 까지만 나와서 문제없어보임



# ===============PCCB WIDGET 동작===============
if add_radio == 'PCCB':
    PCCB_ITEM = st.selectbox(
        'PCCB item',
        ('선택하세요','MC','MOLD','M.OX')
    )
    




