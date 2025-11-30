import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

def lung():
    # Define available models with their paths and descriptions
    models = {
        "VGG16 Unfrozen": {
            "path": "model_weights/vgg_unfrozen.h5",
            "description": "VGG16 architecture with unfrozen layers for fine-tuning on medical images"
        },
        "VGG19 Model 01": {
            "path": "model_weights/vgg19_model_01.h5",
            "description": "VGG19 architecture - First training configuration"
        },
        "VGG19 Model 02": {
            "path": "model_weights/vgg19_model_02.h5",
            "description": "VGG19 architecture - Second training configuration with different parameters"
        }
    }
    
    class_names = ["NORMAL", "PNEUMONIA"]

    st.title("🫁 Lung X-Ray Disease Detection")
    st.write("Upload a chest X-ray to classify **Normal vs Pneumonia**")

    # Add important warning
    st.warning("⚠️ **Important**: This tool is for educational purposes only. Always consult healthcare professionals for medical diagnosis.")

    # Model selection
    st.subheader("🔧 Model Selection")
    selected_model_name = st.selectbox(
        "Choose a model:",
        options=list(models.keys()),
        help="Select which trained model to use for prediction"
    )
    
    # Display model description
    selected_model_info = models[selected_model_name]
    st.write(f"**Model Info:** {selected_model_info['description']}")

    # Add confidence threshold slider
    confidence_threshold = st.slider(
        "Confidence Threshold (%)",
        min_value=50,
        max_value=95,
        value=70,
        help="Minimum confidence required for a definite prediction"
    )

    uploaded_file = st.file_uploader("📤 Upload Chest X-ray", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded X-ray", use_column_width=True)

        # ✅ Load and preprocess image
        try:
            img = load_img(uploaded_file, target_size=(128, 128), color_mode="rgb")
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize
            
        except Exception as e:
            st.error(f"❌ Error processing image: {str(e)}")
            return

        if st.button("🔍 Predict", type="primary"):
            with st.spinner(f"Loading {selected_model_name} and analyzing X-ray... Please wait ⏳"):
                try:
                    # Load the selected model
                    model = load_model(selected_model_info["path"])
                    
                    # Make prediction
                    prediction = model.predict(img_array, verbose=0)
                    prob = prediction[0]
                    
                    index = np.argmax(prob)
                    result = class_names[index]
                    confidence = prob[index] * 100

                    # Display results
                    st.subheader("🎯 Prediction Results")
                    
                    # Result card
                    if confidence < confidence_threshold:
                        st.warning(f"⚠️ **Low Confidence Prediction: {result}**")
                        st.info(f"Confidence ({confidence:.2f}%) is below the threshold ({confidence_threshold}%). Please consult a healthcare professional.")
                    else:
                        if result == "NORMAL":
                            st.success(f"✅ **Result: {result}**")
                        else:
                            st.error(f"🚨 **Result: {result}**")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Model Used", selected_model_name)
                    with col2:
                        st.metric("Prediction", result)
                    with col3:
                        st.metric("Confidence", f"{confidence:.2f}%")

                    # Confidence chart
                    st.subheader("📊 Prediction Confidence")
                    fig, ax = plt.subplots(figsize=(10, 6))
                    
                    # Create colored bars with threshold line
                    colors = ['lightgreen', 'lightcoral']
                    bars = ax.bar(class_names, prob, color=colors, edgecolor='black', alpha=0.7)
                    ax.set_ylabel("Probability", fontsize=12)
                    ax.set_title(f"Confidence Scores - {selected_model_name}", fontsize=14, fontweight='bold')
                    ax.set_ylim(0, 1)
                    
                    # Add threshold line
                    threshold_line = confidence_threshold / 100
                    ax.axhline(y=threshold_line, color='red', linestyle='--', 
                              label=f'Confidence Threshold ({confidence_threshold}%)')
                    
                    # Add value labels on bars
                    for bar, value, class_name in zip(bars, prob, class_names):
                        height = bar.get_height()
                        color = 'black' if value > 0.5 else 'white'
                        ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                               f'{value:.3f}\n({value*100:.1f}%)', 
                               ha='center', va='bottom', fontweight='bold',
                               color=color, fontsize=10)
                    
                    # Customize the plot
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    plt.xticks(fontsize=11)
                    plt.yticks(fontsize=11)
                    ax.legend()
                    
                    st.pyplot(fig)

                    # Interpretation
                    st.subheader("💡 Interpretation & Recommendations")
                    
                    if result == "NORMAL":
                        if confidence >= confidence_threshold:
                            st.success("""
                            **Normal X-ray Interpretation:**
                            - The lung fields appear clear
                            - No significant consolidation observed
                            - Normal lung markings present
                            """)
                        else:
                            st.warning("""
                            **Low Confidence Normal Result:**
                            - The model is uncertain about this prediction
                            - Consider getting a second opinion
                            - Clinical correlation recommended
                            """)
                    else:
                        if confidence >= confidence_threshold:
                            st.error("""
                            **Pneumonia Suspicion:**
                            - Areas of consolidation may be present
                            - Possible air bronchograms or opacity patterns
                            - **Urgent:** Please consult a radiologist or healthcare provider immediately
                            """)
                        else:
                            st.warning("""
                            **Low Confidence Pneumonia Result:**
                            - Some features suggestive of pneumonia detected
                            - Model confidence is below threshold
                            - **Important:** Clinical evaluation strongly recommended
                            """)

                except Exception as e:
                    st.error(f"❌ Error during prediction: {str(e)}")

    # Add information section at the bottom
    st.markdown("---")
    with st.expander("ℹ️ About the Models & Disclaimer"):
        st.write("""
        **Model Descriptions:**
        
        - **VGG16 Unfrozen**: VGG16 architecture with unfrozen layers, fine-tuned on medical X-ray images
        - **VGG19 Model 01**: VGG19 architecture with first training configuration
        - **VGG19 Model 02**: VGG19 architecture with second training configuration
        
        **Medical Disclaimer:** 
        This AI tool is for educational and research purposes only. 
        It should not replace professional medical diagnosis, consultation, or treatment. 
        Always seek the advice of qualified healthcare providers with medical questions.
        """)

# Run the app
if __name__ == "__main__":
    lung()