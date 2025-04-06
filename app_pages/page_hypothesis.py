import streamlit as st

def hypothesis_body():
    st.write("### Hypothesis and Validation")

    st.info(
        f"**Hypothesis 1:** Powdery mildew appears as a white, dusty coating on "
        f"leaves, making them visually distinct from healthy leaves."
    )

    st.success(
        f"**Key Observations from Image Analysis:**\n\n"
        f"- **Image Montage:** Powdery mildew-affected leaves exhibit white patches and noticeable discoloration.\n"
        f"- **Average Image Comparison:** Infected leaves appear lighter in color overall.\n"
        f"- **Variability and Difference Analysis:**\n"
        f"  - Minimal variation in the central region of both leaves.\n"
        f"  - Healthy leaves show significant contrast variation in the middle, unlike affected leaves."
    )

    st.info(
        f"**Hypothesis 2:** An ML system trained on cherry leaf images can accurately "
        "predict that a cherry leaf is healthy or  infected with mildew with "
        "at least 90% accuracy."
    )

    st.success(
        f"This has been verified through the ML Prediction Metrics which show "
        f"99% accuracy."
    )

    st.info(
        f"**Hypothesis 3:** Implementing a machine learning solution for cherry "
        "leaf inspection will improve the accuracy and speed of detecting powdery "
        "mildew, leading to reduced reliance on manual labor, cost savings, enhanced "
        "productivity, and increased worker safety by minimizing exposure to "
        "potential environmental hazards."
    )

    st.warning(
        f"While we won't fully understand all aspects of this hypothesis until "
        f"we have been able to compare cost etc. until we can inspect performance metrics "
        f"both before and after the ML model has been introduced. That said, it "
        f"is reasonable to assume speed, accuracy and safety will all be positively "
        f"impacted."
    )