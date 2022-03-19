import streamlit as st
from uploader import storage_upload
from io import StringIO
import base64
import tempfile
# import pdfplumber
from pathlib import Path
import requests
import os
st.markdown('''
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
''', unsafe_allow_html=True)

# create credentials file
google_credentials_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

if not os.path.isfile(google_credentials_file):

    print(
        "write credentials file 🔥"
        + f"\n- path: {google_credentials_file}")

    # retrieve credentials
    json_credentials = os.environ["GOOGLE_CREDS"]

    # write credentials
    with open(google_credentials_file, "w") as file:

        file.write(json_credentials)

else:

    print("credentials file already exists 🎉")

def card(question, answer, score):
    return f'''
    <div class="card">
        <div class="card-header">
            {question}
        </div>
        <div class="card-body">
            <blockquote class="blockquote mb-0">
                <p>{answer}</p>
                <footer class="blockquote-footer">Confidence score: {score}%</footer>
            </blockquote>
        </div>
    </div>
    '''

st.title('The Contract Manager')

uploaded_file = st.file_uploader('Choose your .pdf file', type='pdf')
if uploaded_file is not None:
    with open(os.path.join(uploaded_file.name),'wb') as f:
        f.write((uploaded_file).getbuffer())
        storage_upload(f'{uploaded_file.name}', f'{uploaded_file.name}', rm=True)

    url = f'https://unicorn-jkpbyd77ba-ew.a.run.app/question?pdf_name={uploaded_file.name}'

    response = requests.get(url)

    prediction = response.json()

    if prediction:
        for question, content in prediction.items():
            #return card(question, content['answer'], content['score'])
            st.markdown(card(question, content['answer'], round(content['score']* 100, 2),), unsafe_allow_html=True)

        #        st.markdown (f"""#{question} """)
        #        st.markdown(f"""## answer: {content['answer']}""")
        #        st.markdown(f"""## confidence :{content['score']}""") 
