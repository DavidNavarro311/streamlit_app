import streamlit as st
import pandas as pd

st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# This is Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')

df_racer = pd.read_csv('data/racer_stats.csv')

#st.write(df_racer)

st.dataframe(df_racer.style
            .highlight_max(color='lightgreen', axis=0, subset=['Speed', 'Acceleration', 'Weight','Handling', 'Traction/Grip', 'Mini-Turbo', 'Times First Place', 'Total Races'])
            .highlight_min(color='red', axis=0, subset=['Speed', 'Acceleration', 'Weight','Handling', 'Traction/Grip', 'Mini-Turbo', 'Times First Place', 'Total Races']))

st.line_chart(df_racer, x= 'Speed', y = ['Acceleration', 'Weight', 'Handling', 'Traction/Grip', 'Mini-Turbo'])

st.header('Racer speed does not seem to correlate to numbert of races they win')
x = st.slider('How many Racers to show', 1, len(df_racer))

st.write('Racers by Speed')
#df_fastest_Racer = df_racer[['Character', 'Speed']].sort_values('Speed', ascending) = False.iloc[0:x]
#st.dataframe(df_fastest_racer)