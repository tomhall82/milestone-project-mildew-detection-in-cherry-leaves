import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    """
    Loads the test evaluation file for a specific version.
    """
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')