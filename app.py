import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions
)

st.set_page_config(
    page_title="AI Image Classifier",
    page_icon="🖼️"
)

st.title("🖼️ AI Image Classifier")
st.write("Upload an image and let the pretrained AI model classify it.")

@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if file:

    image = Image.open(file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((224, 224))

    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    prediction = model.predict(x, verbose=0)

    results = decode_predictions(prediction, top=3)[0]

    st.subheader("Prediction")

    for _, label, confidence in results:
        st.write(
            f"**{label.replace('_', ' ').title()}** — "
            f"{confidence * 100:.2f}%"
        )