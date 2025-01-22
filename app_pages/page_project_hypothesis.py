import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write('### Project Hypothesis and Validation')

    st.success(
        "1. The cherry leaves on the farm with a fungal infection have white "
        "powdery marks which clearly differentiates them from a healthy leaf. "
        "We suspect this will allow a machine learning model to pick out the "
        "differences between the two sets of images we have.\n"
        "2. The client is expecting a minimum degree of accuracy of 97%. It is "
        "a high number however we are confident the model can reach the target "
        "set.\n"
        "3. It currently takes a worker on the farm around 30 minutes with each "
        "tree taking samples to check for infection. We believe a machine learning "
        "model can drastically cut down the amount of time it takes by instantly "
        "defining whether a leaf is healthy or not. We expect there to be an "
        "option to upload multiple images at once to further speed up the process.\n"
    )
    st.write('---')
    st.warning(
        "Upon validation of our machine learning model we have found it to be a "
        "success.\n"
        "1. Due to the clear visual differences between a healthy leaf and a "
        "non-healthy one the model was able to easily distinguish between the "
        "two possible outcomes.\n"
        "2. The accuracy of the model reached 100% which is above the predefined "
        "thresholds we agreed with the client and can therefore be considered a "
        "success. This is despite the fact there were no clear differences in "
        "in the average image of both a healthy leaf and an infected one.\n"
        "3. Due to the speed of the model to examine multiple images at once "
        "combined with its level of accuracy it will cut down on the amount of "
        "time it currently takes to check each tree. The ability to download "
        "the results will also help speed up applying the solution to the "
        "fungal infection.\n\n"
        "As a result, we consider the model a success and see no reason why it "
        "can't be used across the client's multiple farms around the country. "
        "Allowing the client to save multiple hours in examining the health "
        "of their crops.\n"
    )
