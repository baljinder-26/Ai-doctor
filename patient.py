import streamlit as st
import s
from streamlit_lottie import st_lottie
import requests
import random
import io
import multi
# import tt

from datetime import datetime

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def pat():
        lottie_patient = load_lottieurl("https://lottie.host/5b9587db-da28-4f72-b8e0-1e9f8acfab0f/Ph8Dy2Ot5z.json")

        with st.sidebar:
            for i in range(1,8):
                st.write("")

            st_lottie(lottie_patient, height=250, key="patient_animation")
    
        if 'show_suggestions' not in st.session_state:
            st.session_state.show_suggestions = False
        with st.sidebar:
            st.sidebar.markdown("""
                <style>
                .sidebar-tagline {
                    font-size: 20px;
                    font-weight: 700;
                    color: #FFFFFF; /* bright white for dark background */
                    text-align: center;
                    margin-top: 25px;
                    margin-bottom: 15px;
                    font-family: 'Segoe UI', sans-serif;
                    letter-spacing: 0.5px;
                    opacity: 0.9;
                }
                </style>

                <div class="sidebar-tagline">Diet & Lifestyle 👇</div>
            """, unsafe_allow_html=True)
            st.markdown("""
                <style>
                @keyframes rainbow {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
                
                @keyframes glow {
                    0% { box-shadow: 0 0 20px #ff0080; }
                    25% { box-shadow: 0 0 30px #0080ff; }
                    50% { box-shadow: 0 0 40px #80ff00; }
                    75% { box-shadow: 0 0 30px #ff8000; }
                    100% { box-shadow: 0 0 20px #ff0080; }
                }
                
                @keyframes bounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-5px); }
                }
                
                @keyframes shake {
                    0%, 100% { transform: translateX(0); }
                    25% { transform: translateX(-2px); }
                    75% { transform: translateX(2px); }
                }
                
                .rainbow-btn {
                    background: linear-gradient(
                        135deg, 
                        #ff0000, #ff8000, #ffff00, #80ff00, 
                        #00ff00, #00ff80, #00ffff, #0080ff, 
                        #0000ff, #8000ff, #ff00ff, #ff0080
                    );
                    background-size: 300% 300%;
                    animation: rainbow 3s ease infinite, pulse 2s ease-in-out infinite;
                    color: white !important;
                    padding: 20px 30px;
                    border: none;
                    border-radius: 15px;
                    font-size: 28px;
                    font-weight: 800;
                    cursor: pointer;
                    text-align: center;
                    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
                    text-decoration: none !important;
                    display: block;
                    width: 100%;
                    margin: 15px 0;
                    position: relative;
                    overflow: hidden;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                }
                
                .rainbow-btn::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 100%;
                    height: 100%;
                    background: linear-gradient(
                        90deg,
                        transparent,
                        rgba(255,255,255,0.3),
                        transparent
                    );
                    transition: left 0.6s ease;
                }
                
                .rainbow-btn:hover {
                    animation: rainbow 1s ease infinite, glow 1.5s ease infinite, bounce 0.5s ease, shake 0.3s ease;
                    transform: scale(1.1) rotate(2deg);
                    border-radius: 25px;
                }
                
                .rainbow-btn:hover::before {
                    left: 100%;
                }
                
                .rainbow-btn:active {
                    transform: scale(0.95) rotate(-1deg);
                    animation: none;
                    background-size: 100% 100%;
                }
                
                .rainbow-btn::after {
                    content: '✨ Diet & Lifestyle Magic ✨';
                    position: absolute;
                    top: -45px;
                    left: 50%;
                    transform: translateX(-50%);
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    padding: 8px 16px;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: 600;
                    white-space: nowrap;
                    opacity: 0;
                    transition: all 0.3s ease;
                    pointer-events: none;
                    text-decoration: none !important;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                }
                
                .rainbow-btn:hover::after {
                    opacity: 1;
                    top: -50px;
                }
                
                /* Sparkle effect */
                .rainbow-btn span.sparkle {
                    position: absolute;
                    background: white;
                    border-radius: 50%;
                    pointer-events: none;
                    opacity: 0;
                }
                
                /* Style the form submit button to look like our custom button */
                div[data-testid="stFormSubmitButton"] button {
                    background: linear-gradient(135deg, #ff0000, #ff8000, #ffff00, #80ff00) !important;
                    background-size: 300% 300% !important;
                    animation: rainbow 3s ease infinite, pulse 2s ease-in-out infinite !important;
                    color: white !important;
                    padding: 20px 30px !important;
                    border: none !important;
                    border-radius: 15px !important;
                    font-size: 28px !important;
                    font-weight: 800 !important;
                    cursor: pointer !important;
                    text-align: center !important;
                    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
                    text-decoration: none !important;
                    display: block !important;
                    width: 100% !important;
                    margin: 15px 0 !important;
                    position: relative !important;
                    overflow: hidden !important;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5) !important;
                }
                
                div[data-testid="stFormSubmitButton"] button:hover {
                    animation: rainbow 1s ease infinite, glow 1.5s ease infinite !important;
                    transform: scale(1.1) rotate(2deg) !important;
                    border-radius: 25px !important;
                }
                </style>
            """, unsafe_allow_html=True)
            
            # Create a form for the button
            with st.form("magic_button_form"):
                submitted = st.form_submit_button("💡")
                
                if submitted:
                    st.session_state.show_suggestions = True
                    st.rerun()

        # JavaScript for additional effects
        st.sidebar.markdown("""
            <script>
            // Add sparkle effect on click
            document.addEventListener('DOMContentLoaded', function() {
                const button = document.querySelector('[data-testid="stFormSubmitButton"] button');
                if (button) {
                    button.innerHTML = '💡';
                    button.className = 'rainbow-btn';
                    
                    button.addEventListener('click', function(e) {
                        // Create sparkles
                        for (let i = 0; i < 10; i++) {
                            createSparkle(e);
                        }
                    });
                    
                    function createSparkle(e) {
                        const sparkle = document.createElement('div');
                        sparkle.className = 'sparkle';
                        
                        const size = Math.random() * 10 + 5;
                        sparkle.style.width = size + 'px';
                        sparkle.style.height = size + 'px';
                        
                        const rect = button.getBoundingClientRect();
                        sparkle.style.left = (e.clientX - rect.left) + 'px';
                        sparkle.style.top = (e.clientY - rect.top) + 'px';
                        
                        button.appendChild(sparkle);
                        
                        // Animate sparkle
                        const angle = Math.random() * Math.PI * 2;
                        const distance = Math.random() * 50 + 30;
                        const x = Math.cos(angle) * distance;
                        const y = Math.sin(angle) * distance;
                        
                        sparkle.animate([
                            { 
                                transform: 'translate(0, 0) scale(1)',
                                opacity: 1
                            },
                            { 
                                transform: `translate(${x}px, ${y}px) scale(0)`,
                                opacity: 0
                            }
                        ], {
                            duration: 600,
                            easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
                        }).onfinish = () => sparkle.remove();
                    }
                }
            });
            </script>
        """, unsafe_allow_html=True)

        # --- Page navigation ---
        if st.session_state.show_suggestions:
            if st.button("⬅️ Go to Back"):
                st.session_state.show_suggestions = False
                st.rerun()
            s.sugg()
        else:
            discord_bg_url = "https://img.freepik.com/premium-vector/blue-bright-doctor-silhouette-background_36402-427.jpg?semt=ais_hybrid&w=740&q=80"  # Example animated discord-like background

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
                    background-color: rgba(0, 0, 0, 0.3);
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
                # st.write("Welcome to AI Doctor- Your Personal Guide")
                
                # -----------------------
                # Helper: Load Lottie safely
                # -----------------------



            # -----------------------
            # Helper: load Lottie JSON safely
            # -----------------------
            @st.cache_data(show_spinner=False)
            def load_lottie_url(url: str):
                try:
                    r = requests.get(url, timeout=6)
                    if r.status_code == 200:
                        return r.json()
                except Exception:
                    return None
                return None

            # -----------------------
            # Helper: load image bytes for download (optional)
            # -----------------------
            @st.cache_data(show_spinner=False)
            def load_image_bytes(url: str):
                try:
                    r = requests.get(url, timeout=6)
                    if r.status_code == 200:
                        return r.content
                except Exception:
                    return None
                return None

            # -----------------------
            # Simple symptom extraction (keyword-based)
            # -----------------------
            SYMPTOM_KEYWORDS = [
                "fever", "cough", "cold", "headache", "nausea", "vomit", "vomiting",
                "fatigue", "tired", "chest pain", "shortness of breath", "breathless",
                "dizziness", "thirst", "frequent urination", "sore throat", "stomach pain",
                "diarrhea", "loss of appetite", "palpitations", "sweating"
            ]

            def extract_symptoms_from_text(text: str):
                if not text:
                    return []
                text_low = text.lower()
                found = []
                for kw in SYMPTOM_KEYWORDS:
                    if kw in text_low:
                        found.append(kw)
                # remove duplicates, preserve order
                seen = set()
                ordered = []
                for s in found:
                    if s not in seen:
                        ordered.append(s)
                        seen.add(s)
                return ordered

            # -----------------------
            # Dummy prediction logic (deterministic & explainable)
            # Replace with real ML model when ready
            # -----------------------
            def dummy_predict(age:int, bmi:float, bp:float, symptoms:list):
                """
                Returns dict:
                - risk_score (0-100)
                - category ('Low','Moderate','High')
                - reasons (list of strings explaining influences)
                """
                reasons = []
                score = 0

                # Age influence
                if age >= 60:
                    score += 25
                    reasons.append("Age >= 60 increases risk")
                elif age >= 45:
                    score += 12
                    reasons.append("Age between 45 and 59")

                # BMI influence
                if bmi >= 35:
                    score += 25
                    reasons.append("Severely high BMI (>=35)")
                elif bmi >= 30:
                    score += 15
                    reasons.append("High BMI (>=30)")
                elif bmi >= 25:
                    score += 5
                    reasons.append("Overweight (BMI >=25)")

                # Blood pressure influence
                if bp >= 160:
                    score += 20
                    reasons.append("Very high blood pressure (>=160)")
                elif bp >= 140:
                    score += 12
                    reasons.append("High blood pressure (>=140)")

                # Symptom influence (each important symptom adds)
                critical_symptoms = {"chest pain", "shortness of breath", "palpitations", "loss of appetite"}
                moderate_symptoms = {"fever", "dizziness", "severe fatigue", "frequent urination", "thirst"}
                for s in symptoms:
                    if s in critical_symptoms:
                        score += 20
                        reasons.append(f"Critical symptom: {s}")
                    elif s in moderate_symptoms:
                        score += 8
                        reasons.append(f"Moderate symptom: {s}")
                    else:
                        score += 3
                        reasons.append(f"Symptom: {s}")

                # small random jitter to avoid same exact values every run (but deterministic enough)
                jitter = random.randint(-3, 3)
                score = max(0, min(100, score + jitter))

                if score < 35:
                    category = "Low"
                elif score < 70:
                    category = "Moderate"
                else:
                    category = "High"

                return {"risk_score": score, "category": category, "reasons": reasons}



            # Lottie URLs - chosen to be generally reliable; can be replaced
            LOTTIE_DOCTOR = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
            LOTTIE_HEALTH = "https://assets9.lottiefiles.com/packages/lf20_h2r3iqjq.json"

            lottie_doctor = load_lottie_url(LOTTIE_DOCTOR)
            lottie_health = load_lottie_url(LOTTIE_HEALTH)

            # Header


                # st.title("AI Doctor — Virtual Health Companion")
            st.markdown("""
            <style>
            .intro-container {
                padding: 30px;
                margin-top: 40px;
                border-radius: 20px;
                background: linear-gradient(135deg, #e3f2fd, #ffffff);
                box-shadow: 0 6px 20px rgba(0,0,0,0.15);
                text-align: center;
                animation: fadeIn 2s ease-in-out;
            }
            .intro-title {
                font-size: 42px;
                font-weight: 800;
                color: #1e88e5;
                text-shadow: 2px 2px #bbdefb;
            }
            .intro-text {
                font-size: 20px;
                font-weight: 500;
                color: #333333;
                margin-top: 15px;
                line-height: 1.6;
            }
            .highlight {
                color: #d32f2f;
                font-weight: 700;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            </style>

            <div class="intro-container">
                <div class="intro-title">AI Doctor – Patient Clinical Profile</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""AI Doctor is an Artificial Assitant for the humans and giving answers to their queries""")

            # with col2:
            #     if lottie_doctor:
            #         st_lottie(lottie_doctor, height=200, key="doctor_lottie")
            #     else:
            #         st.image("https://cdn-icons-png.flaticon.com/512/2966/2966487.png", width=140)

            # st.markdown("---")

            # -----------------------
            # Input: Patient details
            # -----------------------
            st.subheader("Patient Details")
            with st.container():
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    name = st.text_input("Full name", placeholder="Your Name")
                with c2:
                    age = st.number_input("Age", min_value=0, max_value=120, value=30)
                with c3:
                    gender = st.selectbox("Gender", ["Prefer not to say", "Female", "Male", "Other"])
                with c4:
                    contact = st.text_input("Contact (optional)")

                d1, d2 = st.columns(2)
                with d1:
                    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, format="%.1f")
                with d2:
                    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, format="%.1f")

                # compute BMI (display-only)
                bmi = None
                if height_cm > 0:
                    height_m = height_cm / 100.0
                    bmi = weight / (height_m * height_m)
                    st.metric("BMI", f"{bmi:.1f}")

            st.markdown("---")

            # -----------------------
            # Input: Symptoms
            # -----------------------
            st.subheader("Describe your symptoms (in plain English)")
            symptoms_text = st.text_area("Type symptoms, duration, severity, and anything relevant...", height=140)

            st.markdown("**Tip:** Describe when your symptoms started and how severe they are. E.g., 'chest pain since yesterday, moderate intensity'.")

            # -----------------------
            # Optional vitals
            # -----------------------
            st.subheader("Optional Vitals (if known)")
            v1, v2, v3 = st.columns(3)
            with v1:
                bp = st.number_input("Systolic Blood Pressure (mm Hg)", value=120)
            with v2:
                hr = st.number_input("Heart rate (bpm)", value=75)
            with v3:
                temp = st.number_input("Body Temperature (°C)", value=36.6)

            st.markdown("---")

            # -----------------------
            # Analyze button
            # -----------------------
            analyze = st.button("Analyze Health")
            if analyze:
                if not name.strip():
                    st.error("Please enter patient's full name.")
                else:
                    # Extract symptoms
                    extracted = extract_symptoms_from_text(symptoms_text)
                    if not extracted:
                        st.info("No known keywords detected in symptoms text — result will use vitals and demographics.")
                    # Predict
                    predict_result = dummy_predict(age=int(age), bmi=float(bmi), bp=int(bp), symptoms=extracted)

                    # Display main summary
                    st.header("Assessment Summary")
                    rcol1, rcol2 = st.columns([1,2])
                    with rcol1:
                        # image that indicates risk
                        if predict_result["category"] == "High":
                            st.image("https://cdn-icons-png.flaticon.com/512/464/464619.png", width=100, caption="High Risk")
                        elif predict_result["category"] == "Moderate":
                            st.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=100, caption="Moderate Risk")
                        else:
                            st.image("https://cdn-icons-png.flaticon.com/512/190/190406.png", width=100, caption="Low Risk")

                    with rcol2:
                        st.subheader(f"Predicted Risk: {predict_result['category']}")
                        st.progress(predict_result["risk_score"])
                        st.write(f"**Risk Score:** {predict_result['risk_score']} / 100")
                        # show contributing reasons
                        with st.expander("Why this score?"):
                            for r in predict_result["reasons"]:
                                st.write("- " + r)

                    # show extracted symptoms
                    st.subheader("Extracted Symptoms")
                    if extracted:
                        st.write(", ".join(extracted))
                    else:
                        st.write("No keyword-based symptoms found.")

                    # Recommendations section
                    st.subheader("Recommendations")
                    if predict_result["category"] == "High":
                        st.error("High risk detected — seek medical attention immediately. Consider visiting the nearest ER or contacting a physician.")
                        st.write("- Contact emergency services if symptoms are severe (chest pain, fainting, severe breathlessness).")
                        st.write("- Avoid strenuous activity and rest. Keep hydrated.")
                    elif predict_result["category"] == "Moderate":
                        st.warning("Moderate risk — book a consultation with your healthcare provider for evaluation and tests.")
                        st.write("- Monitor vitals (BP, HR, temperature) regularly.")
                        st.write("- Consider basic tests: CBC, blood sugar, ECG (as recommended by physician).")
                    else:
                        st.success("Low risk — maintain healthy lifestyle and watch for changes.")
                        st.write("- Follow a balanced diet, exercise regularly, and monitor symptoms.")
                        st.write("- If new or worsening symptoms appear, consult a doctor.")

                    # extra tips
                    st.markdown("**General Wellness Tips**")
                    st.write("""
                    - Balanced diet: include vegetables, lean proteins, whole grains; reduce processed sugars.
                    - Physical activity: aim for 30 minutes of moderate exercise most days.
                    - Sleep: 7-8 hours per night.
                    - Hydration: 2-3 liters of water per day (adjust by climate & activity).
                    """)

                    # Animated health block (fallback safe)
                    if lottie_health:
                        st_lottie(lottie_health, height=220, key="health_anim")
                    else:
                        st.image("https://images.unsplash.com/photo-1584433144859-0e66f0c9f3ca?q=80&w=700&auto=format&fit=crop&ixlib=rb-4.0.3&s=99bd5f3a5cba2aa7f7f9f6d0d6c9abf8", width=700)

                    # -----------------------
                    # Downloadable summary (text)
                    # -----------------------
                    def create_summary_text():
                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        s = io.StringIO()
                        s.write("AI Doctor - Health Summary\n")
                        s.write(f"Generated: {now}\n\n")
                        s.write("Patient Details\n")
                        s.write(f"Name: {name}\nAge: {age}\nGender: {gender}\nContact: {contact}\n\n")
                        s.write("Vitals\n")
                        s.write(f"Weight: {weight} kg\nHeight: {height_cm} cm\nBMI: {bmi:.1f}\nBP: {bp} mm Hg\nHR: {hr} bpm\nTemp: {temp} C\n\n")
                        s.write("Extracted Symptoms:\n")
                        if extracted:
                            s.write(", ".join(extracted) + "\n\n")
                        else:
                            s.write("None detected (keyword-based)\n\n")
                        s.write("Prediction\n")
                        s.write(f"Risk Score: {predict_result['risk_score']} / 100\n")
                        s.write(f"Risk Category: {predict_result['category']}\n\n")
                        s.write("Reasons:\n")
                        for r in predict_result["reasons"]:
                            s.write("- " + r + "\n")
                        s.write("\nRecommendations:\n")
                        if predict_result["category"] == "High":
                            s.write("Seek immediate medical attention. Consider ER if severe.\n")
                        elif predict_result["category"] == "Moderate":
                            s.write("Book a consultation and consider diagnostic tests.\n")
                        else:
                            s.write("Maintain healthy lifestyle and monitor symptoms.\n")
                        s.seek(0)
                        return s.read()

                    summary_text = create_summary_text()
                    st.download_button("Download Health Summary (TXT)", data=summary_text, file_name="ai_doctor_summary.txt", mime="text/plain")

            
            st.markdown("---")
            st.caption("Demo app for educational purposes. This is not a medical device or a diagnostic tool.")