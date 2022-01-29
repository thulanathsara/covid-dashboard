


from pandas.core.frame import DataFrame
import streamlit as st 
import pandas 
from libraries import *
import numpy as np




countries = ['USA', 'Australia', 'China', 'Spain', 'Egypt', 'Sri Lanka','France','Japan','Canada','Brazil','Italy','Russia']
data_types =['cases', 'deaths', 'recovered']

flag_codes={'USA':'us','Australia':'au','China':'cn','Egypt':'eg','Spain':'es','Sri Lanka':'lk','France':'fr','Japan':'jp','Canada':'ca','Brazil':'br','Italy':'it','Russia':'ru'}

st.sidebar.markdown("<h1 style='text-align: center;'>🦠 Ajust the following Parameters 😷</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

country = st.sidebar.selectbox('Pick a country', countries)
date=st.sidebar.slider('Pick Number of days')
data_type = st.sidebar.multiselect('Pick data types', data_types)
st.sidebar.warning("Follow the health regulations")


st.markdown("<h1 style='text-align: center;'>🦠 Covid-19 Dashboard 😷</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)




cases__df = get_historic_cases(country,date)
deaths_df=get_historic_deaths(country, date)
recoveries_df=get_historic_recoveries(country, date)
historic_df=pd.concat([cases__df,deaths_df,recoveries_df],axis=1).astype(int)
daily_cases_df = get_daily_cases(country,date)
daily_deaths_df=get_daily_deaths(country, date)
daily_recoveries_df=get_daily_recoveries(country, date)
daily_df=pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)
yersterday_cases = get_yesterday_cases(country)
yersterday_deaths=get_yesterday_deaths(country)
yersterday_recoveries=get_yesterday_recoveries(country)





st.metric('Country',country)
st.image(f'https://flagcdn.com/56x42/{flag_codes[country]}.png')

col1,col2,col3 = st.columns(3)

col1.metric(label="Cases", value=yersterday_cases)
col2.metric(label="Deaths", value=yersterday_deaths)
col3.metric(label="Recoveries", value=yersterday_recoveries)

st.line_chart(daily_df[data_type])







st.video('https://www.youtube.com/watch?v=I-Yd-_XIWJg')


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/R.832ad698cefce55904803a9d58be78d6?rik=%2bjSWc30rnXCtyw&pid=ImgRaw&r=0")
    }
   .sidebar .sidebar-content {
        background: url("https://www.shutterstock.com/image-illustration/coronavirus-covid19-under-microscope-3d-rendered-1931363474.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


import _json
st.image("https://th.bing.com/th/id/R.1f1efbe58fcb1dc48d5a4e9971cef973?rik=hZRO%2bkqJqIHnPA&riu=http%3a%2f%2fwww.hdwallpaperspulse.com%2fwp-content%2fuploads%2f2020%2f04%2fdigital-Stay-Safe-Images.png&ehk=JtyLIrM0B1Od02EUhOnizhwJwcqSBUWrYKjruhbYXvU%3d&risl=&pid=ImgRaw&r=0")