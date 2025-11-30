import streamlit as st

def sugg():
    st.markdown("""
    <style>
        body {
            background-color: #2f3136;
            color: white;
        }

        [data-testid="stAppViewContainer"] {
            background-image: url("https://cdn.discordapp.com/attachments/1294905019388395563/1431685950852960266/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0zNzNiYXRjaDE1LWJnLTExLmpwZw.png");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        [data-testid="stHeader"] {
            background: rgba(0, 0, 0, 0);
        }

        .symptom-card {
            border-radius: 20px;
            border: 2px solid #99aab5;
            padding: 12px;
            margin: 10px;
            text-align: center;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            background: rgba(54, 57, 63, 0.8);
        }

        .symptom-card:hover {
            transform: scale(1.05);
            border-color: #7289da;
            box-shadow: 0px 0px 20px #7289da;
        }

        .selected {
            border-color: #43b581 !important;
            box-shadow: 0px 0px 25px #43b581 !important;
            background: rgba(67, 181, 129, 0.2);
        }

        .symptom-img {
            width: 150px;
            height: 100px;
            border-radius: 15px;
            object-fit: cover;
            margin-bottom: 10px;
        }

        .symptom-name {
            font-size: 18px;
            font-weight: 600;
        }

        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 0 0 10px #7289da;
            margin-bottom: 30px;
        }
        
        .button-container {
            margin-top: 10px;
            margin-bottom: 15px;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="title">🩺 Select the Symptoms You Are Experiencing</div>', unsafe_allow_html=True)

    # Symptom list
    symptoms = [
        {"name": "Itching", "img": "https://hips.hearstapps.com/hmg-prod/images/what-causes-itching-1570469798.png?crop=0.668xw:1.00xh;0.173xw,0&resize=640:*"},
        {"name": "Skin Rash", "img": "https://images.medicinenet.com/images/article/main_image/contact-dermatitis-rash-itch.jpg?output-quality=75"},
        {"name": "Nodal Skin Eruptions", "img": "https://www.hopkinsmedicine.org/-/media/images/health/1_-conditions/skin/man-with-scaly-flaky-skin-around-his-face-teaser.jpg?h=320&iar=0&w=560&hash=4E646D11BF56E3EA3E8411396B385E2D"},
        {"name": "Continuous Sneezing", "img": "https://www.nugenomics.in/wp-content/uploads/2023/04/Nugenomics-Blog-2-scaled-1.jpg"},
        {"name": "Shivering", "img": "https://static.independent.co.uk/2022/12/13/11/13105629-3eba5ac1-95e4-4227-b517-1fe172776a70.jpg"},
        {"name": "Stomach Pain", "img": "https://www.emergencyphysicians.org/siteassets/emphysicians/all-images/kwtg/stomach-ache3.jpg"},
        {"name": "Cough", "img": "https://cdn.prod.website-files.com/5ee7039040ea6efb80d7521c/603377e8a4756404f5cd9b92_Conundrums_5_Types_of_Coughs_in_Kids.jpeg"},
        {"name": "Headache", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMZtmuuMDR_e_NeUvkK1veVQ0Q48wkyKGZnA&s"},
        {"name": "Fever", "img": "https://t4.ftcdn.net/jpg/02/95/51/51/360_F_295515132_gv62hHBccX4N69uy6SGxFEqrsRVa5Bdb.jpg"},
        {"name": "Fatigue", "img": "https://muscha.org/wp-content/uploads/2019/02/fatigued-woman-1200x795.jpg"},
        {"name": "Vomiting", "img": "https://drupal-cdn-hfaeddcdbng5hfbg.a01.azurefd.net/sites/default/files/2025-02/Nausea-and-Vomiting-scaled.jpg"},
        {"name": "Diarrhea", "img": "https://www.drhc.ae/hubfs/Diarrhea%20Dubai%20General%20Medicine%20Clinic.jpg"},
        {"name": "Chest Pain", "img": "https://craftbodyscan.com/wp-content/uploads/2024/05/experiencing-chest-pain.webp"},
        {"name": "Shortness of Breath", "img": "https://sa1s3optim.patientpop.com/assets/images/provider/photos/2252940.jpeg"},
        {"name": "Joint Pain", "img": "https://cdn.painscale.com/cms/imgs/dd427880-a85c-11ea-835d-4bb524880da2.jpg"},
        {"name": "Weight Loss", "img": "https://www.helpguide.org/wp-content/uploads/2023/02/Weight-Loss-1.jpeg"},
        {"name": "Nausea", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMAxNNCgnT3lVJ4BDakd2ut-m9Opj9ac2A5w&s"},
        {"name": "Sweating", "img": "https://vitalrecord.tamu.edu/wp-content/uploads/2016/05/w_sweating_thefacialfitness.jpg"},
        {"name": "Insomnia", "img": "https://www.health.com/thmb/z5hP-BUm8CS-iuTa5o9GcE-iRZ4=/2000x0/filters:no_upscale():max_bytes(150000):strip_icc()/sleep-insomnia-AdobeStock_279764198-28e7ca58aa8d42caa1e9ada2ceb8f25d.jpg"},
        {"name": "Anxiety & Depression", "img": "https://images.indianexpress.com/2021/11/post-covid-weakness.jpg"},
        {"name": "Blurred Vision", "img": "https://www.elmanretina.com/wp-content/uploads/blurry_vision.jpg"},
        {"name": "Numbness", "img": "https://assets.yourpractice.online/2459/3d-images/hand-numbness-h.jpg"},
        {"name": "Swelling", "img": "https://content.health.harvard.edu/wp-content/uploads/2023/09/d1779065-110c-49bf-aa56-e8d9bcb443d1.jpg"}
    ]

    # Initialize session state
    if "selected" not in st.session_state:
        st.session_state.selected = []

    def toggle(symptom):
        if symptom in st.session_state.selected:
            st.session_state.selected.remove(symptom)
        else:
            st.session_state.selected.append(symptom)

    # Display symptom grid
    cols = st.columns(3)
    for i, s in enumerate(symptoms):
        with cols[i % 3]:
            selected = s["name"] in st.session_state.selected
            css_class = "symptom-card selected" if selected else "symptom-card"

            st.markdown(f"""
            <div class="{css_class}">
                <img src="{s['img']}" class="symptom-img">
                <div class="symptom-name">{s['name']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="button-container">', unsafe_allow_html=True)
            cols1 = st.columns([1, 2, 1])  
            with cols1[1]:
                button_label = f"{'✅ 𝗗𝗘𝗦𝗘𝗟𝗘𝗖𝗧' if selected else '⚡ 𝗦𝗘𝗟𝗘𝗖𝗧 ⚡'}"
                
                if st.button(button_label, key=s['name']):
                    toggle(s["name"])
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("✅ Selected Symptoms:")
    if st.session_state.selected:
        st.success(", ".join(st.session_state.selected))
    else:
        st.warning("No symptoms selected yet")

    # --- Disease Prediction Section ---
    st.markdown("### 🧠 Disease Prediction")
    if st.button("🔍 Predict Disease", type="primary", use_container_width=True):
        selected = set(st.session_state.selected)

        # --- Simple Symptom-to-Disease Mapping (replace later with ML model) ---
        disease_map = {
            frozenset(["Itching", "Skin Rash", "Nodal Skin Eruptions"]): 
                ("Fungal Infection", ["Use antifungal cream", "Keep area dry", "Avoid tight clothes"]),
            frozenset(["Cough", "Fever", "Fatigue"]): 
                ("Viral Infection", ["Stay hydrated", "Take rest", "Paracetamol if needed"]),
            frozenset(["Chest Pain", "Shortness of Breath", "Fatigue"]): 
                ("Heart Disease", ["Consult cardiologist", "Avoid stress", "Regular check-up"]),
            frozenset(["Headache", "Nausea", "Vomiting"]): 
                ("Migraine", ["Rest in dark room", "Avoid loud noise", "Stay hydrated"]),
            frozenset(["Diarrhea", "Vomiting", "Fever"]): 
                ("Food Poisoning", ["Drink ORS", "Avoid outside food", "Consult doctor if persists"]),
        }

        predicted = None
        precautions = []

        for key, (disease, precs) in disease_map.items():
            if key.issubset(selected):
                predicted = disease
                precautions = precs
                break

        if predicted:
            st.success(f"🩸 **Predicted Disease:** {predicted}")
            st.info("### 🩹 Precautions:")
            for p in precautions:
                st.markdown(f"- {p}")
        else:
            st.warning("⚠️ No exact match found. Try selecting more symptoms for better accuracy.")
