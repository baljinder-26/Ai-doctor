import streamlit as st
import multi
import patient
import finder
import s
from datetime import datetime
import time
from streamlit_lottie import st_lottie
import requests
import random
import io

@st.cache_resource
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# @st.cache_resource
def main():
    st.set_page_config(
        page_title="AI Doctor",
        page_icon="🩺",
        layout="wide"
    )

    # Initialize session state in the main file
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    
    choice = st.sidebar.selectbox(
        "Wellness Corner:",
        ["Home", "Patient Check Up", "Multi-Disease Prediction","HealthFinder🏥"]
    )
       

    # --- Page Header ---
     # ✅ Make sure this is here

    
    
    # Navigation based on choice
    if choice == "Home":
       
        
        discord_bg_url = "https://t4.ftcdn.net/jpg/05/64/05/49/360_F_564054980_NpVuWxBcFSXyvaBYdB2zPFSKTol5f2XV.jpg"  # Example animated discord-like background
    
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
           
        @st.cache_data(show_spinner=False)
        def load_lottie_url(url: str):
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    return r.json()
            except:
                return None
            return None
        lottie_patient = load_lottie_url("https://lottie.host/5b9587db-da28-4f72-b8e0-1e9f8acfab0f/Ph8Dy2Ot5z.json")

        with st.sidebar:
            for i in range(1,7):
                st.write("")

            st_lottie(lottie_patient, height=250, key="patient_animation")
            
       
        if 'show_suggestions' not in st.session_state:
            st.session_state.show_suggestions = False
        with st.sidebar:
            # st.write("Upgrade your Lifestyle Today!")
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
        if st.session_state.show_suggestions:#true
            if st.button("⬅️ Return to Home"):
                st.session_state.show_suggestions = False
                st.rerun()
            s.sugg()
        else:#false
            doctor_anim = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_h2r3iqjq.json")
            # healthcare_anim = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")
            # analysis_anim = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_cg8qgqvq.json")

            st.markdown("""
                <style>
                body {
                    background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
                }
                .hero {
                    display: flex;
                    flex-direction: column;
                    align-items: center;         /* ✅ centers horizontally */
                    justify-content: center;
                    text-align: center;
                    padding: 5px 20px;
                    animation: fadeIn 2s ease-in-out;
                    width: 100%;                 /* ✅ take full width */
                    max-width: 900px;            /* ✅ optional: limit max width */
                    margin: 0 auto;              /* ✅ center horizontally */
                }

                .hero-title {
                    font-size: 40px;
                    font-weight: 800;
                    background: linear-gradient(90deg, #1976d2, #42a5f5);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;  /* ✅ better than 'light blue' */
                    margin-bottom: 20px;
                    text-shadow: 2px 2px #bbdefb;
                    text-align: center;          /* ✅ keep text centered */
                }

                .hero-subtitle {
                    font-size: 24px;
                    font-weight: 600;
                    color: white;
                    max-width: 800px;
                    margin: 0 auto;              /* ✅ centers text block */
                    line-height: 1.5;
                    text-align: center;          /* ✅ better than justify for centering */
                    padding-left: 0;             /* ❌ remove fixed padding */
                    padding-right: 0;            /* optional */
                }


                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(30px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                .section-title {
                    font-size: 36px;
                    font-weight: 700;
                    color: #99EDEA;
                    text-align: center;
                    margin: 50px 0 20px;
                }
                .feature-box {
                    padding: 8px;
                    background: #ffffff;
                    border-radius: 20px;
                    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease;
                    text-align: center;
                }
                .feature-box:hover {
                    transform: translateY(-10px);
                    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
                }
                .feature-title {
                    font-size: 16px;
                    font-weight: 500;
                    color: #000000 !important;
                    margin-top: 12px;
                }
                .feature-text {
                    font-size: 18px;
                    color: white;
                    margin-top: 10px;
                }
                .cta-button {
                    display: block;
                    margin: 50px auto;
                    padding: 15px 40px;
                    background: linear-gradient(90deg, #1976d2, #42a5f5);
                    color: white;
                    font-size: 20px;
                    font-weight: bold;
                    border: none;
                    border-radius: 40px;
                    cursor: pointer;
                    text-align: center;
                    transition: 0.3s;
                    text-decoration: none;
                }
                .cta-button:hover {
                    background: white;
                    transform: scale(1.05);
                }
                </style>
            """, unsafe_allow_html=True)


            with st.container():
                st.markdown('<div class="hero">', unsafe_allow_html=True)
                st.markdown('<div class="hero-title">🩺 AI Doctor – Your Smart Health Companion</div>', unsafe_allow_html=True)
                st.markdown('<div class="hero-subtitle">Experience the future of healthcare with an intelligent virtual assistant that analyzes your health data, understands your symptoms, and provides AI-powered predictions and lifestyle recommendations — all from the comfort of your home.</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                if doctor_anim:
                    st_lottie(doctor_anim, height=300, key="hero-anim")

            # -----------------------
            # ABOUT SECTION
            # -----------------------
            st.markdown('<div class="section-title">About AI Doctor</div>', unsafe_allow_html=True)
            col1, col2 = st.columns([1,1])
        
        
            st.markdown("""
            <style>
            .what-section {
                background: linear-gradient(135deg, rgba(0, 224, 255, 0.1), rgba(56, 239, 125, 0.1), rgba(102, 126, 234, 0.1));
                padding: 40px;
                border-radius: 25px;
                border: 1px solid rgba(0, 224, 255, 0.3);
                box-shadow: 0 15px 40px rgba(0, 224, 255, 0.15),
                            inset 0 1px 0 rgba(255, 255, 255, 0.2);
                margin-top: 40px;
                animation: fadeInUp 1.2s ease-out;
                backdrop-filter: blur(10px);
                position: relative;
                overflow: hidden;
            }
            
            .what-section::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
                animation: shine 6s ease-in-out infinite;
            }
            
            .what-title {
                font-size: 2.8em;
                font-weight: 800;
                background: linear-gradient(45deg, #00e0ff, #38ef7d, #00e0ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-align: center;
                margin-bottom: 30px;
                text-shadow: 0 0 30px rgba(0, 224, 255, 0.3);
                position: relative;
            }
            
            .what-text {
                font-size: 1.3em;
                line-height: 1.8;
                color: #e0e0e0;
                text-align: center;
                margin-bottom: 30px;
                font-weight: 400;
                text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
            }
            
            .tech-highlights {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            
            .tech-item {
                background: rgba(255, 255, 255, 0.08);
                padding: 20px;
                border-radius: 15px;
                border: 1px solid rgba(0, 224, 255, 0.2);
                text-align: center;
                transition: all 0.3s ease;
                backdrop-filter: blur(5px);
            }
            
            .tech-item:hover {
                transform: translateY(-5px);
                border-color: rgba(56, 239, 125, 0.5);
                box-shadow: 0 10px 25px rgba(56, 239, 125, 0.2);
            }
            
            .tech-icon {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            
            .tech-title {
                font-size: 1.2em;
                font-weight: 700;
                color: #00e0ff;
                margin-bottom: 8px;
            }
            
            .tech-desc {
                font-size: 0.95em;
                color: #cccccc;
                line-height: 1.5;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 15px;
                margin: 25px 0;
            }
            
            .feature-item {
                display: flex;
                align-items: center;
                gap: 15px;
                padding: 15px;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                border-left: 4px solid #38ef7d;
                transition: all 0.3s ease;
            }
            
            .feature-item:hover {
                background: rgba(255, 255, 255, 0.1);
                transform: translateX(5px);
            }
            
            .feature-icon {
                font-size: 1.8em;
                flex-shrink: 0;
            }
            
            .feature-text {
                color: #e0e0e0;
                font-size: 1.1em;
                font-weight: 500;
            }
            
            .mission-text {
                background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(255, 107, 107, 0.15));
                padding: 25px;
                border-radius: 18px;
                border: 1px solid rgba(102, 126, 234, 0.3);
                margin-top: 30px;
                text-align: center;
                font-size: 1.2em;
                color: #ffffff;
                line-height: 1.7;
                font-weight: 400;
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(40px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            @keyframes shine {
                0% { left: -100%; }
                20% { left: 100%; }
                100% { left: 100%; }
            }
            </style>

            <div class="what-section">
                <div class="what-title">🩺 What is AI Doctor?</div>
                <p style="color: white; text-align: center;">An intelligent virtual healthcare companion revolutionizing medical diagnostics</p>
                <p style="color: white; text-align: center;">Multi-disease prediction platform using advanced machine learning algorithms</p>
                <p style="color: white; text-align: center;">24/7 accessible medical assistant bridging healthcare gaps</p>
                <p style="color: white; text-align: center;">Democratizing healthcare access globally & Supporting healthcare professionals with AI tools</p>
                
        """, unsafe_allow_html=True)

            # with col2:
                
            # -----------------------
            # FEATURES SECTION
            # -----------------------
            st.markdown('<div class="section-title">Core Features</div>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                # st.markdown('<div class="feature-box">', unsafe_allow_html=True)
                # # st.image("https://cdn-icons-png.faticon.com/512/2966/2966487.png", width=80)
                # st.markdown('<div class="feature-title">Symptom Analysis</div>', unsafe_allow_html=True)
                # st.markdown('<div class="feature-text">Extract and interpret health conditions using NLP from simple text descriptions.</div>', unsafe_allow_html=True)
                # st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("""
                <div class="feature-box">
                    <h3 class="feature-title">Symptom Analysis</h3>
                
                </div>
            """, unsafe_allow_html=True)
                st.markdown('<div class="feature-text">Extract and interpret health conditions using NLP from simple text descriptions.</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)


            with col2:
                st.markdown("""
                <div class="feature-box">
                    <h3 class="feature-title">Disease Prediction</h3>
                
                </div>
            """, unsafe_allow_html=True)
                # st.markdown('<div class="feature-title">Disease Prediction</div>', unsafe_allow_html=True)
                st.markdown('<div class="feature-text">AI-powered models estimate risks for diseases like diabetes, heart disease, and more.</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col3:
                st.markdown("""
                    <div class="feature-box">
                        <h3 class="feature-title">Smart Guidance</h3>
                    
                    </div>
                """, unsafe_allow_html=True)
                st.markdown('<div class="feature-text">Receive easy-to-understand advice, home remedies, and next-step recommendations.</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # -----------------------
            # HOW IT WORKS
            # -----------------------
            st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
            col1, col2 = st.columns([1,1])
            with col1:
                st.subheader("🚀 Quick Start")
                st.write("""
                Select **Multi-Disease Prediction** from the sidebar to:
                - Analyze brain tumor MRI images
                - MRI:- Magnetic Resonance Imaging
                - Check for heart disease 
                - Lung Disease Detection 
                """)

            with col2:
                st.markdown("""
                ### Step-by-Step Process
                1. **Input Data** – Enter basic health info and describe your symptoms.  
                2. **AI Analysis** – NLP interprets your input and extracts medical parameters.  
                3. **Risk Prediction** – Machine learning predicts possible conditions.  
                4. **Recommendations** – Generative AI provides next-step suggestions.  
                5. **Optional Export** – Download your health summary for future reference.
                """)

            # -----------------------
            # CTA - Start Diagnosis
            # -----------------------
            st.markdown("""
                <a href="#" class="cta-button">🚀 Start Diagnosis Now</a>
            """, unsafe_allow_html=True)

            # Footer
            st.markdown("---")
            st.caption("⚠️ Disclaimer: AI Doctor is a demonstration prototype and should not be used for medical decisions. Always consult a licensed medical professional.")
            import time

                    # Glass notification styled bottom-right popup



        # Darker glass-style toast popup
            st.markdown("""
            <style>
            @keyframes slideFadeInOut {
                0%   {opacity: 0; transform: translateX(100%) scale(0.9);}
                10%  {opacity: 1; transform: translateX(0%) scale(1);}
                90%  {opacity: 1; transform: translateX(0%) scale(1);}
                100% {opacity: 0; transform: translateX(100%) scale(0.9);}
            }

            .toast-container {
                position: fixed;
                bottom: 30px;
                right: 30px;
                backdrop-filter: blur(18px);
                background: rgba(10, 10, 10, 0.8);  /* MUCH darker glass background */
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 18px;
                padding: 24px 30px;
                z-index: 9999;
                text-align: left;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.55);
                animation: slideFadeInOut 3s ease-in-out forwards;
                color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
                max-width: 340px;
                width: fit-content;
            }

            .toast-container h3 {
                color: #42a5f5;
                margin: 0 0 8px 0;
                font-size: 22px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }

            .toast-container p {
                font-size: 16px;
                margin: 2px 0;
                color: #e3f2fd;
                opacity: 0.9;
            }
            </style>

            <div class="toast-container">
                <h3>Welcome to <strong>AI Doctor</strong></h3>
                <p>Your virtual healthcare assistant.</p>
                
            </div>
        """, unsafe_allow_html=True)

        # Show for 2 seconds
            time.sleep(15)
            
            
            
            st.markdown("---")
            st.info("💡 **Tip**: Use the sidebar to navigate between different features.")
        
            
    elif choice == "Patient Check Up":
        patient.pat()
    
    elif choice == "Multi-Disease Prediction":
        multi.show()

    elif choice == "HealthFinder🏥":
        finder.health()

    # elif choice == "":
    #     s.sugg()

if __name__ == "__main__":
    main()