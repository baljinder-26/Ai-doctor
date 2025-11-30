import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
import cv2

def lung():
    # Set page configuration
    # st.set_page_config(
    #     page_title="Lung Disease Classifier",
    #     page_icon="🫁",
    #     layout="wide",
    #     initial_sidebar_state="expanded"
    # )
    discord_bg_url="https://t3.ftcdn.net/jpg/09/07/52/90/360_F_907529080_Rvvk1QtI2BGnLqA6yolZhVtfz697U4bl.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{discord_bg_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Optional: Make widgets slightly transparent */
        .stApp > div {{
            background-color: rgba(0, 0, 0, 0.4);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }}

        /* Optional: Customize headers */
        h1, h2, h3, h4, h5, h6 {{
            color: #7289da;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # Custom CSS for better styling
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .result-box {
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid;
        }
        .normal {
            background-color: #d4edda;
            border-color: #28a745;
            color: #155724;
        }
        .pneumonia {
            background-color: #f8d7da;
            border-color: #dc3545;
            color: #721c24;
        }
        .upload-box {
            border: 2px dashed #ccc;
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            margin: 20px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    @st.cache_resource
    def load_trained_model():
        """Load the trained model with caching"""
        try:
            model = load_model("our_model.h5")
            return model
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None

    def preprocess_image(image):
        """Preprocess the uploaded image for prediction"""
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize image
        image = image.resize((224, 224))

        
        # Convert to array and normalize
        img_array = np.array(image) / 255.0
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        return img_array

    def predict_image(model, image):
        """Make prediction on the image"""
        try:
            # Preprocess image
            processed_image = preprocess_image(image)
            
            # Make prediction
            predictions = model.predict(processed_image, verbose=0)
            
            # Get probabilities
            normal_prob = predictions[0][0]  # Assuming index 1 is NORMAL
            pneumonia_prob = predictions[0][1]  # Assuming index 0 is PNEUMONIA
            
            # Get predicted class
            class_idx = np.argmax(predictions[0])
            class_names = {0: "NORMAL", 1: "PNEUMONIA",}
            predicted_class = class_names[class_idx]
            confidence = max(normal_prob, pneumonia_prob) * 100
            
            return predicted_class, confidence, normal_prob, pneumonia_prob
            
        except Exception as e:
            st.error(f"Prediction error: {e}")
            return None, 0, 0, 0

    # Main header
    st.markdown('<h1 class="main-header">🫁 Lung Disease Classifier</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This AI tool helps classify chest X-ray images into:
        - *Normal*: Healthy lung tissue
        - *Pneumonia*: Signs of lung infection
        
        *Note*: This is for educational purposes only. 
        Always consult healthcare professionals for medical diagnosis.
        """
    )
    
    st.sidebar.title("Model Information")
    st.sidebar.text("Architecture: VGG19")
    st.sidebar.text("Input Size: 128x128 pixels")
    st.sidebar.text("Classes: Normal, Pneumonia")
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Chest X-ray")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a chest X-ray image",
            type=['jpg', 'jpeg', 'png', 'bmp'],
            help="Upload a clear chest X-ray image for analysis"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded X-ray", use_column_width=True)
            
            # Image information
            st.write(f"*Image Details:*")
            st.write(f"- Format: {uploaded_file.type}")
            st.write(f"- Size: {image.size}")
            st.write(f"- Mode: {image.mode}")
    
    with col2:
        st.subheader("🔍 Analysis Results")
        
        if uploaded_file is not None:
            # Load model
            with st.spinner("Loading model and analyzing..."):
                model = load_trained_model()
                
                if model is not None:
                    # Make prediction
                    predicted_class, confidence, normal_prob, pneumonia_prob = predict_image(model, image)
                    
                    if predicted_class:
                        # Display results
                        st.success("Analysis Complete!")
                        
                        # Confidence bars
                        st.write("*Confidence Levels:*")
                        
                        # Normal confidence
                        col_norm, col_pct_norm = st.columns([3, 1])
                        with col_norm:
                            st.write("Normal:")
                        with col_pct_norm:
                            st.write(f"{normal_prob*100:.1f}%")
                        
                        st.progress(float(normal_prob))
                        
                        # Pneumonia confidence  
                        col_pneu, col_pct_pneu = st.columns([3, 1])
                        with col_pneu:
                            st.write("Pneumonia:")
                        with col_pct_pneu:
                            st.write(f"{pneumonia_prob*100:.1f}%")
                        
                        st.progress(float(pneumonia_prob))
                        
                        # Result box
                        if predicted_class == "NORMAL":
                            st.markdown(
                                f'<div class="result-box normal">'
                                f'<h3>✅ Normal Lung</h3>'
                                f'<p>The X-ray appears to show healthy lung tissue.</p>'
                                f'<p><strong>Confidence: {confidence:.2f}%</strong></p>'
                                f'</div>',
                                unsafe_allow_html=True
                            )
                        else:
                            st.markdown(
                                f'<div class="result-box pneumonia">'
                                f'<h3>⚠ Pneumonia Detected</h3>'
                                f'<p>The X-ray shows signs consistent with pneumonia.</p>'
                                f'<p><strong>Confidence: {confidence:.2f}%</strong></p>'
                                f'</div>',
                                unsafe_allow_html=True
                            )
                        
                        # Recommendations
                        st.subheader("📋 Recommendations")
                        if predicted_class == "NORMAL":
                            st.info("""
                            - No immediate concerns detected in the X-ray
                            - Continue regular health checkups
                            - Consult a doctor if you experience any symptoms
                            """)
                        else:
                            st.warning("""
                            - *Consult a healthcare professional immediately*
                            - This AI detection is not a medical diagnosis
                            - Further tests may be needed for confirmation
                            - Follow your doctor's advice for treatment
                            """)
        
        else:
            # Placeholder when no image is uploaded
            st.info("👆 Upload a chest X-ray image to get started")
            
            # Sample images or instructions
            st.markdown("""
            <div class="upload-box">
            <h3>📁 How to use:</h3>
            <p>1. Click 'Browse files' above</p>
            <p>2. Select a chest X-ray image (JPG, PNG, BMP)</p>
            <p>3. Wait for AI analysis</p>
            <p>4. View results and recommendations</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "🩺 Medical AI Tool | For Educational Purposes Only | Consult Healthcare Professionals for Diagnosis"
        "</div>",
        unsafe_allow_html=True
    )

# If this file is run directly
if __name__ == "_main_":
    lung()