import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* The cherry plantation crop from Farmy & Foods is facing a challenge where "
        f"the leaves on their cherry trees have been presenting powdery mildew.\n"
        f"* Currently, the process is manual verification of a given cherry tree whether "
        f"it contains powdery mildew. An employee spends around 30 minutes in each tree, "
        f" taking a few samples and verifying visually if the leaf is healthy or "
        f"has powdery mildew. \n"
        f"* If there is powdery mildew, the employee applies a specific compound to"
        f" kill the fungus. The time spent applying this compound is 1 minute. \n"
        f"* The company has thousands of cherry trees located on multiple farms  "
        f"across the country.\n\n"
        
        f"**Project Dataset**\n"
        f"* The dataset contains over four thousand images taken from the client's crop fields. "
        f"The images show healthy cherry leaves and cherry leaves that have powdery mildew, "
        f"a fungal disease that affects many plant species. ")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
        )