import streamlit as st
from PIL import Image
import os

from src.inference import load_model, run_inference_single
from utils.image_processing import process_image

MODEL_PATH = './models/best1.pt'
model = load_model(MODEL_PATH)

st.set_page_config(
    page_title='Helmet Safety Detection App',
    # page_icon='👷🏻‍♂️👷🏻',
    # layout='wide',
    initial_sidebar_state='expanded',
)

st.title('Helmet Safety Detection App')
st.write('Upload an image to detect helmets.')

uploaded_file = st.file_uploader(
    'Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open(uploaded_file)
        st.image(uploaded_file,
                 caption='Uploaded Image',
                 use_column_width=True)

    with col2:
        with st.spinner('Detecting...'):
            img_out = process_image(run_inference_single(model, img))
        st.image(img_out,
                 caption='Output Image',
                 use_column_width=True)
        
        
        
        
