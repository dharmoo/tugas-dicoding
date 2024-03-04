import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

day_df = pd.read_csv('dashboard/day_df.csv')
hour_df = pd.read_csv('dashboard/hour_df.csv')
img = Image.open("dashboard/Bike.jpeg")

st.header("Bike Sharing Dataset :sparkles:")


tab1,tab2 = st.tabs(["Performa Penyewaan Sepeda Tiap Bulan", "Perbandingan Jenis Sewa Sepeda Berdasarkan Musim"])

with st.sidebar:
    st.image(img,
             caption = "Sepeda Pak Dharmo",

             
             )
    st.write("Sepeda Pak Dharmo adalah tempat penyewaan khusus untuk sepeda. Pada tempat sewa Sepeda Pak Dharmo terdapat berbagai sepeda yang bisa disewa. Website ini adalah gambaran umum terkait performa bisnis yang ada pada tempat Sepeda Pak Dharmo.")


with tab1:
    pertanyaan_1 = day_df.groupby(['mnth', 'yr'])['cnt'].sum().unstack()
    plt.figure(figsize=(10, 6))
    plt.plot(pertanyaan_1.index, pertanyaan_1[0], label='2011', marker='o')
    plt.plot(pertanyaan_1.index, pertanyaan_1[1], label='2012', marker='o')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Sewa')
    plt.title('Performa Penyewaan Sepeda tiap Bulan')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(1, 13), labels=['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'], rotation=60)
    # plt.show()
    st.pyplot(plt)

with tab2:
    pertanyaan_2 = day_df.groupby('season')[['casual', 'registered']].sum()
    q2 = pertanyaan_2.plot(kind='bar', stacked=False, figsize=(10, 6))
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Sewa')
    plt.title('Perbandingan Jenis Sewa Sepeda berdasarkan Musim')
    plt.legend(title='Tipe', labels=['Casual', 'Registered'])
    plt.xticks(rotation=0)
    q2.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
    # plt.show()
    st.pyplot(plt)