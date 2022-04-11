import streamlit as st
import pandas as pd
import altair as alt


DATA_URL = 'population_by_country_2020.csv'

ss = st.session_state.get(x=1)
    
if st.button("Increment x"):
    ss.x = ss.x + 1
    st.text(ss.x)
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")
st.subheader('Raw data')
st.write(data)
data.set_index('Country (or dependency)')
st.bar_chart(data['Population (2020)'])