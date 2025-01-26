import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file
import requests
import boto3
import io


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Healthy': 0, 'Powdery Mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    
    # Add a unique key to avoid Streamlit errors
    st.plotly_chart(fig, key=f"plot_{pred_class}_{np.random.randint(1000)}")


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/mildew_detector_model.keras")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample cell is "
        f"**{pred_class.lower()}**.")

    return pred_proba, pred_class


model = None

def load_model_from_s3(bucket_name, model_key):
    global model
    try:
        if model is None:  # Check if the model is already loaded
            # Initialize boto3 S3 client
            s3_client = boto3.client('s3')
            
            # Download the model from the S3 bucket
            model_obj = s3_client.get_object(Bucket=bucket_name, Key=model_key)
            
            # Read model file into memory and load the model
            model_data = model_obj['Body'].read()
            model = tf.keras.models.load_model(io.BytesIO(model_data))
            
            print("Model loaded successfully!")
        
        return model
    except Exception as e:
        st.error(f"Error loading model from S3: {e}")
        return None


def get_prediction(input_data):
    try:
        # Load model (Only needs to be done once)
        model = load_model_from_s3('mildew-detection', 'mildew_detector_model.keras')
        
        if model is None:
            return None
        
        # Ensure input_data is preprocessed before passing it to the model
        # For example, if input_data is an image, ensure it’s resized, normalised, etc.
        
        prediction = model.predict(input_data)
        
        return prediction
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        return None