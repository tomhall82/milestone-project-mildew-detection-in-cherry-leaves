import streamlit as st


def summary_body():

    st.write("### Brief Project Summary")

    st.info(
        f"**General Information**\n"
        f"Powdery mildew, caused by Podosphaera clandestina, is an obligate "
        f"biotrophic fungus that affects sweet and sour cherry trees. Mid- "
        f"and late-season sweet cherry cultivars (Prunus avium) are particularly "
        f"vulnerable to this disease, rendering the fruit unmarketable due to "
        f"the white fungal growth that appears on the surface of the cherries.\n"
        f"Initial symptoms of powdery mildew typically appear 7 to 10 days after "
        f"the first irrigation. These symptoms include light, roughly circular, "
        f"powdery patches on the young, susceptible leaves, which are newly "
        f"unfolded and light green in color. Older leaves, however, develop an "
        f"age-related resistance to powdery mildew, making them less prone to "
        f"infection.\n"
        f"Unlike many other fungi, powdery mildews do not require free water for "
        f"germination. However, fungal growth and germination are favored by high "
        f"humidity levels, as noted by Grove & Boal (1991a).\n"
        f"The current method of manually inspecting cherry trees for signs of "
        f"powdery mildew has been deemed time-inefficient. To address this "
        f"challenge, the client has requested the development of a Machine Learning "
        f"(ML) model that can predict, based on uploaded photographs, whether a "
        f"given cherry leaf shows signs of infection."
    )
    st.info(f"\n**Project Dataset**\n"
        f"* The available dataset contains 4208 images: "
        f"2104 each for both heathy leaves and ones infected with powdery mildew. "
        f"This dataset can be downloaded from "
        f"[Project Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )
    st.write(
        f"* For further information, please see the "
        f"[Project README file](https://github.com/tomhall82/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"""* 1 -  The client is interested in conducting a study to visually 
        differentiate a healthy cherry leaf from one with powdery mildew.\n"""
        f"""* 2 - The client is interested in predicting if a cherry leaf is 
        healthy or contains powdery mildew."""
    )