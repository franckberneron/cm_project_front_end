BUCKET_NAME     = 'wagon-data-739-tolyai'
FILE_VERSION    = '01'
FILE_NAME       = 'UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Affiliate Agreement.pdf'

import os
from google.cloud import storage


def storage_upload(pdf_file, local_path, rm=False):
    print(pdf_file)
    client = storage.Client().bucket(BUCKET_NAME)

    local_file_path = f'../cm_project_contracts_pdf/{pdf_file}'
    storage_location = f"pdf/{pdf_file}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(f'{pdf_file}')
#    blob.upload_from_filename(f'{local_file_path}')
    print(f"=> {pdf_file} uploaded to bucket {BUCKET_NAME} inside {storage_location}")
    if rm:
        os.remove(f'{pdf_file}')

if __name__ == '__main__' :
    storage_upload('UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Affiliate Agreement.pdf', '../cm_project_contracts_pdf/')

