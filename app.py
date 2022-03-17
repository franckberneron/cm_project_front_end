import streamlit as st
from uploader import storage_upload
from io import StringIO
import base64
import tempfile
# import pdfplumber
from pathlib import Path
import requests
import os


uploaded_file = st.file_uploader('Choose your .pdf file', type='pdf')
if uploaded_file is not None:
    with open(os.path.join(uploaded_file.name),'wb') as f:
        f.write((uploaded_file).getbuffer())
        storage_upload(f'{uploaded_file.name}', f'{uploaded_file.name}', rm=True)

    url = f'https://unicorn-jkpbyd77ba-ew.a.run.app/question?pdf_name={uploaded_file.name}'

    response = requests.get(url)

    prediction = response.json()

    for question, content in prediction.items():
        st.markdown (f"""#{question} """)
#        for content_item in content.items():
        st.markdown (f"""answer: {content['answer']}""")
        st.markdown (f"""confidence :{content['score']}""")

 