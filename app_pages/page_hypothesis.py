import streamlit as st


def hypothesis_body():
    st.write("### Hypothesis and Validation")

    st.info(
        f"**Hypothesis 1:** Powdery mildew appears as a white, dusty "
        f"coating on leaves, making them visually distinct from "
        f"healthy leaves."
    )

    st.success(
        f"**Key Observations from Image Analysis:**\n\n"
        f"- **Image Montage:** Powdery mildew-affected leaves exhibit "
        f"white patches and noticeable discoloration.\n"
        f"- **Average Image Comparison:** Infected leaves appear "
        f"lighter in color overall.\n"
        f"- **Variability and Difference Analysis:**\n"
        f"  - Minimal variation in the central region of both leaves.\n"
        f"  - Healthy leaves show significant contrast variation in the "
        f"middle, unlike affected leaves."
    )

    st.info(
        f"**Hypothesis 2:** An ML system trained on cherry leaf "
        "images can accurately predict that a cherry leaf is "
        "healthy or  infected with mildew with at least 90% accuracy."
    )

    st.success(
        f"This has been verified through the ML Prediction Metrics which show "
        f"99% accuracy."
    )

    st.info(
        f"**Hypothesis 3:** Implementing a machine learning solution for "
        "cherry leaf inspection will improve the accuracy and speed of "
        "detecting powdery mildew, leading to reduced reliance on manual "
        "labor, cost savings, enhanced productivity, and increased worker "
        "safety by minimizing exposure to potential environmental hazards."
    )

    st.warning(
        f"While we won't fully understand all aspects of this hypothesis "
        f"until we have been able to compare cost etc. until we can inspect "
        f"performance metrics both before and after the ML model has been "
        f"introduced. That said, it s reasonable to assume speed, accuracy "
        f"and safety will all be positively impacted."
    )
    