import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def distribution(col_df):
    serie_1 = df[col_df]
    fig, ax = plt.subplots()
    st.dataframe(serie_1.describe())
    sns.set_style('darkgrid')
    sns.set_context('talk', font_scale= .8, rc={'grid.linewidth': 0.6})
    sns.violinplot(ax = ax, x = df['continent'], y = df[col_df]) 
    st.pyplot(fig)

def correlation(var_1, var_2):
    val_1, val_2 = df[var_1], df[var_2]
    fig, ax = plt.subplots()
    r_coef = np.corrcoef(x= val_1, y=val_2)
    st.write(f'Coefficient de corrélation de : {round(r_coef[0,1],3)}')
    sns.set_style('darkgrid')
    sns.set_context('talk', font_scale= .8, rc={'grid.linewidth': 0.6})

    sns.scatterplot(ax= ax, x=var_1, y=var_2, hue='continent', data=df)
    #ax.scatter(x=val_1, y=val_2)
    st.pyplot(fig)


df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

df['continent'] = df.continent.str.strip(' .')

st.title('Analyse des caracstérique de véhicules')

st.dataframe(df)

list_col = df.columns[(df.columns != 'continent') & (df.columns != 'year')]

print(list_col)
col_choice = st.selectbox(label='Choose a variable', options= list_col)

st.subheader(f'1- Distribution of variable {col_choice} for all countries :')
distribution(col_choice)


col_choice = st.multiselect(label='Choose two variables', options= list_col, default=['mpg', 'hp'])
print(col_choice)

st.subheader(f'2- Correlation of two variables ({col_choice[0]}, {col_choice[1]}) for all countries :')
correlation(col_choice[0], col_choice[1])


