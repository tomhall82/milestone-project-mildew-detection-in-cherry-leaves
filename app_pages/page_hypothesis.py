import streamlit as st

def hypothesis_page():
    st.write("### Hypothesis and Validation")

    st.info(
        f"**Hypothesis:** Powdery mildew appears as a white, dusty coating on leaves, making them visually distinct from healthy leaves."
    )

    st.success(
        f"**Key Observations from Image Analysis:**\n\n"
        f"- **Image Montage:** Powdery mildew-affected leaves exhibit white patches and noticeable discoloration.\n"
        f"- **Average Image Comparison:** Infected leaves appear lighter in color overall.\n"
        f"- **Variability and Difference Analysis:**\n"
        f"  - Minimal variation in the central region of both leaves.\n"
        f"  - Healthy leaves show significant contrast variation in the middle, unlike affected leaves."
    )