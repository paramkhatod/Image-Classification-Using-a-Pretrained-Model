# 🖼️ AI Image Classification

A simple image classification application using a pretrained MobileNetV2 deep learning model.

This project was developed as part of the CodeOrbit Tech Artificial Intelligence Internship.

## 📌 Project Overview

The application allows users to upload an image and uses a pretrained MobileNetV2 model to predict the contents of the image.

The application displays the top predicted classes along with their confidence scores.

## ✨ Features

- Upload JPG, JPEG and PNG images
- Pretrained MobileNetV2 model
- Image preprocessing
- Image classification
- Top 3 predictions
- Confidence scores
- Simple Streamlit interface

## 🛠️ Technologies Used

- Python
- TensorFlow
- MobileNetV2
- NumPy
- Pillow
- Streamlit

## 🧠 How It Works

The application follows this pipeline:

```text
Input Image
     ↓
Image Preprocessing
     ↓
Pretrained MobileNetV2
     ↓
Prediction
     ↓
Top 3 Classes
     ↓
Confidence Scores