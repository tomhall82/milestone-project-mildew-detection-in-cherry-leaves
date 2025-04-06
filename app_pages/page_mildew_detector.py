"""
Original code is from Code Institute walkthrough project, re-purposed
for this project
"""
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def detection_body():

    st.write("### Mildew Detection")

    st.info(
        f"* The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew."
    )

    st.write(
        f"* You can download a set of healthy and powdery mildew leaves for "
        f"live prediction. You can download the images from "
        f"[here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )

    st.write("---")

    images_buffer = st.file_uploader('Upload a cherry leaf image. \
                                     You may select more than one.',
                                     type='jpeg', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x \
                {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = pd.concat([df_report, pd.DataFrame
                                  ([{"Name": image.name, 'Result': pred_class}]
                                   )], ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
