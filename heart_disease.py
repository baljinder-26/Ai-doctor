import streamlit as st
import random

# Custom CSS for clean look
def heart():
    discord_bg_url = "https://t3.ftcdn.net/jpg/07/34/16/52/360_F_734165295_bHzRvuB74SQsPuspUgcTEQAwROrv3pTy.jpg" #Example animated discord-like background
    # discord_bg_url="https://t4.ftcdn.net/jpg/05/64/05/49/360_F_564054980_NpVuWxBcFSXyvaBYdB2zPFSKTol5f2XV.jpg"
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
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            background: linear-gradient(90deg, #FF0000, #0000FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            margin-bottom: 2rem;
            font-weight: bold;
        }
        .tip-card {
            background: #000080;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid #1E90FF;
        }
        .emergency {
            background: #8B0000;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border: 2px solid #FF0000;
            font-weight: bold;
        }
        .mild-card {
            background: #228B22;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid #32CD32;
        }
        .moderate-card {
            background: #FF8C00;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid #FFA500;
        }
        .daily-tip-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
            border: 3px solid #ff4b4b;
        }
        .tip-button {
            background: linear-gradient(45deg, #FF4B4B, #FF6B6B);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            margin: 10px 0;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
            transition: all 0.3s ease;
        }
        .tip-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

    # Heart Disease Types Database
    HEART_DISEASE_TIPS = {
        "coronary artery disease": {
            "level": "High Risk",
            "tips": [
                "🫀 Get regular cholesterol and blood pressure checks",
                "💊 Take prescribed medications like statins and aspirin",
                "🚶 Walk 30 minutes daily to improve circulation",
                "🥑 Eat Mediterranean diet rich in healthy fats",
                "😴 Manage stress through meditation and proper sleep",
                "🚭 Quit smoking immediately - it's the #1 risk factor"
            ],
            "symptoms": [
                "Chest pain (angina)",
                "Shortness of breath",
                "Heart palpitations",
                "Fatigue during physical activity",
                "Pain in shoulders or arms"
            ]
        },
        "heart failure": {
            "level": "Serious Condition",
            "tips": [
                "⚖️ Monitor weight daily - sudden gain means fluid retention",
                "🧂 Limit salt intake to less than 1500mg per day",
                "💧 Restrict fluids as advised by doctor",
                "💊 Take diuretics and other heart medications regularly",
                "🏥 Attend all follow-up appointments",
                "🚨 Know emergency signs: worsening shortness of breath, swelling"
            ],
            "symptoms": [
                "Shortness of breath at rest",
                "Swelling in legs and ankles",
                "Persistent coughing",
                "Rapid weight gain",
                "Difficulty lying flat to sleep"
            ]
        }
    }

    # Daily Heart Tips
    daily_heart_tips = [
        "Check your blood pressure today if you have a monitor",
        "Take the stairs instead of elevator",
        "Add one extra vegetable to your meals",
        "Practice deep breathing for 5 minutes",
        "Replace one processed snack with fresh fruit",
        "Walk for 10 minutes after your main meal",
        "Drink a glass of water before each meal",
        "Choose whole grain bread instead of white bread",
        "Measure your waist circumference today",
        "Take a 5-minute break from sitting every hour",
        "Swap red meat for fish or plant-based protein",
        "Read food labels for sodium content",
        "Laugh intentionally for 2 minutes - it's internal jogging for your heart",
        "Try meditation or mindfulness for stress relief",
        "Get 7-8 hours of quality sleep tonight",
        "Include a handful of nuts as your daily snack",
        "Use herbs and spices instead of salt for flavor",
        "Take a 15-minute walk during your lunch break",
        "Choose olive oil instead of butter for cooking",
        "Practice gratitude by listing 3 things you're thankful for"
    ]

    # Main Title
    st.markdown('<div class="main-title">Heart Care AI Doctor</div>', unsafe_allow_html=True)

    # Search Bar for Heart Disease Types
    st.markdown("## Search Heart Disease Types🔍")
    search_term = st.text_input(
        "Search specific heart conditions:",
        placeholder="e.g., coronary artery, heart failure, arrhythmia..."
    )

    # Quick Access Buttons
    st.markdown("### Quick Access🎯")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🫀 Coronary Artery"):
            st.session_state.search_term = "coronary artery disease"
            st.rerun()

    with col2:
        if st.button("💔 Heart Failure"):
            st.session_state.search_term = "heart failure"
            st.rerun()

    with col3:
        if st.button("💓 Arrhythmia"):
            st.session_state.search_term = "arrhythmia"
            st.rerun()

    # Display search results
    if search_term or 'search_term' in st.session_state:
        if 'search_term' in st.session_state:
            search_term = st.session_state.search_term
        
        found = False
        for disease, info in HEART_DISEASE_TIPS.items():
            if search_term.lower() in disease.lower():
                found = True
                
                card_class = "emergency" if "High Risk" in info["level"] or "Serious" in info["level"] else "mild-card"
                
                st.markdown(f"## {disease.title()}")
                st.markdown(f'<div class="{card_class}">📊 Risk Level: {info["level"]}</div>', unsafe_allow_html=True)
                
                st.markdown("### Management Tips💡")
                for tip in info["tips"]:
                    st.markdown(f'<div class="tip-card">{tip}</div>', unsafe_allow_html=True)
                
                st.markdown("### 🚨 Common Symptoms")
                for symptom in info["symptoms"]:
                    st.write(f"• {symptom}")
                
                break
        
        if not found and search_term:
            st.warning("❌ No specific heart condition found. Try: coronary artery, heart failure")

    # Daily Tip Section with Clickable Button
    st.markdown("---")
    st.markdown("## Daily Heart Health Tip💡")

    # Initialize session state for tip visibility
    if 'show_tip' not in st.session_state:
        st.session_state.show_tip = False

    # Catchy button to reveal tip
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(
            "🎯 Get Today's Heart Tip!",
            key="tip_button",
            use_container_width=True
        ):
            st.session_state.show_tip = True
            st.session_state.current_tip = random.choice(daily_heart_tips)

    # Show the tip when button is clicked
    if st.session_state.show_tip:
        st.markdown(f"""
        <div class="daily-tip-box">
            <p style="font-size: 20px; margin: 15px 0;"><b>{st.session_state.current_tip}</b></p>
            <p style="font-size: 14px; opacity: 0.9;">Keep clicking for more tips!</p>
        </div>
        """, unsafe_allow_html=True)

    # Emergency Warning
    st.markdown("### Heart Attack Warning Signs🚨")
    st.markdown("""
    <div class="emergency">
    ⚠️ <b>Seek IMMEDIATE medical help for:</b>
    <br><br>
    • Chest pain or pressure lasting more than 5 minutes
    • Pain spreading to arms, back, neck, jaw
    • Severe shortness of breath
    • Cold sweat, nausea, lightheadedness
    • Unusual fatigue or weakness
    </div>
    """, unsafe_allow_html=True)

    # Disclaimer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
    ⚠️ <b>Disclaimer:</b> This is for informational purposes only. Always consult healthcare professionals for medical advice.
    </div>
    """, unsafe_allow_html=True)