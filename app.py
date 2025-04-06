import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import summary_body
from app_pages.page_data_visualiser import data_visualiser_body
from app_pages.page_mildew_detector import detection_body
from app_pages.page_hypothesis import hypothesis_body
from app_pages.page_ml_performance import ml_performance_metrics

# Create an instance of the app
app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", summary_body)
app.add_page("Cells Visualiser", data_visualiser_body)
app.add_page("Mildew Detection", detection_body)
app.add_page("Project Hypothesis", hypothesis_body)
app.add_page("ML Performance Metrics", ml_performance_metrics)

app.run()  # Run the app
