

from numpy.random.mtrand import random
import streamlit 
import pandas
from libraries import *
import numpy as np
import pandas as pd



countries = ['USA', 'Australia', 'China', 'Spain', 'Egypt', 'Sri Lanka','France','Japan','Canada','Brazil','Italy','Russia']
data_types =['cases', 'deaths', 'recovered']

flag_codes={'USA':'us','Australia':'au','China':'cn','Egypt':'eg','Spain':'es','Sri Lanka':'lk','France':'fr','Japan':'jp','Canada':'ca','Brazil':'br','Italy':'it','Russia':'ru'}



streamlit.sidebar.title('Adjust the following Parameters')
country = streamlit.sidebar.selectbox('Pick a country', countries)
date=streamlit.sidebar.slider('Pick Number of days')
data_type = streamlit.sidebar.multiselect('Pick data types', data_types)


streamlit.sidebar.warning("Follow the health regulations")

cases__df = get_historic_cases(country,date)
deaths_df=get_historic_deaths(country, date)
recoveries_df=get_historic_recoveries(country, date)

historic_df=pandas.concat([cases__df,deaths_df,recoveries_df],axis=1).astype(int)


daily_cases_df = get_daily_cases(country,date)
daily_deaths_df=get_daily_deaths(country, date)
daily_recoveries_df=get_daily_recoveries(country, date)

daily_df=pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)

yersterday_cases = get_yesterday_cases(country)
yersterday_deaths=get_yesterday_deaths(country)
yersterday_recoveries=get_yesterday_recoveries(country)



streamlit.title("Meu Conqerrors")

streamlit.metric('Country',country)
streamlit.image(f'https://flagcdn.com/56x42/{flag_codes[country]}.png')

col1,col2,col3 = streamlit.columns(3)

col1.metric(label="Cases", value=yersterday_cases)
col2.metric(label="Deaths", value=yersterday_deaths)
col3.metric(label="Recoveries", value=yersterday_recoveries)

streamlit.line_chart(daily_df[data_type])







streamlit.video('https://www.youtube.com/watch?v=5DGwOJXSxqg')



streamlit.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://motionarray.imgix.net/preview-475499-eBceHCPaJ9-high_0000.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://motionarray.imgix.net/preview-475499-eBceHCPaJ9-high_0000.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


streamlit.write('Map data')
data_of_map = pd.DataFrame(
  np.random.random[36.66, -121.6],
  columns = ['latitude', 'longitude'])
streamlit.map(data_of_map)
