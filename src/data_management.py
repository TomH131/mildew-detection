import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib
import boto3


def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)


def download_model():
    # Create S3 client
    s3 = boto3.client('s3')
    
    # Define the bucket and key for your model file
    bucket_name = "mildew-detection" 
    model_key = "outputs/v1/mildew_detector_model.keras"
    
    # Download the model file from S3 and save it locally as model.h5
    s3.download_file(bucket_name, model_key, "mildew_detector_model.keras")

    print("Model downloaded successfully!")

