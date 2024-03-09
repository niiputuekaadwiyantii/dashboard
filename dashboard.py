import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
import streamlit as st

# Load or define your day_df here (replace 'your_data.csv' with your actual data file)
day_df = pd.read_csv("all_data.csv")

def create_user_weather(df):
    result = df.groupby(by='weather_cond').agg({
        'count': ['max', 'min', 'mean', 'sum']
    })
    return result

def create_user_year(df):
    df['month'] = pd.Categorical(df['month'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)
    monthly_counts = df.groupby(by=["month","year"]).agg({
        "count": "sum"
    }).reset_index()
    return monthly_counts

def create_user_season(df):
    filtered_data_2012 = df[df["year"] == 2012]  # Replace '1' with '2012'
    return filtered_data_2012

def main():
    st.header('Projek Analisis Data: Bike Sharing')
    st.subheader('Course: Analysis Data with Python')
    st.subheader('1. Pengaruh cuaca terhadap jumlah pengguna sepeda')
    user_weather = create_user_weather(day_df)
    
    plt.figure(figsize=(8,6))
    sns.barplot(
        x='weather_cond',
        y='count',
        data=day_df
    )

    plt.title('Jumlah Pengguna Sepeda berdasarkan Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt.gcf())  # Pass the current figure to st.pyplot()

    st.subheader('Perbadingan jumlah pengguna sepeda pada tahun 2011 vs 2012')
    comparison_year = create_user_year(day_df)
    sns.lineplot(
        data=comparison_year,
        x="month",
        y="count",
        hue="year",
        palette="rocket",
        marker="o"
    )

    plt.title("Jumlah pengguna sepeda berdasarkan Bulan dan tahun")
    plt.xlabel(None)
    plt.ylabel(None)
    plt.legend(title="Tahun", loc="upper right")
    plt.tight_layout()
    st.pyplot(plt.gcf())  # Pass the current figure to st.pyplot()

    st.subheader('Pengaruh musim terhadap Jumlah Pengguna Sewa Sepeda baik Casual dan registered di tahun 2012')
    user_season = create_user_season(day_df)
    fig = px.bar(user_season, x="season", y="count", title="Pengaruh Musim terhadap Jumlah Pengguna Sewa Sepeda pada tahun 2012")
    fig.update_xaxes(title="musim")
    fig.update_yaxes(title="Jumlah Pengguna Sewa Sepeda (cnt)")

    st.plotly_chart(fig)

    st.subheader('Pengaruh suhu atau temperatur serta kelembapan terhadap pengguna sepeda baik casual dan registered')
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1)
    sns.scatterplot(
        x='temp',
        y='count',
        data=day_df,
        alpha=0.5
    )
    plt.title('Temperature vs Count')

    plt.subplot(1, 3, 2)
    sns.scatterplot(
        x='atemp',
        y='count',
        data=day_df,
        alpha=0.5
    )
    plt.title('Feels Like Temperature vs Count')

    plt.subplot(1, 3, 3)
    sns.scatterplot(
        x='hum',
        y='count',
        data=day_df,
        alpha=0.5
    )
    plt.title('Humidity vs Count')

    st.pyplot(plt.gcf())  # Pass the current figure to st.pyplot()

if __name__ == '__main__':
    main()
