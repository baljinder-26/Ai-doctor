import streamlit as st
from streamlit_lottie import st_lottie
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------------------
# Brain Tumor Streamlit App
# ---------------------------
def brain():
    # Load animation--
    #https://lottie.host/a96a25e2-48c2-4a3f-948d-329319ee34fa/19F2qxjhD6.json
    brain_anim = load_lottieurl("https://lottie.host/961c5b72-2a4f-4628-b4e1-bd0557972b2b/kclaamX7MU.json")

    st.title("🧠 Brain Tumor Detection")
    st.markdown("### Upload MRI Image to Predict Tumor Type")
    st.write("---")

    # CSS styling for nice hover effect
    # st.markdown("""
    #     <style>
    #     .main-card {
    #         background: rgba(255,255,255,0.9);
    #         border-radius: 20px;
    #         padding: 25px;
    #         box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    #         transition: all 0.3s ease-in-out;
    #     }
    #     .main-card:hover {
    #         transform: scale(1.02);
    #         box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    #     }
    #     </style>
    # """, unsafe_allow_html=True)

    # Load model (cached)
    @st.cache_resource
    def load_model():
        model = tf.keras.models.load_model("vgg16_model.h5")
        return model

    model = load_model()

    # Define class labels
    class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

    # Prediction function
    def predict_tumor(img):
        img = cv2.resize(img, (128, 128))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions)
        confidence_score = np.max(predictions)
        return class_labels[predicted_class_index], confidence_score, predictions

    # Animation block
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    if brain_anim:
        st_lottie(brain_anim, height=250, key="brain")
    else:
        st.error("⚠️ Animation failed to load")
    st.markdown('</div>', unsafe_allow_html=True)

    # Upload image
    uploaded_file = st.file_uploader("📤 Upload MRI Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, caption="🧩 Uploaded MRI Image", use_column_width=True)

        if st.button("🔍 Predict"):
            with st.spinner("Analyzing..."):
                tumor_type, confidence, probs = predict_tumor(img)

                if tumor_type == "notumor":
                    st.success(f"✅ No Tumor Detected — ({confidence * 100:.2f}% confidence)")
                else:
                    st.error(f"🧠 Tumor Detected: **{tumor_type.capitalize()}**")
                    st.metric(label="Prediction Confidence", value=f"{confidence * 100:.2f}%")

                # Display class probability distribution
                st.write("### 🔢 Prediction Probabilities")
                prob_dict = {label: float(probs[0][i]) for i, label in enumerate(class_labels)}
                st.json(prob_dict)

                # Bar chart visualization
                st.bar_chart(prob_dict)

    st.write("---")
    st.info("✨ Hover over the animation card for a smooth transition effect.")

# ---------------------------
# Entry Point
# ---------------------------
if __name__ == "__main__":
    brain()


