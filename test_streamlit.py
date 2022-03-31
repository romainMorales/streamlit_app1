import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt

def distribution(col_df):
    serie_1 = df[col_df]
    st.dataframe(serie_1.describe())
    st.plotly_chart(plt.hist(serie_1))


def correlation(serie_1, serie_2):
    val_1, val_2 = df[serie_1], df[serie_2]
    r_carre = np.corrcoef(x= val_1, y=val_2)
    st.dataframe(r_carre)
    st.plotly_chart(plt.scatter(x=val_1, y=val_2))

df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

df['continent'] = df.continent.str.strip(' .')


st.title('Analyse des caracstérique de véhicules')

st.header('\ Distribution ')
mpg_analyse = distribution('mpg')
st.write(mpg_analyse)

time60_analyse = distribution('time-to-60')
st.write(time60_analyse)

st.header('\ Corrélation ')
mpg_hp_cor = correlation('mpg', 'hp')
st.write(mpg_hp_cor)