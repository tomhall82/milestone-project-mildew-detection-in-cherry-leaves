"""
Original code is from Code Institute walkthrough project, re-purposed
for this project
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics():
    """
    Displays the machine learning model's performance metrics.
    """
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    # Correctly load the image using plt.imread
    labels_distribution = plt.imread(
        f"outputs/{version}/"
        "labels_distribution.png"
    )

    st.image(
        labels_distribution,
        caption=(
            'Labels Distribution on Train, '
            'Validation and Test Sets'
        )
    )

    st.info(
        f"* The dataset was split into three parts: a training set, a test "
        f"set, and a validation set. This is the standard approach for "
        f"dividing data in Machine Learning.\n"
        f"* The training set, being the largest, was the first data the ML "
        f"model encountered. Its larger size ensures that the model is "
        f"exposed to enough data to fully learn the distinctions between "
        f"the two types of images.\n"
        f"* The validation set was then used to fine-tune the model's "
        f"performance.\n"
        f"* Finally, the test set served as the ultimate check to confirm "
        f"that the model can handle new data and has learned as expected."
    )
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.info(
        f"* As shown in the graphs above, the model generally achieved a "
        f"high level of accuracy.\n"
        f"* The model's performance on the training set initially improved "
        f"rapidly. There was a slight dip in performance at epoch 3 however, "
        f"the model regained accuracy in the following epoch and continued "
        f"to improve.\n"
        f"* The loss graph, which measures how closely the model's "
        f"predictions match the actual outcomes, indicates adequate "
        f"performance on both the training and validation sets. "
        f"Additionally, overfitting has been kept to a minimum."
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                              index=['Loss', 'Accuracy']))
    st.info(
        f"* At the start of the project, the client requested an ML model "
        f"capable of predicting with 97% accuracy whether a leaf had mildew "
        f"or not based on its image.\n"
        f"* As shown in the table above, the model predicted the status of "
        f"images in the test dataset with 99% accuracy, meaning this "
        f"requirement has been successfully met."
    )
