import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
import s

# Import your modules
try:
    import brain_tumor
    import heart_disease
    import lung_disease
    import eye
    import kidney_disease
except ImportError as e:
    st.error(f"Could not import brain_tumor module: {e}")

# Initialize session_state
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# ---------------------------
# Function to load Lottie animations
# ---------------------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show():
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
        st.markdown("""
        <style>
        /* Main button styling with gradient animation */
        .custom-btn {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 50%, #6a11cb 100%);
            background-size: 200% 200%;
            color: white !important;
            padding: 14px 32px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(106, 17, 203, 0.4);
            transition: all 0.4s ease-in-out;
            position: relative;
            overflow: hidden;
            margin: 8px 0;
            width: 100%;
        }
        
        /* Gradient animation on hover */
        .custom-btn:hover {
            background-position: 100% 100%;
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 8px 25px rgba(142, 45, 226, 0.5);
        }
        
        /* Disease card styling */
        .cta-button {
            display: block;
            margin: 50px auto;
            padding: 18px 45px;
            background: linear-gradient(135deg, #ffd166, #ff9e6d);
            color: #000000;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            text-align: center;
            transition: all 0.5s ease;
            text-decoration: none;
            box-shadow: 0 8px 25px rgba(255, 209, 102, 0.4);
            position: relative;
            overflow: hidden;
        }

        .cta-button:hover {
            background: linear-gradient(135deg, #ff9e6d, #ffd166);
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 35px rgba(255, 209, 102, 0.6);
            color: #000000;
        }
        
        /* Custom Streamlit Button Styling with Advanced Animations */
        .stButton > button {
            width: 100% !important;
            transition: all 0.5s ease !important;
            font-weight: bold !important;
            border: none !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        /* Brain Tumor Analyze Button - Animated Neon Green */
        .stButton > button[key="brain-btn"] {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 25%, #11998e 50%, #38ef7d 75%, #11998e 100%) !important;
            background-size: 300% 300% !important;
            color: white !important;
            padding: 18px 45px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border: 2px solid #00ff88 !important;
            cursor: pointer !important;
            border-radius: 15px !important;
            box-shadow: 0 0 20px rgba(17, 153, 142, 0.6), 
                        inset 0 0 15px rgba(56, 239, 125, 0.3) !important;
            animation: brainGlow 3s ease-in-out infinite, 
                    brainGradient 4s ease infinite !important;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
        }

        .stButton > button[key="brain-btn"]:hover {
            animation: brainPulse 0.6s ease-in-out, 
                    brainGradient 2s ease infinite !important;
            transform: translateY(-5px) scale(1.05) !important;
            box-shadow: 0 0 30px rgba(56, 239, 125, 0.8),
                        0 0 60px rgba(17, 153, 142, 0.4),
                        inset 0 0 20px rgba(56, 239, 125, 0.5) !important;
        }

        @keyframes brainGlow {
            0%, 100% { box-shadow: 0 0 20px rgba(17, 153, 142, 0.6), inset 0 0 15px rgba(56, 239, 125, 0.3); }
            50% { box-shadow: 0 0 30px rgba(56, 239, 125, 0.8), inset 0 0 20px rgba(56, 239, 125, 0.5); }
        }

        @keyframes brainGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes brainPulse {
            0% { transform: translateY(-5px) scale(1.05); }
            50% { transform: translateY(-5px) scale(1.08); }
            100% { transform: translateY(-5px) scale(1.05); }
        }
        
        /* Heart Disease Analyze Button - Pulsing Red Heartbeat */
        .stButton > button[key="btn_heart"] {
            background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 25%, #ff6b6b 50%, #ff8e8e 75%, #ff6b6b 100%) !important;
            background-size: 300% 300% !important;
            color: white !important;
            padding: 18px 45px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            border: 2px solid #ff4444 !important;
            cursor: pointer !important;
            border-radius: 20px 5px 20px 5px !important;
            box-shadow: 0 0 25px rgba(255, 107, 107, 0.5),
                        inset 0 0 15px rgba(255, 255, 255, 0.2) !important;
            animation: heartbeat 1.5s ease-in-out infinite,
                    heartGradient 3s ease infinite !important;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.7) !important;
            clip-path: polygon(0 0, 100% 0, 95% 100%, 5% 100%) !important;
        }

        .stButton > button[key="btn_heart"]:hover {
            animation: heartPulse 0.8s ease-in-out,
                    heartGradient 2s ease infinite !important;
            transform: translateY(-4px) scale(1.06) !important;
            box-shadow: 0 0 35px rgba(255, 107, 107, 0.8),
                        0 0 70px rgba(255, 142, 142, 0.4),
                        inset 0 0 25px rgba(255, 255, 255, 0.3) !important;
        }

        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.02); }
            50% { transform: scale(1); }
            75% { transform: scale(1.02); }
        }

        @keyframes heartPulse {
            0% { transform: translateY(-4px) scale(1.06); }
            50% { transform: translateY(-4px) scale(1.09); }
            100% { transform: translateY(-4px) scale(1.06); }
        }

        @keyframes heartGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
            
        .disease-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 12px 30px rgba(0, 224, 255, 0.2);
            border: 1px solid #00e0ff;
        }
        
        /* Disease header styling */
        .disease-header {
            text-align: center;
            margin-bottom: 15px;
        }
        
        .disease-icon {
            font-size: 32px;
            margin-bottom: 8px;
            text-shadow: 0 0 20px rgba(0, 224, 255, 0.5);
        }
        
        .disease-name {
            font-size: 20px;
            font-weight: bold;
            color: #00e0ff;
            text-shadow: 0 2px 10px rgba(0, 224, 255, 0.4);
            margin: 5px 0;
            letter-spacing: 0.5px;
            background: linear-gradient(45deg, #00e0ff, #00b3ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Description styling */
        .disease-desc {
            font-size: 14px;
            color: #e0e0e0;
            margin-bottom: 15px;
            line-height: 1.5;
            padding: 0 10px;
        }
        
        /* Stats styling */
        .disease-stats {
            background: rgba(0, 224, 255, 0.1);
            padding: 8px 12px;
            border-radius: 10px;
            font-size: 12px;
            color: #00e0ff;
            margin: 10px 0;
            border: 1px solid rgba(0, 224, 255, 0.3);
        }
        
        .back-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-size: 200% 200%;
            color: white !important;
            padding: 6px 18px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
            transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }

        .back-btn:hover {
            background-position: 100% 100%;
            transform: translateX(-3px) scale(1.05);
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.5);
            border-color: rgba(255, 255, 255, 0.3);
        }
        
        /* Page transition animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .page-content {
            animation: fadeIn 0.5s ease-out;
        }
        </style>
        """, unsafe_allow_html=True)

        # ---------------------------
        # Lottie Animation URLs
        # ---------------------------
        lottie_urls = {
            "Brain Tumor": "https://lottie.host/a96a25e2-48c2-4a3f-948d-329319ee34fa/19F2qxjhD6.json",
            "Heart Disease": "https://lottie.host/3dd06959-12fe-4ae4-b371-77a954be451b/10hGU2FMAB.json",
            "Lung Disease": "https://lottie.host/678eece9-a7ca-4f77-9c26-e783b0a5ac63/rqcXjTPPet.json",
            "Eye Disease": "https://lottie.host/7bbaf2d5-172b-4034-b15b-0bf0a5559505/fPwaLRNSWh.json",
            "Kidney Disease": "https://lottie.host/9ea627c0-9fc1-4869-9504-721f539bcdf9/CMQ7ggeDvj.json"
        }
            
        # Load all animations
        animations = {name: load_lottieurl(url) for name, url in lottie_urls.items()}

        # Disease descriptions
        disease_descriptions = {
            "Brain Tumor": "Analyze MRI scans for tumor detection and classification using advanced AI algorithms with 95% accuracy.",
            "Heart Disease": "Predict cardiovascular conditions and assess heart health risk factors through comprehensive analysis.",
            "Lung Disease": "Detect pulmonary conditions and analyze respiratory health from medical images with deep learning."
        }

        # Disease statistics
        disease_stats = {
            "Brain Tumor": "🎯 80-85% Accuracy | ⏱️ 30s Analysis",
            "Heart Disease": "🎯 80% Accuracy | ⏱️ 45s Analysis", 
            "Lung Disease": "🎯 84% Accuracy | ⏱️ 35s Analysis",
            "Eye Disease": "🎯 81% Accuracy | ⏱️ 40s Analysis",
            "Kidney Disease": "🎯 85% Accuracy | ⏱️ 35s Analysis"
        }

        # Navigation functions
        def go_to_home():
            st.session_state.current_page = "home"

        def go_to_brain_tumor():
            st.session_state.current_page = "brain_tumor"

        def go_to_heart_disease():
            st.session_state.current_page = "heart_disease"

        def go_to_lung_disease():
            st.session_state.current_page = "lung_disease"
        
        def go_to_eye():
            st.session_state.current_page = "eye_disease"

        def go_to_kidney():
            st.session_state.current_page = "kidney_disease"

        # Home page
        if st.session_state.current_page == "home":
            st.markdown('<div class="page-content">', unsafe_allow_html=True)
            
            st.markdown("""
                <div style="text-align: center; padding: 35px 0;">
                    <div style="
                        background: linear-gradient(135deg, rgba(147, 51, 234, 0.1), rgba(219, 39, 119, 0.1));
                        border: 1px solid rgba(192, 132, 252, 0.4);
                        border-radius: 20px;
                        padding: 30px;
                        margin: 0 auto;
                        max-width: 800px;
                        box-shadow: 0 10px 30px rgba(147, 51, 234, 0.15);
                        animation: pulseGlow 3s ease-in-out infinite;
                    ">
                        <h1 style="
                            background: linear-gradient(45deg, #c084fc, #ec4899, #c084fc);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;
                            background-clip: text;
                            font-size: 2.5em;
                            margin-bottom: 15px;
                            text-shadow: 0 0 30px rgba(192, 132, 252, 0.5);
                        ">
                            AI Doctor - Multi-Disease Prediction 🩺
                        </h1>
                </div>
                
                <style>
                    @keyframes pulseGlow {
                        0%, 100% { 
                            box-shadow: 0 10px 30px rgba(147, 51, 234, 0.15);
                            border-color: rgba(192, 132, 252, 0.4);
                        }
                        50% { 
                            box-shadow: 0 15px 45px rgba(219, 39, 119, 0.25);
                            border-color: rgba(236, 72, 153, 0.6);
                        }
                    }
                </style>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 20px; margin-bottom: 10px;">
                    <div style="flex: 1; max-width: 150px; height: 2px; background: linear-gradient(90deg, transparent, #00e0ff, #00e0ff);"></div>
                    <h3 style="
                        color: #38ef7d;
                        font-weight: 600;
                        font-size: 1.4em;
                        white-space: nowrap;
                        margin: 0;
                        text-shadow: 0 0 10px rgba(56, 239, 125, 0.3);
                    ">
                        Choose the Module you want to go with 🧬
                    </h3>
                    <div style="flex: 1; max-width: 150px; height: 2px; background: linear-gradient(90deg, #38ef7d, #38ef7d, transparent);"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
            st.write("")
            
            # Create three columns for diseases
            col1, col2, col3 = st.columns(3)
            
            # Brain Tumor Card
            with col1:
                st.markdown('<div class="disease-card">', unsafe_allow_html=True)
                st.markdown("""
                <div class="disease-header">
                    <div class="disease-name">BRAIN TUMOR</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Lottie animation
                if animations["Brain Tumor"]:
                    st_lottie(animations["Brain Tumor"], height=140, key="brain_anim")
                else:
                    st.error("Animation failed to load")
                
                # Stats
                st.markdown(f'<div class="disease-stats">{disease_stats["Brain Tumor"]}</div>', unsafe_allow_html=True)
                
                # Animated Analyze Button - Neon Green Brain
                if st.button("🧠 Analyze Brain MRI", key="brain-btn", use_container_width=True):
                    go_to_brain_tumor()
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)

            # Heart Disease Card
            with col2:
                st.markdown('<div class="disease-card">', unsafe_allow_html=True)
                st.markdown("""
                <div class="disease-header">
                    <div class="disease-name">HEART DISEASE</div>
                </div>
                """, unsafe_allow_html=True)

                # Lottie animation
                if animations["Heart Disease"]:
                    st_lottie(animations["Heart Disease"], height=140, key="heart_anim")
                else:
                    st.error("Animation failed to load")
                
                # Stats
                st.markdown(f'<div class="disease-stats">{disease_stats["Heart Disease"]}</div>', unsafe_allow_html=True)
                
                # Description
                # st.markdown(f'<div class="disease-desc">{disease_descriptions["Heart Disease"]}</div>', unsafe_allow_html=True)
                
                # Animated Analyze Button - Pulsing Red Heart
                if st.button("❤️ Analyze Heart Health", key="btn_heart", use_container_width=True):
                    go_to_heart_disease()
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)

            # Lung Disease Card
            with col3:
                st.markdown('<div class="disease-card">', unsafe_allow_html=True)
                st.markdown("""
                <div class="disease-header">
                    <div class="disease-name">LUNG DISEASE</div>
                </div>
                """, unsafe_allow_html=True)
                
            
                
                # Lottie animation
                if animations["Lung Disease"]:
                    st_lottie(animations["Lung Disease"], height=140, key="lung_anim")
                else:
                    st.markdown("<div style='font-size: 60px; text-align: center; margin: 20px 0;'>🫁</div>", unsafe_allow_html=True)
                
                # Stats
                st.markdown(f'<div class="disease-stats">{disease_stats["Lung Disease"]}</div>', unsafe_allow_html=True)
                
                # Description
                # st.markdown(f'<div class="disease-desc">{disease_descriptions["Lung Disease"]}</div>', unsafe_allow_html=True)
                
                # Animated Analyze Button - Breathing Purple Lungs
                if st.button("🫁 Analyze Lung Health", key="btn_lung", use_container_width=True):
                    go_to_lung_disease()
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)
            with col1:
                # st.video('https://youtu.be/ZASsQCHPYH0?si=3cmbevwLem9N0BuH')
                st.markdown('<div class="disease-card">', unsafe_allow_html=True)
                st.markdown("""
                <div class="disease-header">
                    <div class="disease-name">EYE DISEASE</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Lottie animation
                if animations["Eye Disease"]:
                    st_lottie(animations["Eye Disease"], height=140, key="eye_anim")
                else:
                    st.markdown("<div style='font-size: 60px; text-align: center; margin: 20px 0;'>👁️</div>", unsafe_allow_html=True)
                
                # Stats
                st.markdown(f'<div class="disease-stats">{disease_stats["Eye Disease"]}</div>', unsafe_allow_html=True)
                
                # Description
                # st.markdown(f'<div class="disease-desc">{disease_descriptions["Lung Disease"]}</div>', unsafe_allow_html=True)
                
                # Animated Analyze Button - Breathing Purple Lungs
                # if st.button("Check Eye Care", key="btn_lung", use_container_width=True):
                if st.button("👁️ Check Eye Care"):
                    go_to_eye()
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            # st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="disease-card">', unsafe_allow_html=True)
                st.markdown("""
                <div class="disease-header">
                    <div class="disease-name">CHRONIC KIDNEY DISEASE</div>
                </div>
                """, unsafe_allow_html=True)

                # Lottie animation
                if animations["Kidney Disease"]:
                    st_lottie(animations["Kidney Disease"], height=140, key="kidney_anim")
                else:
                    st.error("Animation failed to load")
                
                # Stats
                st.markdown(f'<div class="disease-stats">{disease_stats["Kidney Disease"]}</div>', unsafe_allow_html=True)
                
                # Animated Analyze Button - Pulsing Red Heart
                if st.button("🧬 Analyze Kidney Health"):
                    go_to_kidney()
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)

            
            st.markdown('</div>', unsafe_allow_html=True)

        # Brain Tumor page
        elif st.session_state.current_page == "brain_tumor":
            st.markdown('<div class="page-content">', unsafe_allow_html=True)
            
            # Back button
            if st.button("⬅️ Back to Disease Selection", key="back_brain"):
                go_to_home()
                st.rerun()
            
            with st.spinner("🧠 Loading Brain Tumor Detection Module..."):
                time.sleep(1.5)
            
            st.success("Brain Tumor module loaded successfully!✅")
            
            # Call the function from brain_tumor.py
            try:
                brain_tumor.brain()
            except Exception as e:
                st.error(f"Error loading brain tumor module: {e}")
                if st.button("🔄 Return to Home"):
                    go_to_home()
                    st.rerun()
                
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.current_page == "heart_disease":
            if st.button("⬅️ Back to Disease Selection", key="back_brain"):
                go_to_home()
                st.rerun()
            with st.spinner("Loading Heart Disease Detection Module..."):
                time.sleep(1.5)
            
            # st.success("Heart Disease module loaded successfully!✅")
            
            
            try:
                heart_disease.heart()
            except Exception as e:
                st.error(f"Error loading heart disease module: {e}")
                if st.button("🔄 Return to Home"):
                    go_to_home()
                    st.rerun()
        
        elif st.session_state.current_page == "lung_disease":
            if st.button("⬅️ Back to Disease Selection", key="back_brain"):
                go_to_home()
                st.rerun()
            with st.spinner("Loading Lung Disease Detection Module..."):
                time.sleep(1.5)
            
            # st.success("Lung Disease module loaded successfully!✅")
           
            try:
                lung_disease.lung()
            except Exception as e:
                st.error(f"Error loading lung disease module: {e}")
                if st.button("🔄 Return to Home"):
                    go_to_home()
                    st.rerun()

        elif st.session_state.current_page == "eye_disease":
            st.markdown('<div class="page-content">', unsafe_allow_html=True)
            
            # Back button
            if st.button("⬅️ Back to Disease Selection", key="back_brain"):
                go_to_home()
                st.rerun()
            
            with st.spinner("Loading Eye Disease Module..."):
                time.sleep(1.5)
            
            # st.success("Eye Disease Module loaded successfully!✅")
            
            # Call the function from brain_tumor.py
            try:
                eye.ankhen()
            except Exception as e:
                st.error(f"Error loading eye disease module: {e}")
                if st.button("🔄 Return to Home"):
                    go_to_home()
                    st.rerun()
        

        elif st.session_state.current_page == "kidney_disease":
            if st.button("⬅️ Back to Disease Selection", key="back_brain"):
                go_to_home()
                st.rerun()
            with st.spinner("Loading Kidney Disease Detection Module..."):
                time.sleep(1.5)
            
            # st.success("Heart Disease module loaded successfully!✅")
            
            # Call the function from brain_tumor.py
            try:
                kidney_disease.kidney()
            except Exception as e:
                st.error(f"Error loading heart disease module: {e}")
                if st.button("🔄 Return to Home"):
                    go_to_home()
                    st.rerun()
                
            st.markdown('</div>', unsafe_allow_html=True)
                