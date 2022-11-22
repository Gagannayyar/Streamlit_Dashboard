import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="StreamLit Simple Dashboard",
    page_icon = "x",
    layout='wide'
)

st.markdown("KPI First Row")

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("First KPI")
    number1 = 123
    st.markdown(number1)


with kpi2:
    st.markdown("Second KPI")
    number2 = 233
    st.markdown(number2)

with kpi3:
    st.markdown("Third KPI")
    number3 = 5436
    st.markdown(number3)


st.markdown("KPI Second Row")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("First KPI")
    number1 = 123
    st.markdown(number1)


with kpi2:
    st.markdown("Second KPI")
    number2 = 233
    st.markdown(number2)

with kpi3:
    st.markdown("Third KPI")
    number3 = 5436
    st.markdown(number3)

with kpi4:
    st.markdown("fourth KPI")
    number4 = 7657
    st.markdown(number4)


st.markdown("Charts")

chart1, chart2 = st.columns(2)

with chart1:
    chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a","b","c"])
    st.line_chart(chart_data)

with chart2:
    chart_data = pd.DataFrame(np.random.randn(2000,3), columns=["x","y","z"])
    st.bar_chart(chart_data)