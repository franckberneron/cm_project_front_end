import streamlit as st
from uploader import storage_upload
from io import StringIO
import base64
import tempfile
# import pdfplumber
from pathlib import Path
import requests

uploaded_file = st.file_uploader('Choose your .pdf file', type='pdf')
if uploaded_file is not None:
    with open(os.path.join(uploaded_file.name),'wb') as f:
        f.write((uploaded_file).getbuffer())
        storage_upload(f'{uploaded_file.name}', f'{uploaded_file.name}', rm=True)



pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)


# enter here the address of your flask api
url = 'https://taxifare.lewagon.ai/predict'

params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

response = requests.get(url, params=params)

prediction = response.json()

pred = prediction['fare']

pred
