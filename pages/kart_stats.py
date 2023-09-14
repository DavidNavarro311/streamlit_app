import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_krafter = pd.read_csv('data/kart_stats.csv')
st.dataframe(df_krafter)

df_krafter = df_krafter[['Body', 'Weight','Acceleration','Mini-Turbo', 'Ground Speed', 'Water Handling']]

st.dataframe(df_krafter.style
            .highlight_max(color='#56b77b', axis=0, subset=['Weight','Acceleration','Mini-Turbo', 'Ground Speed', 'Water Handling'])
            .highlight_min(color='#f44336', axis=0, subset=['Weight','Acceleration','Mini-Turbo', 'Ground Speed', 'Water Handling']))

st.bar_chart(df_krafter, x='Body', y=['Weight','Acceleration','Mini-Turbo','Ground Speed','Water Handling'], color=['#374C58', "#5A958A", "#BDD5BC", "#D8D0C1", '#F6612E'])

fig1 = px.scatter(df_krafter,x='Body', y='Ground Speed',color='Acceleration',width=900, size="Weight", hover_name="Body", color_continuous_scale=px.colors.diverging.BrBG)
st.plotly_chart(fig1, theme="streamlit", use_container_width=False)

chosen_kart = st.selectbox('Pick a Kart', df_krafter['Body'])
df_single_krafter = df_krafter.loc[df_krafter['Body'] == chosen_kart]
df_single_krafter = df_single_krafter.drop(columns=['Body'])
df_unp_krafter = df_single_krafter.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_krafter, x='category', y='strength', color= '#374C58')



