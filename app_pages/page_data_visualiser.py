"""
Original code is from Code Institute walkthrough project, re-purposed
for this project
"""

import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")


def data_visualiser_body():
    st.write("### Data Visualiser")
    st.info(
        f"* The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(
            f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            f"Average Image shows that powdery-mildew affected leaves appear "
            f"lighter in color. The variability image highlights a purple hue "
            f"around the edges of healthy leaves, while the affected leaves "
            f"show a darker edge. The healthy leaves also display more color "
            f"variation in the middle, whereas the affected leaves have a "
            f"more uniform appearance. Overall, the lighter color of the "
            f"affected leaves makes the difference subtle and not very "
            f"noticeable."
        )

        st.image(avg_mildew,
                 caption='Leaf Infected with Powdery Mildew- Average and '
                 'Variability')
        st.image(avg_healthy,
                 caption='Healthy Leaf- Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average powdery mildew and average "
                   "healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"This study demonstrates clear patterns that differentiate "
            f"between the two types of leaves. A visible distinction is "
            f"observed around the edges of the leaves, which helps in making "
            f"the differentiation more apparent. However, there is less color "
            f"variation in the middle sections of both types of leaves, "
            f"particularly in the darker middle areas. This reduced variation "
            f"in color makes it challenging to distinguish between the leaves "
            f"based on the central portions."
            )
        st.image(diff_between_avgs, caption='Difference between average \
                 images')

    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' "
                 "button")
        data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")
