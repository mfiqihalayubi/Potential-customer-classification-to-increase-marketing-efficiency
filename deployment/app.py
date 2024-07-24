import streamlit as st
import eda
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Project   : Milestone 2')
    st.write('Nama      : Muhammad Fiqih Al-ayubi')
    st.write('Batch     : HCK - 017')
    st.write('Objectives: Membuat model yang dapat memprediksi keputusan client bank untuk melakukan investasi term deposit setelah proses telemarketing.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('''Untuk memasarkan produk investasi berupa term deposit (deposito berjangka) kepada clientnya, bank biasanya memiliki beragam cara untuk menawarkan produk tersebut dan
                    salah satunya adalah dengan telemarketing atau pemasaran produk dan jasa kepada pelanggan melalui telepon. Agen pemasaran (dalam konteks ini disebut telemarketer) pada umumnya akan mendapatkan
                   list berupa data - data client bank tersebut untuk memasarkan produknya melalui telepon. Namun seringkali data - data client yang diberikan tidak melalui proses seleksi terlebih dahulu sehingga
                   client - client yang tidak memiliki prospek dalam menggunakan produk perbankan ini tetap dihubungi oleh agen pemasaran. Hal seperti ini tentunya dapat membuat proses pemasaran menjadi tidak efisien dan dapat
                   meningkatkan cost per conversion (biaya pemasaran/konversi client). Oleh karena itu, dibutuhkan suatu cara untuk mengetahui apakah suatu client memiliki prospek dalam menggunakan instrumen term deposit.
                   Slaah satu caranya adalah dengan menggunakan model machine learning yang dapat memprediksi prospek atau tidaknya seorang client dalam melakukan investasi term deposit. Proses prediksi tersebut dinamakan
                   klasifikasi. Pada proses klasifikasi, model machine learning akan mempelajari data historis serta atribut client yang menolak dan yang setuju untuk menggunakan instrumen term deposit. 
                   Dari proses pembelajaran tersebut, model akan memiliki memori berupa ciri - ciri client yang prospek maupun yang tidak prospek untuk ditawarkan investasi.''')

    with st.expander("Kesimpulan"):
        st.caption('''Model terbaik yang dipilih pada kasus ini adalah model SVM. Dari 5 model yang dievaluasi hasil prediksinya pada mode default, model SVM menjadi model yang paling kecil skala overfittingnya. Berdasarkan hasil
                   hyperparameter tuning (pencarian hyperparameter optimal), maka model ini lebih optimal jika menggunakan kernel polynomial dengan degree = 2, gamma = 0.01, dan nilai C = 1.''')

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model .run()