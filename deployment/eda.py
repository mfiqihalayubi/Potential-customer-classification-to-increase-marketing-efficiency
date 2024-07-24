import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function 
def run():
    st.title('Selamat datang di bagian Exploratory Data Analysis')
# Memanggil data csv 
    df= pd.read_csv('bank.csv')

# Menampilakn 5 data teratas
    st.table(df.head(5))


# Menampilkan grafik distribusi data client berdasarkan status deposit
    st.title('Distribusi nilai sentimen')
    image1 = Image.open('distribusi_status_deposit.png')
    st.image(image1, caption='figure 1')

# Menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('''Dari grafik histogram di atas, kita dapat menyimpulkan jika kolom target hampir memiliki distribusi data yang seimbang (balance) antar 2 nilai nya ('yes' atau 'no'). Presentase 
                   client yang belum berinvestasi pada term deposit (deposito berjangka) setelah dihubungi oleh agen pemasaran adalah sebesar 53 %, sementara presentase client yang memutuskan untuk 
                   berinvestasi setelah dihubingi oleh agen pemasaran adalah sebesar 47 % (lebih rendah 6 % dibandingkan yang belum menggunakan). Ini artinya, pemasaran yang dilakukan oleh bank ini 
                   untuk membuat client berinvestasi pada term deposit memiliki keberhasilan sekitar 47 %.''')
        


# Menampilkan Presentase client yang dihubungi berdasarkan jenis pekerjaannya
    st.title('Presentase client yang dihubungi berdasarkan jenis pekerjaannya')
    image2 = Image.open('presentase_client_job.png')
    st.image(image2, caption='figure 2')

# Menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('''Dari grafik histogram di atas kita dapat melihat jika jenis pekerjaan client dengan presentase terbesar adalah pekerjaan management (23 %). Sementara itu, 3 pekerjaan lain yang memiliki presentase jumlah di atas 10 % adalah pekerjaan blue collar (buruh) dengan presentase sebesar 17 %, pekerjaan technician dengan presentase 16 %, dan pekerjaan admin dengan presentase 12 %. Keempat pekerjaan dengan presentase terbesar tersebut berasal dari 68 % dari total client yang dihubungi
                   Selain itu, terdapat beberapa client yang sebenarnya kurang tepat untuk dihubungi jika dilihat dari jenis atau status pekerjaannya. Client - client tersebut adalah client dengan status pensiun (7 %) dan client dengan status student (3 %). Kemungkinan hal ini terjadi karena data client yang akan dihubungi belum diperbaharui. 
                   Note : Saya belum memahami secara pasti apa yang dimaksud pekerjaan management pada dataset ini, tapi kemungkinan besar arti management yang dimaksud adalah semua pekerjaan yang difungsikan untuk mengatur aktivitas organisasi perusahaan baik dari segi operasional produksi, pemasaran, maupun oprasional perusahaan pada umumnya.''')
        


# Menampilkan grafik Distribusi data client berdsarkan umur
    st.title('Distribusi data client berdsarkan umur')
    image3 = Image.open('distribusi_client_age.png')
    st.image(image3, caption='figure 3')

# Menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('''Dari kedua grafik di atas, kita dapat mengambil kesimpulan jika mayoritas client memiliki umur di antara 20 hingga 50 tahun. Jika kita lihat pada rentang Q1 sampai Q3 pada 
                   grafik box plot, maka dapat disimpulkan jika 75 % client memiliki umur di atas 18 tahun dan di bawah 50 tahun. Selain itu, terdapat nilai ekstrim (outlier) pada atribut umur dimana 
                   terdapat sebagian kecil client yang memiliki umur di atas 75 tahun, bahkan kita dapat melihat client yang memiliki umur di atas 90 tahun. Sebuah pertanyaan mungkin akan muncul mengenai
                    kenapa agen pemasaran masih menawarkan term deposit pada client yang memiliki usia tidak produktif. Ada 2 kemungkinan mengapa hal ini terjadi. Pertama, dataset client yang digunakan 
                   untuk menghubungi client bukanlah dataset terupdate. Kedua, client pada usia non produktif tersebut memang masih aktif dalam melakukan transaksi perbankan dan client tersebut memiliki 
                   balance yang cukup tinggi. Jika kemungkinan kedua yang menjadi penyebabnya, maka hal ini tidak mengindikasikan suatu masalah. Namun jika kemungkinan pertama yang menjadi penyebabnya,
                    maka hal ini mengindikasikan adanya masalah dalam proses pengumpulan data client. Hal tersebut menjadi masalah karena memasarkan term deposit pada client dengan usia tidak produktif
                    tanpa alasan yang logis merupakan tindakan pemasaran yang tidak masuk akal dan hanya mengurangi efektivitas pemasaran.''')
        


# Menampilkan grafik Hubungan jenis pekerjaan dengan keputusan client dalam berinvestasi
    st.title('Hubungan jenis pekerjaan dengan keputusan client dalam berinvestasi')
    image4 = Image.open('presentase_agree_job.png')
    st.image(image4, caption='figure 4')

# Menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('''Dari grafik di atas kita dapat mengambil beberapa kesimpulan :
1. Sebagian besar client yang memutuskan untuk menginvestasikan uangnya pada instrumen term deposit memiliki pekerjaan (di level) management. Conversion rate yang didapatkan dalam melakukan penawaran pada client dengan pekerjaan ini adalah sebesar 50.7 %. Urutan kedua berasal dari pekerjaan technician dengan tingkat conversion rate sebesar 46.08 %, lalu diikuti dengan client yang memiliki pekerjaan sebagai blue collar dengan tingkat conversion rate sebesar 36.42 %, dan client yang memiliki pekerjaan sebagai admin dengan tingkat conversion rate sebesar 47.30 %

2. Jika dilihat dari conversion rate (presentase keberhasilan pemasara yang membuat client memutuskan untuk melakukan investasi), maka client dengan pekerjaan sebagai student, retired, dan unemployed menjadi client dengan tingkat conversion rate tertinggi dimana untuk student tingkat conversion ratenya sebesar 74.72 %, retired sebesar 66.32 %, dan unemployed sebesar 56.58 %. Hal ini cukup mengejutkan karena client - client dengan tingkat conversion rate tertinggi justru berasal dari client - client yang tidak memiliki pekerjaan aktif. Kemungkinan hal ini terjadi karena orang - orang yang tidak memiliki pekerjaan aktif lebih memilih untuk mengurangi konsumsinya dan memfokuskan sumber dayanya pada instument - instrument yang dapat menghasilkan pasive income''')
        


# Menampilkan grafik Distribusi loan status (personal dan housing) terhadap status deposit client
    st.title('Distribusi loan status (personal dan housing) terhadap status deposit client')
    image1 = Image.open('clientagree_loan_deposit.png')
    st.image(image1, caption='figure 5')

# Menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('''Dari data grafik di atas kita dapat menarik kesimpulan sebagai berikut :
1. Dari grafik sebelah kiri, kita dapat melihat jika sebagian besar client yang dihubungi oleh agen pemasaran memiliki status tidak memiliki personal loan. Client yang tidak memiliki personal loan dan menolak untuk berinvestasi jumlahnya sedikit lebih tinggi (4897 orang) dibandingkan client yang memiliki status loan yang sama namun memutuskan untuk melakukan investasi (4805). Artinya tidak ada korelasi positif antara status tidak memiliki personal loan dengan keputusan client dalam melakukan investasi

2. Dari grafik sebelah kanan, kita dapat melihat jika sebagian besar client yang memutuskan untuk melakukan investasi berasal dari kelompok yang tidak memiliki housing loan (3354 orang). Sementara itu, sebagian besar client yang memutuskan untuk tidak melakukan investasi berasal dari kelompok yang memiliki housing loan. Hal ini mengindikasikan bahwa client akan cenderung melakukan investasi term deposit jika mereka tidak memiliki housing loan''')