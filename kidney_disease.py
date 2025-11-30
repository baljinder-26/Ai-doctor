import streamlit as st
import pickle
import numpy as np

def kidney():

    st.markdown("<h1 style='text-align:center; color:cyan;'>🧬 Kidney Disease Prediction</h1>", unsafe_allow_html=True)
    st.write("Welcome to Baljinder and his friend Abhijay Entire Project 😊")

    # ---------------------------
    # Load Saved Model
    # ---------------------------
    @st.cache_resource
    def load_model():
        with open("best_model.pkl", "rb") as f:
            model = pickle.load(f)
        return model

    model = load_model()

    st.markdown("### Enter Patient Details")

    # ---------------------------
    # Input Fields (Edit as per your dataset)
    # ---------------------------

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120, 30)
        bp = st.number_input("Blood Pressure", 40, 200, 120)
        sugar = st.selectbox("Sugar Level High?", ["Yes", "No"])

    with col2:
        al = st.number_input("Albumin Level", 0, 10, 1)
        hemoglobin = st.number_input("Hemoglobin", 5.0, 20.0, 13.0)
        appetite = st.selectbox("Appetite Issue?", ["Yes", "No"])

    # Convert categorical to numeric
    sugar_val = 1 if sugar == "Yes" else 0
    appetite_val = 1 if appetite == "Yes" else 0

    # ---------------------------
    # Predict Button
    # ---------------------------
    if st.button("🔍 Predict Kidney Disease"):
        user_data = np.array([[age, bp, sugar_val, al, hemoglobin, appetite_val]])

        try:
            prediction = model.predict(user_data)[0]

            if prediction == 1:
                st.error("❗ The model predicts **Kidney Disease Detected**.")
            else:
                st.success("✅ The model predicts **No Kidney Disease**.")

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")
    st.markdown("<p style='text-align:center;'>Made with ❤️ by Baljinder & Abhijay</p>", unsafe_allow_html=True)


# Run Page
if __name__ == "__main__":
    kidney()
