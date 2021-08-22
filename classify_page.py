import streamlit as st
import torch
import numpy as np
from PIL import Image

@st.cache
def load_model(path_to_model):
    # return model
    pass

def show_classify_page(model):
    st.title("Biopsy Stomachs classifications")
    uploaded_file = st.file_uploader(label="Upload an image for classification",type=("jpg", "tif", "jpeg", "png"))
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        # mean bag length value
        mbl = st.slider('Fast-Slow', 10, 100, 100)
        classify_btn = st.button("Classify!")
        if classify_btn:
            # input the image to model
            # output of the model, classification
            st.write("")
            st.write("Classifying...")
            classification = model(uploaded_file)
            st.write('Classification:    %s (%.2f%%)' % (classification[1], classification[2]*100))
            



