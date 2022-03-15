import streamlit as st
from uploader import storage_upload
from io import StringIO
import base64
import tempfile
# import pdfplumber
from pathlib import Path
uploaded_file = st.file_uploader('Choose your .pdf file', type='pdf')
if uploaded_file is not None:
    with open(os.path.join(uploaded_file.name),'wb') as f:
        f.write((uploaded_file).getbuffer())
        storage_upload(f'{uploaded_file.name}', f'{uploaded_file.name}', rm=True)
    #  with pdfplumber.open(uploaded_file) as pdf:
     # Make temp file path from uploaded file
        # with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        #     st.markdown(“## Original PDF file”)
        #     fp = Path(tmp_file.name)
        #     print(fp)
            # fp.write_bytes(uploaded_file.getvalue())
            # st.write(show_pdf(tmp_file.name))
            # imgs = convert_from_path(tmp_file.name)
            # st.markdown(f”Converted images from PDF”)
            # st.image(imgs)