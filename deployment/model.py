import streamlit as st
import pandas as pd
import pickle
import sklearn

def run():

    # load model
    with open('model.pkl', 'rb') as model:
        model = pickle.load(model)

    age = st.number_input('Age', min_value=18, max_value=100)
    job = st.selectbox('Job', options=['technician', 'management', 'retired', 'student', 'unemployed', 'admin', 'services', 'blue-collar', 'enterpreneur', 'housemaid', 'unknown', 'self-employed']),
    marital = st.selectbox('Marital status', options=['married', 'divorced', 'single']),
    education = st.selectbox('Education', options=['primary', 'tertiary', 'secondary', 'unknown']),
    default = st.selectbox('Default status',options=['yes', 'no']),
    balance = st.number_input('Balance', min_value=0.0, max_value=80000.0),
    housing = st.selectbox('Has housing loans ?',options=['no', 'yes']),
    loan = st.selectbox('Has personal loan ?',options=['no', 'yes']),
    contact = st.selectbox('Contacted by',options=['unknown', 'cellular', 'cellular', 'telephone', 'cellular']),
    day = st.number_input('Day',min_value=1, max_value=31),
    month = st.selectbox('Month', options=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']),
    duration = st.number_input('Call duration (sec)',min_value=2, max_value=3881),
    campaign = st.number_input('How many campaign that have been conducted ?',min_value=1, max_value=63),
    pdays = st.number_input('Number of days passed from previous campaign',min_value=0, max_value=854),
    previous = st.number_input('Number of contacts performed before',min_value=0, max_value=58),
    poutcome = st.selectbox('Previous result',options=['unknown', 'success','other', 'failure'])

    st.markdown('**Berikut adalah data yang telah kamu input :**')
    
 
    dataInf = pd.DataFrame({
        'age' : age,
        'job' : job,
        'marital' : marital,
        'education' : education,
        'default' : default,
        'balance' : balance,
        'housing' : housing,
        'loan' : loan,
        'contact' : contact,
        'day' : day,
        'month' : month,
        'duration' : duration,
        'campaign' : campaign,
        'pdays' : pdays,
        'previous' : previous,
        'poutcome' : poutcome
    }, index=[0])

    st.table(dataInf)


    if st.button(label='Predict'):
        # data dummy prediction
        yPred_inf = model.predict(dataInf)

        # result of prediction
        if yPred_inf[0] == 0:
            st.write('Bukan client potensial')

        else:
            st.write('Client potensial')



