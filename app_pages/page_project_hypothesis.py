import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect cherry leafs, with a fungus, have clear signs of infection white powdery  "
        f"marks that clearly differentiate them from a healthy cherry leaf. \n\n"
        f"* An Image Montage shows the clear difference between a healthy leaf and a non-healthy one. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )