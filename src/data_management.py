"""
Original code is from Code Institute walkthrough project, re-purposed
for this project
"""
import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib


def download_dataframe_as_csv(df):
    """
    Converts a DataFrame to a downloadable CSV link.
    """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" '
        f'download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href


def load_pkl_file(file_path):
    """
    Loads a pickle file from the specified path.
    """
    return joblib.load(filename=file_path)
