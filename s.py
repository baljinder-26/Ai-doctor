import streamlit as st

def sugg():
    discord_bg_url = "https://cdn.discordapp.com/attachments/1294905019388395563/1431685950852960266/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0zNzNiYXRjaDE1LWJnLTExLmpwZw.png?ex=69004b32&is=68fef9b2&hm=9a303f3c04337f4cabf16764617fe234c8fb899a9aa84717735b3fd63a0caf7a&"
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
        .stApp > div {{
            background-color: rgba(0, 0, 0, 0.4);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #7289da;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
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
            object-fit: cover;02
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
    st.markdown(
    '<p style="color: #1E90FF; font-size:20px; font-weight:bold; text-align:center;">Note: Select the symptoms that are similar to each other</p>',
    unsafe_allow_html=True
)



    # Symptom list
    symptoms = [
        {"name": "Itching", "img": "https://hips.hearstapps.com/hmg-prod/images/what-causes-itching-1570469798.png?crop=0.668xw:1.00xh;0.173xw,0&resize=640:*"},
        {"name": "Skin Rash", "img": "https://images.medicinenet.com/images/article/main_image/contact-dermatitis-rash-itch.jpg?output-quality=75"},
        {"name": "Nodal Skin Eruptions", "img": "https://images.everydayhealth.com/images/2025/what-common-rashes-look-like-00-intro-1440x810.jpg"},
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

        # 🩹 SKIN & ALLERGY CONDITIONS
        frozenset(["Itching", "Skin Rash", "Nodal Skin Eruptions"]): 
        ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream (clotrimazole, miconazole) 2-3 times daily",
                "Keep affected area clean and completely dry",
                "Avoid tight, synthetic clothing",
                "Change clothes and underwear daily",
                "Use separate towels for affected areas",
                "Wash clothes in hot water",
                "Avoid scratching to prevent spreading",
                "Wear open-toed shoes if feet are affected",
                "Use antifungal powder in shoes and socks",
                "Complete full treatment course even if symptoms improve"
            ],
            "diet": [
                "Reduce sugar and refined carbs intake",
                "Increase probiotic foods (yogurt, kefir, kimchi)",
                "Eat garlic and onions for natural antifungal properties",
                "Include coconut oil in cooking",
                "Consume foods rich in vitamin C (citrus fruits, bell peppers)",
                "Add turmeric to meals for anti-inflammatory benefits",
                "Stay hydrated with plenty of water",
                "Avoid alcohol and fermented foods",
                "Eat zinc-rich foods (pumpkin seeds, lentils)",
                "Include omega-3 foods (fatty fish, walnuts)"
            ]
        }),
    
        frozenset(["Itching", "Skin Rash", "Continuous Sneezing"]): 
            ("Allergic Reaction", {
                "precautions": [
                    "Identify and avoid known allergens",
                    "Use antihistamines (cetirizine, loratadine) as directed",
                    "Consult dermatologist if symptoms persist",
                    "Use air purifiers with HEPA filters",
                    "Keep windows closed during high pollen seasons",
                    "Wash bedding weekly in hot water",
                    "Shower after outdoor exposure",
                    "Use hypoallergenic bedding covers",
                    "Avoid outdoor activities during high pollen counts",
                    "Keep emergency epinephrine if severe allergies"
                ],
                "diet": [
                    "Include local honey for pollen immunity",
                    "Eat quercetin-rich foods (apples, onions, berries)",
                    "Increase omega-3 fatty acids (salmon, flaxseeds)",
                    "Consume vitamin C rich foods",
                    "Add probiotic foods to diet",
                    "Include bromelain from pineapple",
                    "Eat magnesium-rich foods (spinach, almonds)",
                    "Avoid common allergens (dairy, nuts if sensitive)",
                    "Stay well hydrated with herbal teas",
                    "Include turmeric and ginger in meals"
                ]
            }),
        
        frozenset(["Itching", "Skin Rash", "Swelling"]): 
            ("Skin Allergy", {
                "precautions": [
                    "Apply calamine lotion or hydrocortisone cream",
                    "Avoid scratching affected areas",
                    "Use mild, fragrance-free soap and moisturizer",
                    "Take cool oatmeal baths",
                    "Use cold compresses to reduce swelling",
                    "Wear loose, cotton clothing",
                    "Identify and avoid trigger substances",
                    "Keep nails short and clean",
                    "Apply aloe vera gel for cooling relief",
                    "Consult doctor for severe reactions"
                ],
                "diet": [
                    "Eat anti-inflammatory foods (berries, leafy greens)",
                    "Include omega-3 rich foods",
                    "Consume zinc-rich foods for skin healing",
                    "Add vitamin E foods (nuts, seeds)",
                    "Include quercetin sources",
                    "Eat probiotic foods",
                    "Avoid processed and packaged foods",
                    "Stay hydrated with water and coconut water",
                    "Include turmeric in cooking",
                    "Eat foods rich in vitamin A (sweet potatoes, carrots)"
                ]
            }),
        
        frozenset(["Itching", "Fatigue", "Sweating"]): 
            ("Heat Rash", {
                "precautions": [
                    "Stay in cool, air-conditioned environments",
                    "Wear loose, breathable cotton clothes",
                    "Apply soothing powder (cornstarch-based)",
                    "Take cool showers frequently",
                    "Use calamine lotion for itching",
                    "Avoid heavy creams that block pores",
                    "Keep skin dry and clean",
                    "Use fans or air circulation",
                    "Avoid strenuous exercise in heat",
                    "Stay hydrated with electrolytes"
                ],
                "diet": [
                    "Drink plenty of water and electrolyte fluids",
                    "Eat water-rich fruits (watermelon, cucumber)",
                    "Include potassium-rich foods (bananas, potatoes)",
                    "Consume magnesium foods (spinach, almonds)",
                    "Avoid spicy and hot temperature foods",
                    "Eat light, easily digestible meals",
                    "Include coconut water for hydration",
                    "Avoid caffeine and alcohol",
                    "Eat small, frequent meals",
                    "Include mint and cooling herbs in diet"
                ]
            }), 

                # 😷 RESPIRATORY INFECTIONS
        frozenset(["Continuous Sneezing", "Cough", "Shivering"]): 
            ("Common Cold", {
                "precautions": [
                    "Drink warm fluids like herbal tea and soup every 2-3 hours",
                    "Take steam inhalation with eucalyptus oil 2-3 times daily",
                    "Get plenty of rest and sleep for proper recovery",
                    "Use saline nasal drops to relieve congestion",
                    "Gargle with warm salt water for sore throat relief",
                    "Wash hands frequently to prevent spreading the virus",
                    "Use a humidifier to keep air moist in your room",
                    "Take vitamin C and zinc supplements to boost immunity",
                    "Avoid close contact with family members to prevent transmission",
                    "Use disposable tissues when sneezing or coughing"
                ],
                "diet": [
                    "Drink warm chicken soup or vegetable broth regularly",
                    "Consume ginger tea with honey and lemon for soothing relief",
                    "Eat vitamin C rich foods like oranges, kiwi, and bell peppers",
                    "Include garlic in meals for its natural antiviral properties",
                    "Stay hydrated with warm water throughout the day",
                    "Eat zinc-rich foods like pumpkin seeds and lentils",
                    "Consume probiotic foods like yogurt and kefir for gut health",
                    "Avoid dairy products if they increase mucus production",
                    "Eat light, easily digestible meals like khichdi or porridge",
                    "Include turmeric in warm milk for its anti-inflammatory benefits"
                ]
            }),
        
        frozenset(["Cough", "Fever", "Fatigue"]): 
            ("Viral Infection", {
                "precautions": [
                    "Stay hydrated with water, electrolyte drinks, and oral rehydration solutions",
                    "Take complete rest and avoid physical exertion",
                    "Use paracetamol for fever and body aches as needed",
                    "Monitor body temperature every 4-6 hours",
                    "Use cough suppressants or expectorants based on cough type",
                    "Take warm steam inhalation to relieve respiratory symptoms",
                    "Get adequate sleep of 7-9 hours for recovery",
                    "Isolate yourself to prevent spreading the infection",
                    "Use a humidifier in your room to ease breathing",
                    "Consult doctor if fever persists beyond 3 days"
                ],
                "diet": [
                    "Drink plenty of fluids including herbal teas and warm water",
                    "Eat protein-rich foods like eggs, chicken, and lentils for recovery",
                    "Consume vitamin C rich fruits like oranges and strawberries",
                    "Include ginger and garlic in meals for immune support",
                    "Eat small, frequent meals to maintain energy levels",
                    "Avoid heavy, greasy, and spicy foods that are hard to digest",
                    "Drink warm water with honey and lemon for cough relief",
                    "Include zinc-rich foods like chickpeas and nuts in diet",
                    "Eat probiotic foods to support gut microbiome",
                    "Consume bone broth for essential nutrients and hydration"
                ]
            }),
        
        frozenset(["Cough", "Chest Pain", "Fever"]): 
            ("Pneumonia", {
                "precautions": [
                    "Consult physician immediately for proper diagnosis and treatment",
                    "Take prescribed antibiotics completely as directed",
                    "Monitor breathing patterns and oxygen saturation regularly",
                    "Use incentive spirometer for lung expansion exercises",
                    "Get plenty of bed rest to support recovery",
                    "Stay hydrated with warm fluids to thin mucus",
                    "Use steam inhalation to help clear respiratory passages",
                    "Practice deep breathing exercises to improve lung function",
                    "Avoid smoking and exposure to air pollutants",
                    "Seek emergency care if breathing difficulties worsen"
                ],
                "diet": [
                    "Eat high-protein foods like eggs, fish, and poultry for tissue repair",
                    "Consume vitamin A rich foods like carrots and sweet potatoes for lung health",
                    "Include vitamin C sources like citrus fruits and bell peppers",
                    "Eat small, frequent meals to maintain energy without overloading",
                    "Stay hydrated with warm broths and herbal teas",
                    "Include zinc-rich foods to support immune function",
                    "Avoid dairy products if they thicken respiratory mucus",
                    "Eat antioxidant-rich fruits like berries and pomegranates",
                    "Include garlic and onions in diet for antimicrobial properties",
                    "Consume omega-3 rich foods like walnuts and flaxseeds to reduce inflammation"
                ]
            }),
        
        frozenset(["Cough", "Shortness of Breath", "Fatigue"]): 
            ("Bronchitis", {
                "precautions": [
                    "Avoid smoking and exposure to secondhand smoke completely",
                    "Take steam inhalation with menthol or eucalyptus oil 2-3 times daily",
                    "Use prescribed bronchodilators and medications as directed",
                    "Drink plenty of warm fluids to help thin bronchial secretions",
                    "Use a humidifier in bedroom to keep air moist",
                    "Get adequate rest to allow the bronchial tubes to heal",
                    "Avoid cold air and environmental pollutants",
                    "Practice pursed-lip breathing techniques",
                    "Use cough expectorants to help clear mucus",
                    "Wear a mask in polluted or dusty environments"
                ],
                "diet": [
                    "Drink warm herbal teas with honey for cough relief",
                    "Eat anti-inflammatory foods like turmeric and ginger",
                    "Include ginger in meals and teas for its bronchodilating effects",
                    "Consume vitamin C rich foods to support immune system",
                    "Stay hydrated with warm water throughout the day",
                    "Eat garlic for its natural antimicrobial properties",
                    "Include omega-3 rich foods like salmon and chia seeds",
                    "Avoid cold drinks, ice cream, and frozen foods",
                    "Eat light, nutritious meals that are easy to digest",
                    "Consume warm chicken soup regularly for its soothing properties"
                ]
            }),
        
        frozenset(["Shortness of Breath", "Cough", "Fatigue"]): 
            ("Asthma", {
                "precautions": [
                    "Use inhaler as prescribed by your doctor without skipping doses",
                    "Avoid known triggers like pollen, dust, and pet dander",
                    "Monitor breathing patterns and peak flow regularly",
                    "Keep rescue medication accessible at all times",
                    "Create a written asthma action plan with your healthcare provider",
                    "Use air purifiers with HEPA filters in your home",
                    "Avoid strenuous exercise in cold, dry air",
                    "Practice breathing techniques like diaphragmatic breathing",
                    "Schedule regular medical check-ups with your pulmonologist",
                    "Avoid smoking and exposure to strong chemical odors"
                ],
                "diet": [
                    "Eat omega-3 rich foods like salmon, walnuts, and flaxseeds to reduce inflammation",
                    "Include magnesium-rich foods like spinach, almonds, and avocados",
                    "Consume vitamin C rich fruits and vegetables for antioxidant support",
                    "Eat antioxidant-rich berries like blueberries and strawberries",
                    "Include ginger and turmeric in meals for their anti-inflammatory properties",
                    "Avoid sulfite-containing foods like dried fruits and wine if sensitive",
                    "Stay well hydrated with water and herbal teas",
                    "Eat small, frequent meals to avoid pressure on diaphragm",
                    "Include probiotic foods to support immune system regulation",
                    "Consume apples and onions regularly for their quercetin content"
                ]
            }),

        frozenset(["Chest Pain", "Shortness of Breath", "Sweating"]): 
            ("Heart Attack (Emergency)", {
                "precautions": [
                    "Call emergency services immediately - do not delay",
                    "Chew and swallow aspirin (325mg) if not allergic and advised by doctor",
                    "Stay calm and sit down in a comfortable position",
                    "Loosen tight clothing, especially around neck and chest",
                    "Do not attempt to drive yourself to the hospital",
                    "Keep emergency contact numbers easily accessible",
                    "Learn basic CPR and first aid techniques",
                    "Schedule regular heart health check-ups",
                    "Monitor blood pressure and cholesterol regularly",
                    "Carry medical information and current medications list"
                ],
                "diet": [
                    "Follow a low-sodium diet long-term for heart health",
                    "Eat plenty of fresh fruits and vegetables daily",
                    "Include whole grains like oats and brown rice in diet",
                    "Consume lean proteins like fish and skinless poultry",
                    "Use healthy fats like olive oil and avocados",
                    "Avoid processed and packaged foods high in salt",
                    "Limit red meat and high-fat dairy products",
                    "Practice portion control to maintain healthy weight",
                    "Reduce intake of saturated and trans fats",
                    "Increase dietary fiber through legumes and vegetables"
                ]
            }),
            # 💖 CARDIOVASCULAR & SYSTEMIC
            frozenset(["Chest Pain", "Shortness of Breath", "Fatigue"]): 
            ("Heart Disease", {
                "precautions": [
                    "Consult cardiologist for comprehensive evaluation and treatment plan",
                    "Avoid stress through meditation, yoga, and relaxation techniques",
                    "Regular check-up including ECG, echocardiogram, and blood tests",
                    "Take prescribed medications regularly without missing doses",
                    "Monitor blood pressure and heart rate daily",
                    "Avoid sudden physical exertion and heavy lifting",
                    "Maintain healthy weight through balanced diet and exercise",
                    "Quit smoking and avoid secondhand smoke exposure",
                    "Limit alcohol consumption to moderate levels",
                    "Learn warning signs of heart attack and emergency procedures"
                ],
                "diet": [
                    "Follow Mediterranean-style diet rich in fruits and vegetables",
                    "Consume low-sodium foods and avoid added salt",
                    "Include healthy fats from olive oil, nuts, and avocados",
                    "Eat high-fiber foods like oats, legumes, and whole grains",
                    "Choose lean proteins like fish, skinless poultry, and plant proteins",
                    "Avoid processed foods, fried items, and trans fats",
                    "Include potassium-rich foods like bananas and leafy greens",
                    "Eat small, frequent meals instead of large heavy meals",
                    "Limit red meat and high-cholesterol foods",
                    "Stay hydrated with water and herbal teas"
                ]
            }),
        
        frozenset(["Chest Pain", "Sweating", "Fatigue"]): 
            ("Angina", {
                "precautions": [
                    "Rest immediately when chest pain occurs - sit or lie down",
                    "Avoid physical exertion and emotional stress triggers",
                    "Consult cardiologist for ECG, stress test, and proper diagnosis",
                    "Take prescribed nitroglycerin medication as directed",
                    "Keep emergency medication accessible at all times",
                    "Monitor pattern, frequency, and duration of angina episodes",
                    "Avoid extreme temperatures - both hot and cold environments",
                    "Pace physical activities and take frequent breaks",
                    "Carry medical information and emergency contacts",
                    "Attend regular follow-up appointments with cardiologist"
                ],
                "diet": [
                    "Eat small, frequent meals to avoid overloading the heart",
                    "Follow low-cholesterol diet with limited saturated fats",
                    "Include potassium-rich foods like bananas and sweet potatoes",
                    "Consume magnesium sources like nuts, seeds, and leafy greens",
                    "Avoid heavy meals, especially before physical activity",
                    "Limit caffeine intake which can trigger angina symptoms",
                    "Include healthy fats from fish, nuts, and olive oil",
                    "Eat high-fiber foods to maintain healthy cholesterol levels",
                    "Choose antioxidant-rich fruits and vegetables",
                    "Stay well-hydrated with water throughout the day"
                ]
            }),
        
        frozenset(["Headache", "Fatigue", "Blurred Vision"]): 
            ("Hypertension", {
                "precautions": [
                    "Monitor blood pressure regularly with home monitoring device",
                    "Reduce salt intake to less than 1500-2000mg per day",
                    "Avoid stress through mindfulness and relaxation practices",
                    "Take prescribed blood pressure medications consistently",
                    "Maintain healthy weight through diet and exercise",
                    "Limit alcohol consumption to moderate levels",
                    "Quit smoking and avoid tobacco products",
                    "Get regular exercise - 30 minutes most days",
                    "Ensure adequate sleep of 7-8 hours nightly",
                    "Schedule regular follow-ups with healthcare provider"
                ],
                "diet": [
                    "Follow DASH diet principles (Dietary Approaches to Stop Hypertension)",
                    "Eat potassium-rich foods like bananas, potatoes, and spinach",
                    "Include magnesium sources such as almonds and avocados",
                    "Consume calcium-rich foods like low-fat dairy and leafy greens",
                    "Choose low-sodium options and avoid processed foods",
                    "Eat plenty of fresh fruits and vegetables daily",
                    "Include whole grains like oatmeal and brown rice",
                    "Select lean protein sources like fish and poultry",
                    "Use healthy cooking methods - baking, steaming, grilling",
                    "Limit caffeine and high-sugar beverages"
                ]
            }),
        
        frozenset(["Fatigue", "Sweating", "Weight Loss"]): 
            ("Thyroid Imbalance", {
                "precautions": [
                    "Get comprehensive thyroid function tests (TSH, T3, T4 levels)",
                    "Avoid excessive caffeine and stimulants that worsen symptoms",
                    "Consult endocrinologist for proper diagnosis and treatment",
                    "Take thyroid medication consistently at same time daily",
                    "Monitor symptoms and keep track of changes regularly",
                    "Get regular follow-up blood tests as recommended",
                    "Take medication on empty stomach for better absorption",
                    "Manage stress levels through yoga and meditation",
                    "Ensure adequate rest and quality sleep",
                    "Avoid self-adjusting medication doses without medical advice"
                ],
                "diet": [
                    "Eat balanced diet with adequate protein and complex carbohydrates",
                    "Include iodine-rich foods like seafood and dairy if deficient",
                    "Consume selenium sources like Brazil nuts, tuna, and eggs",
                    "Eat zinc-rich foods like pumpkin seeds, lentils, and chickpeas",
                    "Include iron-rich foods for energy - leafy greens, beans, lean meat",
                    "Avoid excessive raw goitrogenic foods (cabbage, broccoli, kale)",
                    "Include vitamin D sources like fortified foods and sunlight exposure",
                    "Eat omega-3 rich foods for hormone balance",
                    "Choose antioxidant-rich fruits and vegetables",
                    "Stay well-hydrated with water and herbal teas"
                ]
            }),
            # 🤒 GASTROINTESTINAL
                # 🤒 GASTROINTESTINAL
        frozenset(["Stomach Pain", "Vomiting", "Diarrhea"]): 
            ("Gastroenteritis", {
                "precautions": [
                    "Stay hydrated with oral rehydration solution (ORS) after each loose stool",
                    "Avoid spicy, oily, and heavy foods that can irritate stomach",
                    "Eat bland diet following BRAT protocol (banana, rice, applesauce, toast)",
                    "Rest digestive system by starting with clear liquids initially",
                    "Wash hands frequently with soap to prevent spreading infection",
                    "Use separate towels and utensils to avoid contaminating others",
                    "Avoid dairy products, caffeine, and alcohol during recovery",
                    "Take probiotic supplements to restore gut flora after acute phase",
                    "Gradually reintroduce normal foods over 3-5 days as symptoms improve",
                    "Consult doctor if symptoms persist beyond 48 hours or if dehydration occurs"
                ],
                "diet": [
                    "Start with clear broths, electrolyte drinks, and herbal teas",
                    "Gradually introduce BRAT foods - bananas, white rice, applesauce, dry toast",
                    "Add boiled potatoes, steamed carrots, and plain crackers as tolerated",
                    "Include probiotic-rich foods like yogurt and kefir once vomiting stops",
                    "Eat small, frequent meals instead of three large meals",
                    "Avoid raw vegetables, fruits with skins, and high-fiber foods initially",
                    "Stay away from spicy, fried, and processed foods completely",
                    "Drink ginger or peppermint tea to soothe nausea",
                    "Include well-cooked vegetables and lean proteins as recovery progresses",
                    "Maintain hydration with coconut water and clear soups"
                ]
            }),
        
        frozenset(["Diarrhea", "Vomiting", "Fever"]): 
            ("Food Poisoning", {
                "precautions": [
                    "Drink ORS solution regularly to replace lost fluids and electrolytes",
                    "Avoid outside food and stick to home-cooked, freshly prepared meals",
                    "Consult doctor if symptoms persist beyond 24 hours or worsen",
                    "Rest completely to allow body to fight the infection",
                    "Avoid anti-diarrheal medications initially to let body expel toxins",
                    "Maintain strict food hygiene and proper hand washing",
                    "Practice proper food storage and refrigeration techniques",
                    "Cook meat, poultry, and eggs thoroughly to kill bacteria",
                    "Wash fruits and vegetables properly before consumption",
                    "Disinfect kitchen surfaces and cooking utensils regularly"
                ],
                "diet": [
                    "Begin with clear liquids - ORS, electrolyte water, clear broths",
                    "Progress to BRAT diet as vomiting subsides - bananas, rice, applesauce, toast",
                    "Avoid dairy products, fatty foods, and spicy items completely",
                    "Gradually reintroduce normal foods starting with plain khichdi or congee",
                    "Take probiotics like yogurt or supplements to restore gut bacteria",
                    "Drink herbal teas like chamomile or ginger for stomach soothing",
                    "Eat plain boiled potatoes, steamed vegetables, and simple soups",
                    "Avoid raw foods, salads, and uncooked vegetables initially",
                    "Stay hydrated with coconut water and diluted fruit juices",
                    "Include easily digestible proteins like boiled eggs and chicken soup later"
                ]
            }),
        
        frozenset(["Stomach Pain", "Nausea", "Vomiting"]): 
            ("Gastritis", {
                "precautions": [
                    "Avoid spicy, oily, and acidic foods that trigger stomach irritation",
                    "Eat small frequent meals throughout the day instead of large meals",
                    "Take antacids or prescribed medications as needed for symptom relief",
                    "Avoid NSAIDs, alcohol, and smoking which worsen gastritis",
                    "Manage stress through meditation, yoga, and relaxation techniques",
                    "Elevate head of bed if experiencing nighttime reflux symptoms",
                    "Avoid late-night eating - finish meals 2-3 hours before bedtime",
                    "Identify and eliminate specific food triggers through food diary",
                    "Quit smoking and limit alcohol consumption completely",
                    "Consult gastroenterologist for proper diagnosis and treatment plan"
                ],
                "diet": [
                    "Eat bland, non-acidic foods like oatmeal, bananas, and white rice",
                    "Choose lean proteins like skinless chicken, fish, and tofu",
                    "Consume cooked vegetables rather than raw ones initially",
                    "Avoid citrus fruits, tomatoes, chocolate, and mint triggers",
                    "Eat small portions to avoid stomach over-distension",
                    "Include ginger tea or chamomile tea for nausea relief",
                    "Avoid carbonated drinks, coffee, and strong teas",
                    "Eat whole grains like brown rice and quinoa as tolerated",
                    "Include healthy fats from olive oil and avocados in moderation",
                    "Stay well-hydrated with water between meals"
                ]
            }),
        
        frozenset(["Stomach Pain", "Fatigue", "Weight Loss"]): 
            ("Ulcer", {
                "precautions": [
                    "Avoid stress through mindfulness, meditation, and adequate rest",
                    "Take proton pump inhibitors or other prescribed medications regularly",
                    "Avoid NSAIDs, smoking, and excessive alcohol consumption",
                    "Eat regular, small meals to maintain stable stomach environment",
                    "Limit alcohol and caffeine intake which can irritate ulcers",
                    "Monitor for bleeding signs like black stools or vomiting blood",
                    "Manage stress effectively through counseling if needed",
                    "Get adequate sleep and maintain regular sleep schedule",
                    "Avoid late-night meals and eating close to bedtime",
                    "Follow up regularly with gastroenterologist for monitoring"
                ],
                "diet": [
                    "Eat high-fiber foods like fruits, vegetables, and whole grains",
                    "Choose lean proteins and healthy fats for balanced nutrition",
                    "Include probiotic foods to support gut health and healing",
                    "Avoid spicy, fried, and highly processed foods completely",
                    "Eat non-acidic fruits like bananas, melons, and apples",
                    "Include cooked vegetables and well-cooked whole grains",
                    "Avoid citrus fruits, tomatoes, and vinegar-based foods",
                    "Eat small, frequent meals to prevent excessive stomach acid",
                    "Include soothing foods like oatmeal, yogurt, and bananas",
                    "Stay hydrated with water and herbal teas between meals"
                ]
            }),

        # 🧠 NEUROLOGICAL & PSYCHOLOGICAL
        frozenset(["Headache", "Nausea", "Vomiting"]): 
            ("Migraine", {
                "precautions": [
                    "Rest in dark, quiet room during migraine attacks for relief",
                    "Avoid loud noises, bright lights, and strong smells as triggers",
                    "Stay hydrated with small sips of water during episodes",
                    "Take prescribed migraine medication at first sign of attack",
                    "Apply cold compress to forehead and back of neck",
                    "Practice relaxation techniques like deep breathing during attacks",
                    "Identify and avoid personal migraine triggers through diary",
                    "Maintain consistent sleep schedule even on weekends",
                    "Avoid skipping meals and maintain regular eating schedule",
                    "Manage stress through regular exercise and mindfulness"
                ],
                "diet": [
                    "Identify and avoid trigger foods like aged cheese, processed meats",
                    "Eat regular meals to prevent low blood sugar triggering migraines",
                    "Include magnesium-rich foods like spinach, pumpkin seeds, almonds",
                    "Drink ginger tea or chew ginger for nausea relief during attacks",
                    "Stay well-hydrated throughout the day with water and electrolytes",
                    "Include riboflavin (B2) rich foods like eggs and lean meats",
                    "Eat omega-3 rich foods like salmon and walnuts for anti-inflammatory benefits",
                    "Avoid chocolate, alcohol, and artificial sweeteners if triggers",
                    "Include fresh fruits and vegetables for antioxidant support",
                    "Eat small, frequent meals to maintain stable blood sugar levels"
                ]
            }),
        
        frozenset(["Headache", "Insomnia", "Anxiety & Depression"]): 
            ("Mental Stress Disorder", {
                "precautions": [
                    "Practice meditation daily for 15-20 minutes to calm mind",
                    "Maintain sleep hygiene with consistent bedtime and wake-up time",
                    "Talk to a therapist or counselor for professional support",
                    "Limit screen time before bed and create relaxing bedtime routine",
                    "Engage in regular physical activity to reduce stress hormones",
                    "Practice deep breathing exercises during anxious moments",
                    "Set realistic goals and prioritize tasks to reduce overwhelm",
                    "Take regular breaks during work and practice mindfulness",
                    "Connect with supportive friends and family members regularly",
                    "Consider cognitive behavioral therapy for long-term management"
                ],
                "diet": [
                    "Eat complex carbohydrates like whole grains for steady energy",
                    "Include omega-3 fatty acids from fish, walnuts, and flaxseeds",
                    "Consume magnesium-rich foods like leafy greens, nuts, and seeds",
                    "Limit caffeine and alcohol intake which can worsen anxiety",
                    "Eat regular, balanced meals to maintain stable blood sugar",
                    "Include B-vitamin rich foods like eggs, legumes, and whole grains",
                    "Eat tryptophan sources like turkey, bananas, and oats for serotonin",
                    "Include antioxidant-rich fruits and vegetables for brain health",
                    "Stay hydrated with water and herbal calming teas",
                    "Avoid processed foods and excessive sugar which can mood swings"
                ]
            }),
        
        frozenset(["Insomnia", "Fatigue", "Anxiety & Depression"]): 
            ("Sleep Disorder", {
                "precautions": [
                    "Maintain regular sleep schedule even on weekends",
                    "Limit caffeine intake, especially after 2 PM",
                    "Seek therapy or counseling if sleep problems persist",
                    "Create relaxing bedtime routine - warm bath, reading, meditation",
                    "Use bedroom only for sleep and intimacy (no work or screens)",
                    "Ensure comfortable sleep environment - dark, quiet, cool",
                    "Avoid heavy meals, alcohol, and vigorous exercise before bed",
                    "Get regular sunlight exposure during daytime hours",
                    "Limit naps to 20-30 minutes if needed during day",
                    "Practice stress-reduction techniques throughout day"
                ],
                "diet": [
                    "Eat tryptophan-rich foods like turkey, milk, and bananas at dinner",
                    "Include magnesium sources like almonds, spinach, and pumpkin seeds",
                    "Have complex carbohydrates with dinner to promote sleepiness",
                    "Avoid heavy, rich meals within 2-3 hours of bedtime",
                    "Drink herbal teas like chamomile or lavender before bed",
                    "Include tart cherry juice which contains natural melatonin",
                    "Eat warm milk with turmeric or honey before bedtime",
                    "Include foods rich in calcium like yogurt and leafy greens",
                    "Avoid spicy foods, chocolate, and caffeine in evenings",
                    "Eat light snack if hungry before bed - banana or small yogurt"
                ]
            }),
        
        frozenset(["Blurred Vision", "Numbness", "Fatigue"]): 
            ("Neuropathy", {
                "precautions": [
                    "Check blood sugar levels regularly if diabetic",
                    "Avoid alcohol consumption which can worsen nerve damage",
                    "Consult neurologist for proper diagnosis and treatment plan",
                    "Protect numb areas from injury - check feet daily",
                    "Take prescribed nerve pain medications as directed",
                    "Regular foot inspections for cuts, blisters, or injuries",
                    "Wear proper footwear and avoid walking barefoot",
                    "Avoid prolonged pressure on affected limbs",
                    "Manage underlying conditions like diabetes effectively",
                    "Get regular neurological examinations and follow-ups"
                ],
                "diet": [
                    "Eat B-vitamin rich foods - whole grains, eggs, leafy greens",
                    "Include alpha-lipoic acid sources like spinach, broccoli, potatoes",
                    "Consume omega-3 fatty acids for nerve health and inflammation",
                    "Eat antioxidant-rich fruits and vegetables for nerve protection",
                    "Limit sugar and refined carbohydrates to control blood sugar",
                    "Include magnesium-rich foods for nerve function",
                    "Eat vitamin E sources like nuts and seeds for nerve health",
                    "Stay well-hydrated with water and herbal teas",
                    "Include lean proteins for tissue repair and maintenance",
                    "Avoid processed foods and focus on whole, nutrient-dense foods"
                ]
            }),
        
        frozenset(["Fatigue", "Numbness", "Weight Loss"]): 
            ("Diabetes", {
                "precautions": [
                    "Check blood sugar regularly using glucose monitor",
                    "Take prescribed medications consistently as directed",
                    "Follow diabetic diet with controlled carbohydrate intake",
                    "Consult endocrinologist for comprehensive management",
                    "Daily foot care inspection for any cuts or sores",
                    "Regular eye examinations to monitor for retinopathy",
                    "Carry fast-acting sugar source for hypoglycemia episodes",
                    "Wear medical alert identification for emergencies",
                    "Exercise regularly as approved by healthcare provider",
                    "Attend regular medical check-ups and blood tests"
                ],
                "diet": [
                    "Follow balanced meals with controlled carbohydrate portions",
                    "Eat high fiber foods - vegetables, whole grains, legumes",
                    "Choose lean proteins with each meal - fish, chicken, tofu",
                    "Include healthy fats - avocados, nuts, olive oil",
                    "Limit sugary foods, desserts, and sweetened beverages",
                    "Eat regular meal timing to maintain stable blood sugar",
                    "Practice portion control to manage weight effectively",
                    "Choose non-starchy vegetables as main carbohydrate source",
                    "Include whole grains instead of refined grains",
                    "Stay well-hydrated with water and unsweetened beverages"
                ]
            }),

        # 🦴 JOINTS & MUSCLES
        frozenset(["Joint Pain", "Swelling", "Fatigue"]): 
            ("Arthritis", {
                "precautions": [
                    "Exercise lightly with low-impact activities like swimming or walking",
                    "Apply hot compress in morning for stiffness, cold for swelling after activity",
                    "Consult rheumatologist for proper diagnosis and treatment plan",
                    "Use assistive devices if needed for joint protection",
                    "Maintain healthy weight to reduce stress on joints",
                    "Practice proper posture and body mechanics",
                    "Take prescribed anti-inflammatory medications regularly",
                    "Get adequate rest balanced with gentle movement",
                    "Use joint protection techniques during daily activities",
                    "Consider physical therapy for customized exercise program"
                ],
                "diet": [
                    "Eat anti-inflammatory foods - fatty fish, berries, leafy greens",
                    "Include turmeric and ginger in cooking for natural anti-inflammatories",
                    "Consume omega-3 rich foods - walnuts, chia seeds, flaxseeds",
                    "Avoid nightshade vegetables if they worsen symptoms for you",
                    "Include calcium-rich foods for bone health - dairy, leafy greens",
                    "Eat vitamin D sources or get safe sun exposure",
                    "Include antioxidant-rich fruits and vegetables",
                    "Choose lean proteins for muscle support around joints",
                    "Eat whole grains for sustained energy and fiber",
                    "Stay hydrated with water and anti-inflammatory herbal teas"
                ]
            }),
        
        frozenset(["Joint Pain", "Fever", "Fatigue"]): 
            ("Rheumatic Fever", {
                "precautions": [
                    "Consult physician immediately for proper diagnosis and treatment",
                    "Take prescribed antibiotics completely as directed for strep infection",
                    "Get enough bed rest during acute phase of illness",
                    "Monitor heart symptoms and report any chest pain or palpitations",
                    "Follow-up with cardiologist if heart involvement suspected",
                    "Complete full course of antibiotics even if feeling better",
                    "Practice good oral hygiene to prevent future infections",
                    "Avoid strenuous physical activity during recovery period",
                    "Get regular medical monitoring during and after treatment",
                    "Seek prompt treatment for any future strep throat infections"
                ],
                "diet": [
                    "Eat anti-inflammatory foods to reduce joint inflammation",
                    "Include protein-rich foods for tissue repair and recovery",
                    "Consume vitamin C rich foods for immune support and healing",
                    "Stay well-hydrated with water, broths, and herbal teas",
                    "Include iron-rich foods if anemia develops - leafy greens, beans",
                    "Eat small, frequent meals if appetite is poor due to fever",
                    "Choose soft, easy-to-eat foods if throat is sore",
                    "Avoid processed foods and focus on whole, nutritious foods",
                    "Include zinc-rich foods for immune function support",
                    "Eat balanced meals with variety of fruits and vegetables"
                ]
            }),
            
            # 🦠 INFECTIONS & SYSTEMIC
                # 🦠 INFECTIONS & SYSTEMIC
        frozenset(["Fever", "Fatigue", "Sweating"]): 
            ("Malaria", {
                "precautions": [
                    "Consult doctor immediately for blood tests and diagnosis",
                    "Avoid mosquito bites using repellents and protective clothing",
                    "Take prescribed antimalarial medication completely as directed",
                    "Use mosquito nets while sleeping especially in endemic areas",
                    "Monitor body temperature regularly every 4-6 hours",
                    "Stay well hydrated with clean water and electrolyte solutions",
                    "Get complete bed rest during acute phase of illness",
                    "Follow-up with blood tests as recommended by doctor",
                    "Take medication at exact prescribed times for effectiveness",
                    "Seek emergency care if symptoms worsen or consciousness changes"
                ],
                "diet": [
                    "Eat high-protein foods for recovery - eggs, lentils, poultry, fish",
                    "Include iron-rich foods if anemia develops - leafy greens, beans, red meat",
                    "Consume small, frequent meals if nausea or appetite loss occurs",
                    "Avoid heavy, hard-to-digest foods during fever episodes",
                    "Drink oral rehydration solutions to maintain electrolyte balance",
                    "Include vitamin C rich fruits to enhance iron absorption",
                    "Eat easily digestible foods like khichdi, soups, and porridge",
                    "Stay hydrated with coconut water, herbal teas, and clear broths",
                    "Include zinc-rich foods for immune support - pumpkin seeds, chickpeas",
                    "Avoid alcohol and caffeine which can cause dehydration"
                ]
            }),
        
        frozenset(["Cough", "Fever", "Sweating"]): 
            ("Tuberculosis (TB)", {
                "precautions": [
                    "Consult pulmonologist for proper diagnosis and treatment plan",
                    "Regular medication adherence without missing any doses",
                    "Improve nutrition to support immune system and recovery",
                    "Complete full course of treatment (6-9 months) as prescribed",
                    "Practice respiratory hygiene - cover mouth when coughing",
                    "Ensure good ventilation in living and sleeping areas",
                    "Monitor for medication side effects and report to doctor",
                    "Get adequate rest and avoid overexertion during treatment",
                    "Attend all follow-up appointments and tests regularly",
                    "Isolate initially if advised to prevent spreading infection"
                ],
                "diet": [
                    "Eat high-calorie, high-protein diet for weight maintenance",
                    "Include B-vitamin rich foods - whole grains, eggs, lean meats",
                    "Consume iron-rich foods to prevent anemia - spinach, lentils, poultry",
                    "Include vitamin D and calcium sources for bone health",
                    "Eat small, frequent meals to maintain energy and weight",
                    "Avoid alcohol completely during TB treatment",
                    "Include zinc-rich foods for immune function - nuts, seeds, legumes",
                    "Eat antioxidant-rich fruits and vegetables daily",
                    "Stay hydrated with water, soups, and herbal teas",
                    "Include healthy fats for energy - nuts, olive oil, avocado"
                ]
            }),
        
        frozenset(["Fatigue", "Fever", "Weight Loss"]): 
            ("Chronic Infection", {
                "precautions": [
                    "Seek medical diagnosis for proper identification of infection",
                    "Eat balanced diet to support immune system function",
                    "Monitor body temperature regularly and keep record",
                    "Take prescribed antibiotics or antivirals completely",
                    "Get adequate rest and prioritize sleep for recovery",
                    "Follow medical advice strictly and complete treatment",
                    "Practice good hygiene to prevent additional infections",
                    "Manage stress through relaxation techniques",
                    "Avoid exposure to other ill people during recovery",
                    "Attend regular medical follow-ups for monitoring progress"
                ],
                "diet": [
                    "Eat balanced diet with adequate protein for immune support",
                    "Include immune-boosting foods - garlic, ginger, citrus fruits",
                    "Consume small, frequent meals if appetite is poor",
                    "Stay well hydrated with water, broths, and herbal teas",
                    "Avoid raw or undercooked foods during immune compromise",
                    "Include probiotic foods to support gut health - yogurt, kefir",
                    "Eat zinc-rich foods for immune function - seeds, nuts, legumes",
                    "Include vitamin C rich foods for antioxidant support",
                    "Choose easily digestible, nutrient-dense foods",
                    "Avoid processed foods and focus on whole, fresh foods"
                ]
            }),

        # ⚠️ MISCELLANEOUS
        frozenset(["Itching", "Swelling", "Numbness"]): 
            ("Insect Bite or Allergy", {
                "precautions": [
                    "Apply ice pack wrapped in cloth to reduce swelling and itching",
                    "Take oral antihistamine like cetirizine or loratadine as directed",
                    "Avoid scratching area to prevent infection and further irritation",
                    "Clean affected area with soap and water to prevent infection",
                    "Use calamine lotion or hydrocortisone cream for itching relief",
                    "Elevate affected limb if swelling occurs to reduce inflammation",
                    "Monitor for signs of severe allergic reaction - difficulty breathing",
                    "Use insect repellent when outdoors to prevent future bites",
                    "Wear protective clothing in insect-prone areas",
                    "Seek medical help if swelling spreads or breathing difficulties occur"
                ],
                "diet": [
                    "Eat anti-inflammatory foods to reduce swelling - berries, leafy greens",
                    "Include foods rich in vitamin C to support healing - citrus fruits",
                    "Stay well hydrated to help flush out toxins and reduce swelling",
                    "Avoid known food allergens if you have allergic tendencies",
                    "Include quercetin-rich foods - apples, onions, capers, berries",
                    "Eat omega-3 rich foods to reduce inflammation - fish, walnuts",
                    "Include probiotic foods to support immune system balance",
                    "Drink herbal teas like chamomile or peppermint for soothing effect",
                    "Eat fresh fruits and vegetables for antioxidant support",
                    "Avoid processed foods that may contain hidden allergens"
                ]
            }),
        
        frozenset(["Fatigue", "Sweating", "Nausea"]): 
            ("Heat Exhaustion", {
                "precautions": [
                    "Move to cool, shaded, or air-conditioned place immediately",
                    "Drink water and electrolyte solutions to rehydrate",
                    "Rest completely and avoid sun exposure until recovered",
                    "Lie down with legs elevated to improve blood circulation",
                    "Remove excess clothing and loosen tight garments",
                    "Use cool wet cloths or take cool shower to lower body temperature",
                    "Avoid strenuous activity for at least 24 hours after recovery",
                    "Monitor for signs of heat stroke - confusion, high temperature",
                    "Wear light-colored, loose-fitting clothing in heat",
                    "Take frequent breaks in shade when working in hot conditions"
                ],
                "diet": [
                    "Drink electrolyte-rich fluids - ORS, sports drinks, coconut water",
                    "Eat water-rich fruits and vegetables - watermelon, cucumber, oranges",
                    "Include potassium-rich foods - bananas, potatoes, spinach",
                    "Consume magnesium-rich foods - almonds, spinach, avocado",
                    "Avoid spicy foods and hot temperature meals",
                    "Eat light, easily digestible meals to prevent nausea",
                    "Include small, frequent sips of cool liquids",
                    "Avoid caffeine and alcohol which can cause dehydration",
                    "Eat small, frequent meals rather than large heavy meals",
                    "Include mint and cooling herbs in diet for nausea relief"
                ]
            }),
        
        # Single symptom entries
        frozenset(["Itching"]): ("Possible Fungal Infection", {
            "precautions": [
                "Monitor symptoms for progression or spreading",
                "Keep area dry and clean to prevent worsening",
                "Avoid scratching to prevent skin damage and infection",
                "Use mild, fragrance-free soap for cleaning",
                "Wear loose, breathable clothing",
                "Apply soothing lotion like calamine if needed",
                "Observe for development of rash or other symptoms",
                "Consult doctor if itching persists beyond 2-3 days",
                "Avoid potential irritants and allergens",
                "Maintain good personal hygiene"
            ],
            "diet": [
                "Stay well hydrated with water and herbal teas",
                "Include probiotic foods for immune support",
                "Eat anti-inflammatory foods - berries, leafy greens",
                "Avoid excessive sugar and processed foods",
                "Include zinc-rich foods for skin health",
                "Eat foods rich in omega-3 fatty acids",
                "Include vitamin C rich fruits and vegetables",
                "Avoid known food allergens if prone to allergies",
                "Eat balanced meals with variety of nutrients",
                "Include turmeric and ginger in cooking"
            ]
        }),
        
        frozenset(["Skin Rash"]): ("Possible Fungal Infection", {
            "precautions": [
                "Use antifungal cream if rash persists or spreads",
                "Keep affected area clean and dry",
                "Avoid tight clothing that rubs against rash",
                "Use mild, hypoallergenic soap for cleaning",
                "Apply cool compresses for itching relief",
                "Monitor rash for changes in size or appearance",
                "Avoid sharing towels or personal items",
                "Wear breathable cotton clothing",
                "Consult dermatologist if rash worsens",
                "Identify and avoid potential triggers"
            ],
            "diet": [
                "Reduce sugar and refined carbohydrate intake",
                "Include probiotic foods - yogurt, kefir, fermented foods",
                "Eat garlic and onions for natural antifungal properties",
                "Include coconut oil in cooking",
                "Consume vitamin C rich foods for skin healing",
                "Add turmeric to meals for anti-inflammatory benefits",
                "Stay hydrated with plenty of water",
                "Avoid alcohol and processed foods",
                "Eat zinc-rich foods - pumpkin seeds, lentils",
                "Include omega-3 foods - fatty fish, walnuts"
            ]
        }),
        
        frozenset(["Nodal Skin Eruptions"]): ("Possible Fungal Infection", {
            "precautions": [
                "Consult dermatologist if condition worsens",
                "Keep area clean and dry",
                "Avoid squeezing or scratching eruptions",
                "Use prescribed topical treatments as directed",
                "Monitor for signs of infection - redness, pus",
                "Maintain good personal hygiene",
                "Avoid sharing personal care items",
                "Wear loose, breathable clothing",
                "Follow medical advice for treatment",
                "Keep track of any new symptoms"
            ],
            "diet": [
                "Include probiotic-rich foods for immune support",
                "Reduce intake of sugary and processed foods",
                "Eat foods with natural antifungal properties",
                "Include vitamin A rich foods for skin health",
                "Consume zinc-rich foods for healing",
                "Stay well hydrated with water",
                "Include antioxidant-rich fruits and vegetables",
                "Avoid dairy if it seems to worsen condition",
                "Eat balanced meals with variety of nutrients",
                "Include healthy fats for skin nourishment"
            ]
        }),
        
        frozenset(["Itching", "Skin Rash"]): ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream as directed on package",
                "Keep area dry and avoid moisture buildup",
                "Avoid tight clothes that cause friction",
                "Change clothes daily and after sweating",
                "Use separate towels for affected areas",
                "Wash clothes in hot water to kill fungi",
                "Avoid scratching to prevent spreading",
                "Apply powder to keep area dry if needed",
                "Complete full treatment course",
                "Consult doctor if no improvement in 1 week"
            ],
            "diet": [
                "Reduce sugar and refined carbs intake",
                "Increase probiotic foods - yogurt, kefir",
                "Eat garlic for natural antifungal properties",
                "Include coconut oil in diet",
                "Consume vitamin C rich foods",
                "Add turmeric to meals",
                "Stay hydrated with water",
                "Avoid alcohol and fermented foods",
                "Eat zinc-rich foods",
                "Include omega-3 foods"
            ]
        }),
        
        frozenset(["Itching", "Nodal Skin Eruptions"]): ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream twice daily",
                "Keep area dry and clean",
                "Avoid tight clothing",
                "Monitor symptoms for improvement",
                "Don't squeeze or puncture eruptions",
                "Maintain good hygiene practices",
                "Change bedding regularly",
                "Use antifungal powder if needed",
                "Complete treatment course",
                "Seek medical help if worsens"
            ],
            "diet": [
                "Reduce sugar intake significantly",
                "Include probiotic foods daily",
                "Eat natural antifungal foods",
                "Stay well hydrated",
                "Include zinc-rich foods",
                "Eat vitamin-rich fruits",
                "Avoid processed foods",
                "Include healthy fats",
                "Eat antioxidant foods",
                "Maintain balanced nutrition"
            ]
        }),
        
        frozenset(["Skin Rash", "Nodal Skin Eruptions"]): ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream as directed",
                "Keep area dry and clean",
                "Avoid tight clothes",
                "Consult dermatologist if persistent",
                "Don't scratch or irritate area",
                "Use mild soap for cleaning",
                "Wear breathable fabrics",
                "Maintain personal hygiene",
                "Complete treatment fully",
                "Monitor for improvement"
            ],
            "diet": [
                "Reduce sugar and refined carbs",
                "Include probiotic foods",
                "Eat antifungal natural foods",
                "Stay hydrated",
                "Include healing nutrients",
                "Avoid inflammatory foods",
                "Eat balanced meals",
                "Include vitamin C foods",
                "Consume zinc sources",
                "Maintain healthy diet"
            ]
        }),
        # 🟢 EXPANDED DICTIONARY WITH ALL MISSING COMBINATIONS

        # 🩹 SKIN & ALLERGY CONDITIONS (Already partially included)
            frozenset(["Itching", "Skin Rash", "Nodal Skin Eruptions"]): 
        ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream (clotrimazole, miconazole) 2-3 times daily",
                "Keep area dry and clean - pat dry after bathing",
                "Avoid tight clothes that trap moisture",
                "Wear breathable cotton clothing",
                "Change clothes and underwear daily",
                "Use separate towels for affected areas",
                "Avoid scratching to prevent spreading",
                "Wash clothes in hot water",
                "Apply antifungal powder in skin folds",
                "Complete full treatment course"
            ],
            "diet": [
                "Reduce sugar and refined carbohydrates",
                "Increase probiotic foods (yogurt, kefir)",
                "Eat garlic and onions for antifungal properties",
                "Include coconut oil in cooking",
                "Consume vitamin C rich foods",
                "Add turmeric to meals",
                "Stay hydrated with water",
                "Avoid alcohol and fermented foods",
                "Eat zinc-rich foods (pumpkin seeds, lentils)",
                "Include omega-3 foods (fatty fish, walnuts)"
            ]
        }),
    
    frozenset(["Itching", "Skin Rash", "Continuous Sneezing"]): 
        ("Allergic Reaction", {
            "precautions": [
                "Avoid allergens (pollen, dust, pet dander)",
                "Use antihistamines (cetirizine, loratadine)",
                "Consult dermatologist if symptoms persist",
                "Use air purifiers with HEPA filters",
                "Keep windows closed during high pollen",
                "Wash bedding weekly in hot water",
                "Shower after outdoor exposure",
                "Use hypoallergenic bedding covers",
                "Avoid outdoor activities during high pollen",
                "Keep emergency medication if severe allergies"
            ],
            "diet": [
                "Include local honey for pollen immunity",
                "Eat quercetin-rich foods (apples, onions, berries)",
                "Increase omega-3 fatty acids (salmon, flaxseeds)",
                "Consume vitamin C rich foods",
                "Add probiotic foods to diet",
                "Include bromelain from pineapple",
                "Eat magnesium-rich foods (spinach, almonds)",
                "Avoid common food allergens",
                "Stay well hydrated with herbal teas",
                "Include turmeric and ginger in meals"
            ]
        }),
    
    frozenset(["Itching", "Skin Rash", "Swelling"]): 
        ("Skin Allergy", {
            "precautions": [
                "Apply calamine lotion or hydrocortisone cream",
                "Avoid scratching affected areas",
                "Use mild soap and moisturizer regularly",
                "Take cool oatmeal baths for relief",
                "Use cold compresses to reduce swelling",
                "Wear loose, cotton clothing",
                "Identify and avoid trigger substances",
                "Keep nails short and clean",
                "Apply aloe vera gel for cooling relief",
                "Consult doctor for severe reactions"
            ],
            "diet": [
                "Eat anti-inflammatory foods (berries, leafy greens)",
                "Include omega-3 rich foods",
                "Consume zinc-rich foods for skin healing",
                "Add vitamin E foods (nuts, seeds)",
                "Include quercetin sources",
                "Eat probiotic foods",
                "Avoid processed and packaged foods",
                "Stay hydrated with water and coconut water",
                "Include turmeric in cooking",
                "Eat vitamin A rich foods (sweet potatoes, carrots)"
            ]
        }),
    
    frozenset(["Itching", "Fatigue", "Sweating"]): 
        ("Heat Rash", {
            "precautions": [
                "Stay cool in air-conditioned environments",
                "Wear loose cotton clothes for breathability",
                "Apply soothing powder (cornstarch-based)",
                "Take cool showers frequently",
                "Use calamine lotion for itching relief",
                "Avoid heavy creams that block pores",
                "Keep skin dry and clean",
                "Use fans for air circulation",
                "Avoid strenuous exercise in heat",
                "Stay hydrated with electrolytes"
            ],
            "diet": [
                "Drink plenty of water and electrolyte fluids",
                "Eat water-rich fruits (watermelon, cucumber)",
                "Include potassium-rich foods (bananas, potatoes)",
                "Consume magnesium foods (spinach, almonds)",
                "Avoid spicy and hot temperature foods",
                "Eat light, easily digestible meals",
                "Include coconut water for hydration",
                "Avoid caffeine and alcohol",
                "Eat small, frequent meals",
                "Include mint and cooling herbs in diet"
            ]
        }),

        # Single symptoms for skin & allergy
            frozenset(["Itching"]): ("Possible Allergy/Fungal Infection", {
        "precautions": [
            "Monitor symptoms for progression or spreading",
            "Keep area dry and clean",
            "Avoid scratching to prevent infection",
            "Use mild, fragrance-free soap",
            "Apply soothing lotion like calamine",
            "Wear loose, breathable clothing",
            "Observe for development of rash",
            "Consult doctor if persists beyond 2-3 days",
            "Avoid potential irritants",
            "Maintain good personal hygiene"
        ],
        "diet": [
            "Stay well hydrated with water",
            "Include probiotic foods (yogurt, kefir)",
            "Eat anti-inflammatory foods",
            "Avoid excessive sugar and processed foods",
            "Include zinc-rich foods",
            "Eat omega-3 rich foods",
            "Consume vitamin C rich fruits",
            "Avoid known food allergens",
            "Include turmeric and ginger",
            "Eat balanced, nutritious meals"
        ]
        }),
        
        frozenset(["Skin Rash"]): ("Possible Skin Condition", {
            "precautions": [
                "Use antifungal or hydrocortisone cream if persists",
                "Consult dermatologist for proper diagnosis",
                "Keep affected area clean and dry",
                "Avoid tight clothing",
                "Use mild, hypoallergenic soap",
                "Apply cool compresses for relief",
                "Monitor for changes in rash",
                "Avoid scratching",
                "Wear breathable fabrics",
                "Identify potential triggers"
            ],
            "diet": [
                "Reduce sugar and refined carbs",
                "Include probiotic foods",
                "Eat garlic and onions",
                "Include coconut oil",
                "Consume vitamin C rich foods",
                "Add turmeric to meals",
                "Stay hydrated",
                "Avoid alcohol",
                "Eat zinc-rich foods",
                "Include omega-3 foods"
            ]
        }),
        
        frozenset(["Nodal Skin Eruptions"]): ("Possible Skin Condition", {
            "precautions": [
                "Consult dermatologist for proper diagnosis",
                "Keep area clean and dry",
                "Avoid squeezing or scratching",
                "Use prescribed treatments as directed",
                "Monitor for signs of infection",
                "Maintain good hygiene",
                "Avoid sharing personal items",
                "Wear loose clothing",
                "Follow medical advice",
                "Track any new symptoms"
            ],
            "diet": [
                "Include probiotic-rich foods",
                "Reduce sugary foods",
                "Eat natural antifungal foods",
                "Include vitamin A rich foods",
                "Consume zinc-rich foods",
                "Stay well hydrated",
                "Eat antioxidant-rich fruits",
                "Avoid dairy if problematic",
                "Include healthy fats",
                "Eat balanced meals"
            ]
        }),
        
        frozenset(["Swelling"]): ("Monitor Swelling", {
            "precautions": [
                "Apply ice pack if swelling is recent",
                "Use calamine lotion if itching present",
                "Elevate affected area if possible",
                "Monitor for increase in swelling",
                "Keep area clean and dry",
                "Avoid tight clothing",
                "Apply cold compresses",
                "Rest the affected area",
                "Seek medical help if severe",
                "Identify possible causes"
            ],
            "diet": [
                "Eat anti-inflammatory foods",
                "Include potassium-rich foods",
                "Consume magnesium foods",
                "Stay well hydrated",
                "Avoid salty foods",
                "Eat vitamin C rich foods",
                "Include pineapple (bromelain)",
                "Eat ginger and turmeric",
                "Avoid processed foods",
                "Eat balanced meals"
            ]
        }),
        
        frozenset(["Continuous Sneezing"]): ("Possible Allergy", {
            "precautions": [
                "Avoid known allergens",
                "Use air purifiers if indoors",
                "Keep windows closed during high pollen",
                "Wash face and hands after going outside",
                "Use saline nasal spray",
                "Change clothes after outdoor activities",
                "Avoid strong fragrances",
                "Use antihistamines if needed",
                "Consult doctor if persistent",
                "Monitor for other allergy symptoms"
            ],
            "diet": [
                "Include local honey",
                "Eat quercetin-rich foods",
                "Increase omega-3 fatty acids",
                "Consume vitamin C rich foods",
                "Add probiotic foods",
                "Include bromelain sources",
                "Eat magnesium-rich foods",
                "Avoid common allergens",
                "Stay hydrated with herbal teas",
                "Include anti-inflammatory foods"
            ]
        }),

            # 2-symptom pairs for skin & allergy
        frozenset(["Itching", "Skin Rash"]): ("Fungal Infection / Allergy", {
            "precautions": [
                "Use antifungal cream or antihistamines based on symptoms",
                "Keep affected area clean and dry",
                "Avoid scratching to prevent infection",
                "Wear loose, breathable clothing",
                "Monitor symptoms for improvement",
                "Use mild, fragrance-free soap",
                "Apply soothing lotions as needed",
                "Identify and avoid potential triggers",
                "Consult doctor if no improvement",
                "Maintain good personal hygiene"
            ],
            "diet": [
                "Reduce sugar and processed foods",
                "Include probiotic foods (yogurt, kefir)",
                "Eat anti-inflammatory foods",
                "Stay well hydrated with water",
                "Include zinc-rich foods",
                "Eat omega-3 rich foods",
                "Consume vitamin C rich fruits",
                "Avoid known allergens",
                "Include turmeric and ginger",
                "Eat balanced, nutritious meals"
                ]
        }),
        
        frozenset(["Itching", "Nodal Skin Eruptions"]): ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream twice daily",
                "Monitor symptoms for changes",
                "Keep area dry and clean",
                "Avoid tight clothing",
                "Don't squeeze or puncture eruptions",
                "Maintain good hygiene",
                "Change bedding regularly",
                "Use antifungal powder if needed",
                "Complete treatment course",
                "Consult doctor if worsens"
            ],
            "diet": [
                "Reduce sugar intake significantly",
                "Include probiotic foods daily",
                "Eat natural antifungal foods",
                "Stay well hydrated",
                "Include zinc-rich foods",
                "Eat vitamin-rich fruits",
                "Avoid processed foods",
                "Include healthy fats",
                "Eat antioxidant foods",
                "Maintain balanced nutrition"
            ]
        }),
        
        frozenset(["Skin Rash", "Nodal Skin Eruptions"]): ("Fungal Infection", {
            "precautions": [
                "Use antifungal cream as directed",
                "Consult dermatologist for proper diagnosis",
                "Keep area dry and clean",
                "Avoid tight clothes",
                "Don't scratch or irritate area",
                "Use mild soap for cleaning",
                "Wear breathable fabrics",
                "Maintain personal hygiene",
                "Complete treatment fully",
                "Monitor for improvement"
            ],
            "diet": [
                "Reduce sugar and refined carbs",
                "Include probiotic foods",
                "Eat antifungal natural foods",
                "Stay hydrated",
                "Include healing nutrients",
                "Avoid inflammatory foods",
                "Eat balanced meals",
                "Include vitamin C foods",
                "Consume zinc sources",
                "Maintain healthy diet"
            ]
        }),
        
        frozenset(["Itching", "Swelling"]): ("Skin Allergy", {
            "precautions": [
                "Apply calamine lotion for relief",
                "Avoid scratching affected areas",
                "Use cold compresses on swelling",
                "Take oral antihistamines if needed",
                "Keep area clean and dry",
                "Wear loose clothing",
                "Identify allergy triggers",
                "Use mild, hypoallergenic products",
                "Monitor for severe reactions",
                "Consult doctor if persistent"
            ],
            "diet": [
                "Eat anti-inflammatory foods",
                "Include omega-3 rich foods",
                "Consume quercetin sources",
                "Stay well hydrated",
                "Avoid common allergens",
                "Include probiotic foods",
                "Eat vitamin C rich foods",
                "Include zinc-rich foods",
                "Avoid processed foods",
                "Eat balanced meals"
            ]
        }),
        
        frozenset(["Skin Rash", "Swelling"]): ("Skin Allergy", {
            "precautions": [
                "Apply calamine lotion regularly",
                "Use mild soap for cleaning",
                "Avoid scratching the rash",
                "Use cold compresses for swelling",
                "Wear loose, cotton clothing",
                "Take antihistamines as needed",
                "Keep area clean and dry",
                "Identify potential allergens",
                "Monitor for infection signs",
                "Consult dermatologist if severe"
            ],
            "diet": [
                "Eat anti-inflammatory foods",
                "Include omega-3 fatty acids",
                "Consume zinc-rich foods",
                "Add vitamin E foods",
                "Include quercetin sources",
                "Eat probiotic foods",
                "Avoid processed foods",
                "Stay hydrated",
                "Include turmeric in cooking",
                "Eat vitamin A rich foods"
            ]
        }),
        
        frozenset(["Itching", "Continuous Sneezing"]): ("Allergic Reaction", {
            "precautions": [
                "Avoid allergens and irritants",
                "Use antihistamines as directed",
                "Keep windows closed during high pollen",
                "Use air purifiers indoors",
                "Shower after outdoor exposure",
                "Wash bedding regularly",
                "Use saline nasal spray",
                "Wear mask if needed outdoors",
                "Monitor for worsening symptoms",
                "Consult doctor if persistent"
            ],
            "diet": [
                "Include local honey",
                "Eat quercetin-rich foods",
                "Increase omega-3 fatty acids",
                "Consume vitamin C rich foods",
                "Add probiotic foods",
                "Include bromelain sources",
                "Eat magnesium-rich foods",
                "Avoid common food allergens",
                "Stay hydrated with herbal teas",
                "Include anti-inflammatory foods"
            ]
        }),
        
        frozenset(["Skin Rash", "Continuous Sneezing"]): ("Allergic Reaction", {
            "precautions": [
                "Use antihistamines for symptom relief",
                "Avoid allergens and triggers",
                "Apply soothing creams to rash",
                "Use air purifiers at home",
                "Keep indoor environment clean",
                "Wash hands and face frequently",
                "Change clothes after being outdoors",
                "Use hypoallergenic products",
                "Monitor for severe reactions",
                "Consult allergist if needed"
            ],
            "diet": [
                "Include local honey daily",
                "Eat quercetin-rich foods",
                "Increase omega-3 intake",
                "Consume vitamin C foods",
                "Add probiotic foods",
                "Include anti-inflammatory foods",
                "Eat magnesium-rich foods",
                "Avoid potential food allergens",
                "Stay well hydrated",
                "Include turmeric and ginger"
            ]
        }),

            # 😷 RESPIRATORY INFECTIONS
        frozenset(["Continuous Sneezing", "Cough", "Shivering"]): ("Common Cold", {
            "precautions": [
                "Drink warm fluids like herbal tea and soup regularly",
                "Take steam inhalation with eucalyptus oil 2-3 times daily",
                "Get plenty of rest and adequate sleep",
                "Use saline nasal drops for congestion relief",
                "Gargle with warm salt water for sore throat",
                "Take vitamin C and zinc supplements",
                "Use humidifier to moisten air in room",
                "Wash hands frequently to prevent spread",
                "Avoid close contact with others",
                "Use disposable tissues when sneezing"
            ],
            "diet": [
                "Drink warm chicken soup or vegetable broth",
                "Consume ginger tea with honey and lemon",
                "Eat vitamin C rich foods (oranges, kiwi, bell peppers)",
                "Include garlic in meals for immunity",
                "Stay hydrated with warm water",
                "Eat zinc-rich foods (pumpkin seeds, lentils)",
                "Consume probiotic foods (yogurt, kefir)",
                "Avoid dairy if it increases mucus",
                "Eat light, easily digestible meals",
                "Include turmeric in warm milk"
            ]
        }),
        
        frozenset(["Cough", "Fever", "Fatigue"]): ("Viral Infection", {
            "precautions": [
                "Stay hydrated with water and electrolyte drinks",
                "Take complete rest and avoid physical exertion",
                "Use paracetamol for fever and body aches if needed",
                "Monitor temperature regularly",
                "Use cough suppressants or expectorants",
                "Take warm steam inhalation",
                "Get adequate sleep for recovery",
                "Isolate to prevent spreading infection",
                "Use humidifier in room",
                "Consult doctor if fever persists"
            ],
            "diet": [
                "Drink plenty of fluids and herbal teas",
                "Eat protein-rich foods (eggs, chicken, lentils)",
                "Consume vitamin C rich fruits",
                "Include ginger and garlic in meals",
                "Eat small, frequent meals",
                "Avoid heavy, greasy foods",
                "Drink warm water with honey and lemon",
                "Include zinc-rich foods",
                "Eat probiotic foods for gut health",
                "Consume bone broth for nutrients"
            ]
        }),
        
        frozenset(["Cough", "Chest Pain", "Fever"]): ("Pneumonia", {
            "precautions": [
                "Consult physician immediately for diagnosis",
                "Take prescribed antibiotics completely as directed",
                "Monitor breathing patterns and oxygen levels",
                "Use incentive spirometer for lung exercise",
                "Get plenty of bed rest",
                "Stay hydrated with warm fluids",
                "Use steam inhalation regularly",
                "Practice deep breathing exercises",
                "Avoid smoking and pollutants",
                "Seek emergency care if breathing worsens"
            ],
            "diet": [
                "Eat high-protein foods for tissue repair",
                "Consume vitamin A rich foods (carrots, sweet potatoes)",
                "Include vitamin C sources",
                "Eat small, frequent meals",
                "Stay hydrated with warm broths",
                "Include zinc-rich foods",
                "Avoid dairy if it thickens mucus",
                "Eat antioxidant-rich fruits",
                "Include garlic and onions in diet",
                "Consume omega-3 foods for inflammation"
            ]
        }),
        
        frozenset(["Cough", "Shortness of Breath", "Fatigue"]): ("Bronchitis", {
            "precautions": [
                "Avoid smoking and secondhand smoke completely",
                "Take steam inhalation 2-3 times daily",
                "Stay hydrated with plenty of fluids",
                "Use prescribed bronchodilators properly",
                "Get adequate rest for recovery",
                "Avoid cold air and pollutants",
                "Practice breathing exercises",
                "Use cough expectorants as needed",
                "Use humidifier in bedroom",
                "Wear mask in polluted areas"
            ],
            "diet": [
                "Drink warm herbal teas with honey",
                "Eat anti-inflammatory foods",
                "Include ginger and turmeric in meals",
                "Consume vitamin C rich foods",
                "Stay hydrated with warm water",
                "Eat garlic for antimicrobial properties",
                "Include omega-3 rich foods",
                "Avoid cold drinks and ice cream",
                "Eat light, nutritious meals",
                "Consume chicken soup regularly"
            ]
        }),
        
        frozenset(["Shortness of Breath", "Cough", "Fatigue"]): ("Asthma", {
            "precautions": [
                "Use inhaler as prescribed by doctor",
                "Avoid allergens and known triggers",
                "Monitor breathing patterns regularly",
                "Keep rescue medication accessible",
                "Create asthma action plan with doctor",
                "Use air purifiers at home",
                "Avoid strenuous exercise in cold",
                "Practice breathing techniques",
                "Regular medical check-ups",
                "Avoid smoking and strong odors"
            ],
            "diet": [
                "Eat omega-3 rich foods (salmon, walnuts)",
                "Include magnesium foods (spinach, almonds)",
                "Consume vitamin C rich fruits",
                "Eat antioxidant-rich berries",
                "Include ginger and turmeric",
                "Avoid sulfite-containing foods",
                "Stay well hydrated",
                "Eat small, frequent meals",
                "Include probiotic foods",
                "Consume apples and onions regularly"
            ]
        }),

            # Single symptoms for respiratory
        frozenset(["Continuous Sneezing"]): ("Possible Cold/Allergy", {
            "precautions": [
                "Avoid allergens like pollen, dust, and pet dander",
                "Get adequate rest to support immune system",
                "Use saline nasal spray to clear nasal passages",
                "Keep windows closed during high pollen seasons",
                "Wash hands and face after outdoor exposure",
                "Use air purifiers with HEPA filters indoors",
                "Take antihistamines if allergy is suspected",
                "Monitor for other symptoms developing",
                "Avoid strong fragrances and irritants",
                "Consult doctor if sneezing persists beyond 3 days"
            ],
            "diet": [
                "Drink warm herbal teas with honey",
                "Include local honey for pollen immunity",
                "Eat quercetin-rich foods (apples, onions, berries)",
                "Consume vitamin C rich fruits and vegetables",
                "Stay well hydrated with warm water",
                "Include probiotic foods for immune support",
                "Eat anti-inflammatory foods like turmeric and ginger",
                "Avoid dairy if it increases mucus production",
                "Include omega-3 rich foods",
                "Eat light, easily digestible meals"
            ]
        }),
        
        frozenset(["Cough"]): ("Monitor Cough", {
            "precautions": [
                "Stay hydrated with warm fluids throughout the day",
                "Consult physician if cough persists beyond one week",
                "Use honey and lemon for soothing relief",
                "Take steam inhalation to loosen mucus",
                "Avoid smoking and secondhand smoke",
                "Use humidifier to keep air moist",
                "Rest your voice and avoid shouting",
                "Monitor for fever or breathing difficulties",
                "Practice good hand hygiene",
                "Use cough drops or lozenges as needed"
            ],
            "diet": [
                "Drink warm water with honey and lemon",
                "Consume ginger tea for its anti-inflammatory properties",
                "Eat vitamin C rich foods to support immunity",
                "Include garlic in meals for antimicrobial benefits",
                "Stay hydrated with soups and broths",
                "Avoid cold drinks and ice cream",
                "Eat light, nutritious meals",
                "Include zinc-rich foods for immune support",
                "Consume probiotic foods",
                "Avoid spicy and oily foods"
            ]
        }),
        
        frozenset(["Fever"]): ("Monitor Fever", {
            "precautions": [
                "Stay hydrated with water and electrolyte drinks",
                "Get plenty of rest to help body fight infection",
                "Monitor temperature every 4-6 hours",
                "Use paracetamol if fever is above 101°F",
                "Take lukewarm sponge baths for comfort",
                "Wear light, breathable clothing",
                "Keep room temperature comfortable",
                "Seek medical help if fever persists beyond 3 days",
                "Watch for other symptoms developing",
                "Maintain good personal hygiene"
            ],
            "diet": [
                "Drink plenty of fluids including water and herbal teas",
                "Consume electrolyte-rich drinks and coconut water",
                "Eat light, easily digestible foods",
                "Include vitamin C rich fruits",
                "Stay hydrated with clear soups and broths",
                "Avoid heavy, greasy, or spicy foods",
                "Eat small, frequent meals",
                "Include probiotic foods",
                "Consume foods with natural anti-inflammatory properties",
                "Avoid caffeine and alcohol"
            ]
        }),
        
        frozenset(["Fatigue"]): ("Monitor Fatigue", {
            "precautions": [
                "Rest adequately and prioritize sleep",
                "Stay hydrated with water and healthy fluids",
                "Practice stress management techniques",
                "Maintain regular sleep schedule",
                "Avoid overexertion and pace activities",
                "Monitor for other symptoms developing",
                "Get moderate exercise if energy permits",
                "Take short naps during the day if needed",
                "Consult doctor if fatigue persists beyond 2 weeks",
                "Check for nutritional deficiencies"
            ],
            "diet": [
                "Stay well hydrated with water and herbal teas",
                "Eat iron-rich foods (leafy greens, lentils, lean meat)",
                "Include complex carbohydrates for sustained energy",
                "Consume protein-rich foods with each meal",
                "Eat small, frequent meals to maintain energy",
                "Include B-vitamin rich foods (whole grains, eggs)",
                "Stay hydrated with electrolyte drinks if needed",
                "Avoid excessive caffeine and sugar",
                "Include magnesium-rich foods (nuts, seeds, leafy greens)",
                "Eat balanced, nutrient-dense meals"
            ]
        }),
        
        frozenset(["Chest Pain"]): ("Consult physician", {
            "precautions": [
                "Monitor severity and characteristics of pain",
                "Seek immediate medical attention for severe pain",
                "Keep track of when pain occurs and what triggers it",
                "Avoid strenuous physical activity",
                "Rest in comfortable position",
                "Monitor for accompanying symptoms",
                "Keep emergency contacts readily available",
                "Do not ignore persistent chest pain",
                "Follow up with healthcare provider",
                "Learn to recognize emergency warning signs"
            ],
            "diet": [
                "Eat small, frequent meals instead of large ones",
                "Avoid spicy, greasy, and heavy foods",
                "Stay hydrated with water between meals",
                "Include anti-inflammatory foods",
                "Avoid caffeine and alcohol",
                "Eat fiber-rich foods for digestive health",
                "Include heart-healthy fats in moderation",
                "Avoid eating right before bedtime",
                "Consume balanced, nutritious meals",
                "Stay away from trigger foods that cause discomfort"
            ]
        }),
        
        frozenset(["Shortness of Breath"]): ("Monitor Breathing", {
            "precautions": [
                "Seek medical help immediately if severe or worsening",
                "Rest in comfortable, upright position",
                "Practice deep breathing exercises",
                "Monitor breathing patterns and rate",
                "Avoid triggers like smoke and strong odors",
                "Keep emergency inhaler accessible if prescribed",
                "Stay in well-ventilated areas",
                "Avoid strenuous activities",
                "Monitor for other concerning symptoms",
                "Keep emergency numbers handy"
            ],
            "diet": [
                "Eat small, frequent meals to avoid pressure on diaphragm",
                "Stay well hydrated with room temperature water",
                "Include magnesium-rich foods (spinach, almonds, avocado)",
                "Consume omega-3 rich foods for anti-inflammatory benefits",
                "Avoid heavy meals and carbonated drinks",
                "Include antioxidant-rich fruits and vegetables",
                "Eat foods rich in B vitamins for energy",
                "Avoid foods that cause bloating or gas",
                "Stay hydrated with herbal teas",
                "Eat balanced, easily digestible meals"
            ]
        }),
        
        frozenset(["Shivering"]): ("Possible Cold/Infection", {
            "precautions": [
                "Rest and keep warm with blankets",
                "Monitor body temperature regularly",
                "Drink warm fluids to raise body temperature",
                "Take warm baths or use heating pads",
                "Wear warm, layered clothing",
                "Monitor for fever development",
                "Get adequate sleep and rest",
                "Avoid cold environments",
                "Watch for other symptoms appearing",
                "Consult doctor if shivering persists or fever develops"
            ],
            "diet": [
                "Drink warm herbal teas and soups",
                "Consume ginger and turmeric for warming properties",
                "Eat warm, cooked meals instead of cold foods",
                "Include protein-rich foods for energy",
                "Stay hydrated with warm fluids",
                "Include complex carbohydrates for sustained warmth",
                "Eat small, frequent warm meals",
                "Avoid cold drinks and raw foods",
                "Include spices like cinnamon and black pepper",
                "Consume nutrient-dense warm foods"
            ]
        }),

            # 2-symptom pairs for respiratory
        frozenset(["Continuous Sneezing", "Cough"]): ("Possible Cold", {
            "precautions": [
                "Get plenty of rest to support immune system",
                "Stay hydrated with warm fluids throughout the day",
                "Use saline nasal spray for nasal congestion",
                "Take steam inhalation to relieve respiratory symptoms",
                "Gargle with warm salt water for throat irritation",
                "Use honey and lemon for cough relief",
                "Avoid close contact with others to prevent spread",
                "Wash hands frequently with soap and water",
                "Use humidifier to keep air moist",
                "Monitor for fever or worsening symptoms"
            ],
            "diet": [
                "Drink warm herbal teas with honey and lemon",
                "Consume warm chicken soup or vegetable broth",
                "Eat vitamin C rich fruits like oranges and kiwi",
                "Include ginger and garlic in meals for immunity",
                "Stay hydrated with warm water and clear fluids",
                "Eat zinc-rich foods like pumpkin seeds and lentils",
                "Avoid dairy if it increases mucus production",
                "Consume probiotic foods for gut health",
                "Eat light, easily digestible meals",
                "Include turmeric in warm milk or teas"
            ]
        }),
        
        frozenset(["Continuous Sneezing", "Shivering"]): ("Possible Cold", {
            "precautions": [
                "Rest in warm, comfortable environment",
                "Drink warm fluids like herbal teas and soups",
                "Use extra blankets to stay warm during shivering",
                "Take paracetamol if fever develops",
                "Monitor body temperature regularly",
                "Use steam inhalation for nasal congestion",
                "Get adequate sleep for recovery",
                "Avoid cold environments and drafts",
                "Practice good hand hygiene",
                "Consult doctor if symptoms worsen"
            ],
            "diet": [
                "Drink warm fluids frequently throughout the day",
                "Consume warm soups and broths for hydration",
                "Eat vitamin C rich foods to support immunity",
                "Include ginger tea for its warming properties",
                "Stay hydrated with warm water and herbal teas",
                "Eat easily digestible, warm meals",
                "Include garlic for its antimicrobial properties",
                "Avoid cold drinks and raw foods",
                "Consume small, frequent warm meals",
                "Include spices like cinnamon and black pepper"
            ]
        }),
        
        frozenset(["Cough", "Fever"]): ("Viral Infection", {
            "precautions": [
                "Get adequate rest to help body fight infection",
                "Take paracetamol for fever and discomfort",
                "Monitor temperature every 4-6 hours",
                "Stay hydrated with water and electrolyte drinks",
                "Use cough suppressants or expectorants as needed",
                "Take steam inhalation to relieve cough",
                "Isolate to prevent spreading infection",
                "Use humidifier in room",
                "Get plenty of sleep",
                "Consult doctor if fever persists beyond 3 days"
            ],
            "diet": [
                "Drink plenty of fluids including water and herbal teas",
                "Consume warm soups and broths for hydration",
                "Eat vitamin C rich fruits and vegetables",
                "Include protein-rich foods for immune support",
                "Stay hydrated with electrolyte solutions if needed",
                "Eat small, frequent meals to maintain energy",
                "Avoid heavy, greasy, or spicy foods",
                "Include zinc-rich foods for immune function",
                "Consume probiotic foods for gut health",
                "Drink warm water with honey and lemon"
            ]
        }),
        
        frozenset(["Cough", "Fatigue"]): ("Viral Infection", {
            "precautions": [
                "Stay hydrated with water and healthy fluids",
                "Get plenty of rest and avoid physical exertion",
                "Use cough remedies as needed for symptom relief",
                "Take steam inhalation to loosen mucus",
                "Practice good sleep hygiene",
                "Avoid smoking and irritants",
                "Use humidifier to keep air moist",
                "Monitor for fever or other symptoms",
                "Pace activities and take breaks",
                "Consult doctor if symptoms persist"
            ],
            "diet": [
                "Stay well hydrated with water, soups, and teas",
                "Eat protein-rich foods for energy and recovery",
                "Consume complex carbohydrates for sustained energy",
                "Include vitamin C rich foods for immune support",
                "Eat small, frequent meals to maintain energy levels",
                "Include zinc-rich foods for immune function",
                "Avoid heavy, hard-to-digest meals",
                "Consume probiotic foods for gut health",
                "Drink warm fluids with honey for cough relief",
                "Eat balanced, nutrient-dense meals"
            ]
        }),
        
        frozenset(["Fever", "Fatigue"]): ("Possible Viral Infection", {
            "precautions": [
                "Get plenty of rest and prioritize sleep",
                "Stay hydrated with water and electrolyte drinks",
                "Monitor body temperature regularly",
                "Take paracetamol if fever is uncomfortable",
                "Use lukewarm sponge baths for comfort",
                "Wear light, breathable clothing",
                "Avoid strenuous activities",
                "Practice good personal hygiene",
                "Monitor for other symptoms developing",
                "Consult doctor if fever persists beyond 3 days"
            ],
            "diet": [
                "Drink plenty of fluids including water and herbal teas",
                "Consume electrolyte-rich drinks and coconut water",
                "Eat light, easily digestible foods",
                "Include vitamin C rich fruits and vegetables",
                "Stay hydrated with clear soups and broths",
                "Eat small, frequent meals to maintain energy",
                "Include protein-rich foods for recovery",
                "Avoid heavy, greasy, or spicy foods",
                "Consume probiotic foods for immune support",
                "Eat foods with natural anti-inflammatory properties"
            ]
        }),
        
        frozenset(["Cough", "Chest Pain"]): ("Possible Pneumonia", {
            "precautions": [
                "Consult physician for proper evaluation",
                "Monitor breathing patterns and chest pain",
                "Get plenty of rest",
                "Take prescribed medications as directed",
                "Use steam inhalation to help clear lungs",
                "Practice deep breathing exercises",
                "Avoid smoking and pollutants",
                "Monitor for fever or breathing difficulties",
                "Keep follow-up appointments",
                "Seek emergency care if symptoms worsen"
            ],
            "diet": [
                "Eat high-protein foods for tissue repair",
                "Consume vitamin A and C rich foods for lung health",
                "Stay hydrated with warm fluids and broths",
                "Include zinc-rich foods for immune support",
                "Eat small, frequent meals to avoid strain",
                "Avoid dairy if it thickens mucus",
                "Include antioxidant-rich fruits and vegetables",
                "Consume foods with natural antimicrobial properties",
                "Eat easily digestible, nutritious meals",
                "Stay well hydrated with water and herbal teas"
            ]
        }),
        
        frozenset(["Cough", "Shortness of Breath"]): ("Possible Bronchitis/Asthma", {
            "precautions": [
                "Use inhaler if prescribed by doctor",
                "Avoid smoking and secondhand smoke",
                "Take steam inhalation to relieve symptoms",
                "Practice breathing exercises",
                "Avoid cold air and pollutants",
                "Use humidifier in living space",
                "Monitor symptoms and breathing patterns",
                "Keep rescue medication accessible",
                "Avoid strenuous activities",
                "Consult doctor for proper diagnosis"
            ],
            "diet": [
                "Drink warm fluids to help thin mucus",
                "Eat anti-inflammatory foods like ginger and turmeric",
                "Include omega-3 rich foods for lung health",
                "Consume vitamin C rich fruits and vegetables",
                "Stay hydrated with water and herbal teas",
                "Avoid cold drinks and foods that trigger symptoms",
                "Include magnesium-rich foods for bronchial relaxation",
                "Eat small, frequent meals to avoid pressure on diaphragm",
                "Consume foods with natural bronchodilating properties",
                "Avoid foods that cause gas or bloating"
            ]
        }),
        
        frozenset(["Shortness of Breath", "Fatigue"]): ("Possible Asthma", {
            "precautions": [
                "Monitor breathing patterns regularly",
                "Get adequate rest and avoid overexertion",
                "Use prescribed inhalers as directed",
                "Avoid known triggers and allergens",
                "Practice relaxation and breathing techniques",
                "Keep emergency medication accessible",
                "Maintain good indoor air quality",
                "Avoid smoking and strong odors",
                "Pace activities and take breaks",
                "Consult doctor for proper evaluation"
            ],
            "diet": [
                "Eat small, frequent meals to avoid diaphragm pressure",
                "Include magnesium-rich foods for bronchial relaxation",
                "Consume omega-3 rich foods to reduce inflammation",
                "Eat antioxidant-rich fruits and vegetables",
                "Stay well hydrated with room temperature water",
                "Include vitamin C and E rich foods for lung health",
                "Avoid foods that trigger allergies or asthma",
                "Eat balanced, nutrient-dense meals",
                "Include probiotic foods for immune regulation",
                "Avoid heavy meals before physical activity"
            ]
        }),

            # 💖 CARDIOVASCULAR & SYSTEMIC
        frozenset(["Chest Pain", "Shortness of Breath", "Sweating"]): ("Heart Attack (Emergency)", {
            "precautions": [
                "Call emergency services immediately - do not delay",
                "Chew and swallow aspirin (325mg) if not allergic and advised",
                "Stay calm and sit in comfortable position",
                "Loosen tight clothing around neck and chest",
                "Do not attempt to drive yourself to hospital",
                "Keep emergency contact numbers easily accessible",
                "Wait for emergency medical services to arrive",
                "Do not eat or drink anything except aspirin",
                "Monitor symptoms and report changes to emergency responders",
                "Keep prescribed medications and medical history ready"
            ],
            "diet": [
                "EMERGENCY - No food or drink until medically evaluated",
                "Long-term: Follow heart-healthy diet low in saturated fats",
                "Include plenty of fruits and vegetables daily",
                "Choose whole grains over refined carbohydrates",
                "Consume lean proteins like fish and poultry",
                "Use healthy fats from olive oil, nuts, and avocados",
                "Limit sodium intake to control blood pressure",
                "Avoid processed and fried foods completely",
                "Control portion sizes to maintain healthy weight",
                "Stay hydrated with water and herbal teas"
            ]
        }),
        
        frozenset(["Chest Pain", "Shortness of Breath", "Fatigue"]): ("Heart Disease", {
            "precautions": [
                "Consult cardiologist for comprehensive evaluation",
                "Avoid stress through meditation and relaxation techniques",
                "Take prescribed medications regularly without missing doses",
                "Monitor blood pressure and heart rate daily",
                "Avoid sudden physical exertion and heavy lifting",
                "Maintain healthy weight through balanced lifestyle",
                "Quit smoking and avoid secondhand smoke",
                "Limit alcohol consumption to moderate levels",
                "Learn warning signs of heart problems",
                "Attend regular follow-up appointments"
            ],
            "diet": [
                "Follow Mediterranean-style diet rich in plant-based foods",
                "Consume low-sodium foods and avoid added salt",
                "Include healthy fats from olive oil, nuts, and fish",
                "Eat high-fiber foods like oats, legumes, and vegetables",
                "Choose lean proteins like fish, skinless poultry, and legumes",
                "Avoid processed foods, fried items, and trans fats",
                "Include potassium-rich foods like bananas and leafy greens",
                "Eat small, frequent meals instead of large heavy meals",
                "Limit red meat and high-cholesterol foods",
                "Stay hydrated with water and heart-healthy beverages"
            ]
        }),
        
        frozenset(["Chest Pain", "Sweating", "Fatigue"]): ("Angina", {
            "precautions": [
                "Rest immediately when chest pain occurs",
                "Consult cardiologist for ECG and proper diagnosis",
                "Take prescribed nitroglycerin medication as directed",
                "Avoid physical and emotional stress triggers",
                "Keep emergency medication accessible at all times",
                "Monitor pattern and frequency of angina episodes",
                "Avoid extreme temperatures and strenuous activities",
                "Pace physical activities and take frequent breaks",
                "Carry medical information and emergency contacts",
                "Attend regular cardiac follow-up appointments"
            ],
            "diet": [
                "Eat small, frequent meals to avoid overloading heart",
                "Follow low-cholesterol diet with limited saturated fats",
                "Include potassium-rich foods like bananas and sweet potatoes",
                "Consume magnesium sources like nuts, seeds, and leafy greens",
                "Avoid heavy meals, especially before physical activity",
                "Limit caffeine intake which can trigger symptoms",
                "Include healthy fats from fish, nuts, and olive oil",
                "Eat high-fiber foods to maintain healthy cholesterol",
                "Choose antioxidant-rich fruits and vegetables",
                "Stay well-hydrated with water throughout day"
            ]
        }),

        # Single symptoms cardiovascular
        frozenset(["Chest Pain"]): ("Monitor Heart Symptoms", {
            "precautions": [
                "Consult doctor for proper evaluation and diagnosis",
                "Monitor severity, duration, and triggers of pain",
                "Keep track of when pain occurs and associated symptoms",
                "Avoid strenuous activities until cleared by doctor",
                "Rest in comfortable position when pain occurs",
                "Monitor for accompanying symptoms like shortness of breath",
                "Keep emergency contacts readily available",
                "Do not ignore persistent or severe chest pain",
                "Follow up with healthcare provider as recommended",
                "Learn to recognize emergency warning signs"
            ],
            "diet": [
                "Eat small, frequent meals instead of large ones",
                "Avoid spicy, greasy, and heavy foods",
                "Stay hydrated with water between meals",
                "Include heart-healthy anti-inflammatory foods",
                "Avoid caffeine and alcohol which can trigger pain",
                "Eat fiber-rich foods for digestive health",
                "Include healthy fats in moderation",
                "Avoid eating right before bedtime",
                "Consume balanced, nutritious meals",
                "Stay away from foods that cause discomfort"
            ]
        }),
        
        frozenset(["Shortness of Breath"]): ("Monitor Breathing", {
            "precautions": [
                "Seek medical help immediately if severe or worsening",
                "Monitor breathing patterns and rate regularly",
                "Rest in comfortable, upright position",
                "Practice deep breathing and relaxation exercises",
                "Avoid triggers like smoke, dust, and strong odors",
                "Keep emergency inhaler accessible if prescribed",
                "Stay in well-ventilated areas",
                "Avoid strenuous activities and pace yourself",
                "Monitor for other concerning symptoms",
                "Keep emergency numbers easily accessible"
            ],
            "diet": [
                "Eat small, frequent meals to avoid pressure on diaphragm",
                "Stay well hydrated with room temperature water",
                "Include magnesium-rich foods for bronchial relaxation",
                "Consume omega-3 rich foods for anti-inflammatory benefits",
                "Avoid heavy meals and carbonated drinks",
                "Include antioxidant-rich fruits and vegetables",
                "Eat foods rich in B vitamins for energy production",
                "Avoid foods that cause bloating or gas",
                "Stay hydrated with herbal teas like peppermint",
                "Eat balanced, easily digestible meals"
            ]
        }),
        
        frozenset(["Sweating"]): ("Monitor Sweating", {
            "precautions": [
                "Rest and observe for other symptoms",
                "Monitor sweating patterns and triggers",
                "Stay in cool, well-ventilated environments",
                "Wear breathable, moisture-wicking clothing",
                "Stay hydrated with water and electrolytes",
                "Monitor body temperature regularly",
                "Practice stress-reduction techniques",
                "Keep a symptom diary to identify patterns",
                "Consult doctor if sweating is excessive or unexplained",
                "Maintain good personal hygiene"
            ],
            "diet": [
                "Stay well hydrated with water and electrolyte drinks",
                "Eat water-rich fruits and vegetables",
                "Include potassium-rich foods to replace electrolytes",
                "Consume magnesium-rich foods for nerve function",
                "Avoid spicy foods and caffeine which can trigger sweating",
                "Eat light, easily digestible meals",
                "Include cooling foods like cucumber and mint",
                "Avoid alcohol and hot temperature foods",
                "Eat small, frequent meals",
                "Include herbal teas with sage or chamomile"
            ]
        }),
        
        frozenset(["Fatigue"]): ("Monitor Fatigue", {
            "precautions": [
                "Rest and hydrate adequately",
                "Practice good sleep hygiene and get 7-8 hours sleep",
                "Manage stress through meditation and relaxation",
                "Maintain regular sleep-wake schedule",
                "Avoid overexertion and pace daily activities",
                "Monitor for other symptoms developing",
                "Get moderate exercise if energy permits",
                "Take short naps during day if needed",
                "Consult doctor if fatigue persists beyond 2 weeks",
                "Check for nutritional deficiencies and anemia"
            ],
            "diet": [
                "Stay well hydrated with water and herbal teas",
                "Eat iron-rich foods like leafy greens, lentils, lean meat",
                "Include complex carbohydrates for sustained energy",
                "Consume protein-rich foods with each meal",
                "Eat small, frequent meals to maintain energy levels",
                "Include B-vitamin rich foods like whole grains and eggs",
                "Stay hydrated with electrolyte drinks if needed",
                "Avoid excessive caffeine and sugar crashes",
                "Include magnesium-rich foods like nuts and seeds",
                "Eat balanced, nutrient-dense meals"
            ]
        }),
            
            # 2-symptom pairs cardiovascular
        frozenset(["Chest Pain", "Shortness of Breath"]): ("Heart Disease / Angina", {
            "precautions": [
                "Consult cardiologist for comprehensive cardiac evaluation",
                "Monitor symptoms and keep detailed record of episodes",
                "Avoid physical exertion and emotional stress",
                "Take prescribed medications regularly as directed",
                "Keep emergency contact numbers readily available",
                "Learn to recognize warning signs of worsening condition",
                "Practice relaxation techniques and stress management",
                "Carry prescribed emergency medication if available",
                "Schedule regular follow-up appointments",
                "Seek immediate medical help for severe symptoms"
            ],
            "diet": [
                "Follow heart-healthy Mediterranean diet principles",
                "Consume low-sodium foods and limit salt intake",
                "Include potassium-rich foods like bananas and leafy greens",
                "Eat small, frequent meals to avoid cardiac strain",
                "Choose lean proteins and healthy fats",
                "Include high-fiber foods for cholesterol management",
                "Avoid heavy, greasy, and processed foods",
                "Stay well hydrated with water and herbal teas",
                "Limit caffeine and alcohol consumption",
                "Include antioxidant-rich fruits and vegetables"
            ]
        }),
        
        frozenset(["Chest Pain", "Sweating"]): ("Angina / Heart Issue", {
            "precautions": [
                "Rest immediately and monitor symptoms closely",
                "Avoid physical activity until symptoms resolve",
                "Keep track of symptom patterns and triggers",
                "Take prescribed nitroglycerin if available",
                "Stay in comfortable, well-ventilated environment",
                "Monitor blood pressure and heart rate if possible",
                "Avoid stress and emotional triggers",
                "Keep emergency contacts accessible",
                "Consult cardiologist for proper diagnosis",
                "Seek emergency care if symptoms worsen"
            ],
            "diet": [
                "Eat small, light meals to prevent cardiac overload",
                "Avoid spicy foods and heavy meals",
                "Include magnesium-rich foods for heart muscle function",
                "Consume foods rich in coenzyme Q10 (fish, organ meats)",
                "Stay hydrated with water at room temperature",
                "Avoid caffeine and stimulants that can trigger symptoms",
                "Include anti-inflammatory foods in diet",
                "Eat potassium-rich foods for electrolyte balance",
                "Avoid eating large meals before physical activity",
                "Choose easily digestible, nutritious foods"
            ]
        }),
        
        frozenset(["Chest Pain", "Fatigue"]): ("Heart Disease / Angina", {
            "precautions": [
                "Consult cardiologist for proper cardiac assessment",
                "Balance rest with gentle activity as tolerated",
                "Monitor energy levels and pace daily activities",
                "Take prescribed heart medications consistently",
                "Avoid sudden physical exertion",
                "Practice stress reduction techniques",
                "Keep symptom diary to identify patterns",
                "Get adequate quality sleep nightly",
                "Attend regular cardiac follow-ups",
                "Seek immediate help for worsening chest pain"
            ],
            "diet": [
                "Eat balanced meals with controlled portions",
                "Include iron-rich foods if anemia is suspected",
                "Consume complex carbohydrates for sustained energy",
                "Include lean proteins for muscle strength",
                "Stay well hydrated throughout the day",
                "Avoid heavy meals that cause fatigue",
                "Include B-vitamin rich foods for energy production",
                "Eat small, frequent meals to maintain energy",
                "Include heart-healthy fats in moderation",
                "Choose nutrient-dense, easily digestible foods"
            ]
        }),
        
        frozenset(["Shortness of Breath", "Sweating"]): ("Heart Issue", {
            "precautions": [
                "Seek medical attention for proper evaluation",
                "Rest in comfortable, upright position",
                "Monitor breathing patterns and sweating episodes",
                "Avoid physical exertion until evaluated",
                "Practice calm, controlled breathing techniques",
                "Keep emergency contacts readily available",
                "Stay in cool, well-ventilated environment",
                "Monitor for additional symptoms developing",
                "Do not ignore these symptoms",
                "Follow up with healthcare provider promptly"
            ],
            "diet": [
                "Eat small meals to avoid diaphragmatic pressure",
                "Stay hydrated with electrolyte-rich fluids",
                "Include magnesium-rich foods for bronchial relaxation",
                "Consume potassium-rich foods for electrolyte balance",
                "Avoid heavy, gas-producing foods",
                "Include antioxidant-rich fruits and vegetables",
                "Eat light, easily digestible meals",
                "Avoid caffeine and alcohol",
                "Include omega-3 foods for cardiovascular health",
                "Stay well hydrated with water and herbal teas"
            ]
        }),
        
        frozenset(["Shortness of Breath", "Fatigue"]): ("Heart Issue", {
            "precautions": [
                "Monitor symptoms and their patterns closely",
                "Balance activity with adequate rest periods",
                "Practice breathing exercises regularly",
                "Avoid overexertion and pace activities",
                "Keep record of symptom triggers and severity",
                "Consult healthcare provider for evaluation",
                "Monitor for worsening of symptoms",
                "Practice stress management techniques",
                "Get adequate sleep and rest",
                "Seek medical help if symptoms progress"
            ],
            "diet": [
                "Eat small, frequent meals to maintain energy",
                "Include iron-rich foods to combat fatigue",
                "Consume complex carbohydrates for sustained energy",
                "Stay well hydrated with water and healthy fluids",
                "Include protein-rich foods with each meal",
                "Avoid heavy meals that cause bloating",
                "Include B-vitamin sources for energy metabolism",
                "Eat magnesium-rich foods for muscle function",
                "Choose easily digestible, nutritious foods",
                "Include antioxidant-rich fruits and vegetables"
            ]
        }),
        
        frozenset(["Sweating", "Fatigue"]): ("Heart Issue", {
            "precautions": [
                "Rest and observe symptom patterns",
                "Monitor for additional cardiac symptoms",
                "Practice stress reduction techniques",
                "Maintain comfortable room temperature",
                "Stay hydrated with electrolyte solutions",
                "Keep symptom diary to track patterns",
                "Avoid overexertion and heat exposure",
                "Consult doctor if symptoms persist",
                "Get adequate rest and quality sleep",
                "Monitor for chest pain or breathing issues"
            ],
            "diet": [
                "Stay well hydrated with water and electrolyte drinks",
                "Eat potassium-rich foods to replace lost electrolytes",
                "Include magnesium sources for energy production",
                "Consume iron-rich foods if fatigue is significant",
                "Eat small, frequent meals to maintain energy",
                "Include B-vitamin rich foods for metabolic support",
                "Avoid caffeine and sugar crashes",
                "Include cooling foods like cucumber and melon",
                "Eat balanced, nutrient-dense meals",
                "Stay hydrated with coconut water and herbal teas"
            ]
        }),

            # 🧠 NEUROLOGICAL & PSYCHOLOGICAL
        frozenset(["Headache", "Nausea", "Vomiting"]): ("Migraine", {
            "precautions": [
                "Rest in dark, quiet room during migraine attacks",
                "Avoid loud noises and bright lights that trigger symptoms",
                "Stay hydrated with small sips of water to prevent dehydration",
                "Apply cold compress to forehead and back of neck",
                "Take prescribed migraine medication at first sign of attack",
                "Practice relaxation techniques like deep breathing",
                "Identify and avoid personal migraine triggers",
                "Maintain consistent sleep schedule even on weekends",
                "Avoid skipping meals and maintain regular eating pattern",
                "Use acupressure or gentle massage for relief"
            ],
            "diet": [
                "Identify and avoid trigger foods like aged cheese and processed meats",
                "Eat regular meals to prevent low blood sugar triggering migraines",
                "Include magnesium-rich foods like spinach, pumpkin seeds, and almonds",
                "Drink ginger tea or chew ginger for nausea relief",
                "Stay well hydrated with electrolyte-rich fluids",
                "Include riboflavin (B2) rich foods like eggs and lean meats",
                "Eat omega-3 rich foods like salmon and walnuts for anti-inflammatory benefits",
                "Avoid chocolate, alcohol, and artificial sweeteners if they trigger migraines",
                "Include fresh fruits and vegetables for antioxidant support",
                "Eat small, frequent meals to maintain stable blood sugar levels"
            ]
        }),
        
        frozenset(["Headache", "Insomnia", "Anxiety & Depression"]): ("Mental Stress Disorder", {
            "precautions": [
                "Practice daily meditation and mindfulness exercises",
                "Maintain proper sleep hygiene with consistent bedtime routine",
                "Talk to a therapist or counselor for professional support",
                "Limit screen time before bed and create relaxing environment",
                "Engage in regular physical activity to reduce stress hormones",
                "Practice deep breathing exercises during anxious moments",
                "Set realistic goals and prioritize tasks to reduce overwhelm",
                "Take regular breaks during work and practice mindfulness",
                "Connect with supportive friends and family members regularly",
                "Consider cognitive behavioral therapy for long-term management"
            ],
            "diet": [
                "Eat complex carbohydrates like whole grains for steady energy",
                "Include omega-3 fatty acids from fish, walnuts, and flaxseeds",
                "Consume magnesium-rich foods like leafy greens, nuts, and seeds",
                "Limit caffeine and alcohol intake which can worsen anxiety",
                "Eat regular, balanced meals to maintain stable blood sugar",
                "Include B-vitamin rich foods like eggs, legumes, and whole grains",
                "Eat tryptophan sources like turkey, bananas, and oats for serotonin production",
                "Include antioxidant-rich fruits and vegetables for brain health",
                "Stay hydrated with water and calming herbal teas like chamomile",
                "Avoid processed foods and excessive sugar which can cause mood swings"
            ]
        }),
        
        frozenset(["Insomnia", "Fatigue", "Anxiety & Depression"]): ("Sleep Disorder", {
            "precautions": [
                "Maintain regular sleep schedule even on weekends",
                "Limit caffeine intake, especially after 2 PM",
                "Seek therapy or counseling if sleep problems persist",
                "Create relaxing bedtime routine with warm bath and reading",
                "Use bedroom only for sleep and intimacy (no work or screens)",
                "Ensure comfortable sleep environment - dark, quiet, and cool",
                "Avoid heavy meals, alcohol, and vigorous exercise before bed",
                "Get regular sunlight exposure during daytime hours",
                "Limit naps to 20-30 minutes if needed during day",
                "Practice stress-reduction techniques throughout day"
            ],
            "diet": [
                "Eat tryptophan-rich foods like turkey, milk, and bananas at dinner",
                "Include magnesium sources like almonds, spinach, and pumpkin seeds",
                "Have complex carbohydrates with dinner to promote sleepiness",
                "Avoid heavy, rich meals within 2-3 hours of bedtime",
                "Drink herbal teas like chamomile or lavender before bed",
                "Include tart cherry juice which contains natural melatonin",
                "Eat warm milk with turmeric or honey before bedtime",
                "Include foods rich in calcium like yogurt and leafy greens",
                "Avoid spicy foods, chocolate, and caffeine in evenings",
                "Eat light snack if hungry before bed - banana or small yogurt"
            ]
        }),
        
        frozenset(["Blurred Vision", "Numbness", "Fatigue"]): ("Neuropathy", {
            "precautions": [
                "Check blood sugar levels regularly if diabetic",
                "Avoid alcohol consumption which can worsen nerve damage",
                "Consult neurologist for proper diagnosis and treatment plan",
                "Protect numb areas from injury - check feet daily",
                "Take prescribed nerve pain medications as directed",
                "Regular foot inspections for cuts, blisters, or injuries",
                "Wear proper footwear and avoid walking barefoot",
                "Avoid prolonged pressure on affected limbs",
                "Manage underlying conditions like diabetes effectively",
                "Get regular neurological examinations and follow-ups"
            ],
            "diet": [
                "Eat B-vitamin rich foods - whole grains, eggs, leafy greens",
                "Include alpha-lipoic acid sources like spinach, broccoli, potatoes",
                "Consume omega-3 fatty acids for nerve health and inflammation reduction",
                "Eat antioxidant-rich fruits and vegetables for nerve protection",
                "Limit sugar and refined carbohydrates to control blood sugar",
                "Include magnesium-rich foods for nerve function",
                "Eat vitamin E sources like nuts and seeds for nerve health",
                "Stay well-hydrated with water and herbal teas",
                "Include lean proteins for tissue repair and maintenance",
                "Avoid processed foods and focus on whole, nutrient-dense foods"
            ]
        }),
        
        frozenset(["Fatigue", "Numbness", "Weight Loss"]): ("Diabetes", {
            "precautions": [
                "Check blood sugar regularly using glucose monitor",
                "Take prescribed medications consistently as directed",
                "Follow diabetic diet with controlled carbohydrate intake",
                "Consult endocrinologist for comprehensive management",
                "Daily foot care inspection for any cuts or sores",
                "Regular eye examinations to monitor for retinopathy",
                "Carry fast-acting sugar source for hypoglycemia episodes",
                "Wear medical alert identification for emergencies",
                "Exercise regularly as approved by healthcare provider",
                "Attend regular medical check-ups and blood tests"
            ],
            "diet": [
                "Follow balanced meals with controlled carbohydrate portions",
                "Eat high fiber foods - vegetables, whole grains, legumes",
                "Choose lean proteins with each meal - fish, chicken, tofu",
                "Include healthy fats - avocados, nuts, olive oil",
                "Limit sugary foods, desserts, and sweetened beverages",
                "Eat regular meal timing to maintain stable blood sugar",
                "Practice portion control to manage weight effectively",
                "Choose non-starchy vegetables as main carbohydrate source",
                "Include whole grains instead of refined grains",
                "Stay well-hydrated with water and unsweetened beverages"
            ]
        }),

            # Single symptoms neurological
            # 🧠 NEUROLOGICAL & PSYCHOLOGICAL – SINGLE SYMPTOMS (Expanded Advice)
        frozenset(["Headache"]): ("Monitor Headache", {
            "precautions": [
                "Take rest in a quiet and dark room whenever possible",
                "Stay hydrated by drinking plenty of water throughout the day",
                "Avoid prolonged screen time and reduce exposure to bright lights",
                "Consider over-the-counter pain relief if headache persists",
                "Apply cold or warm compress to forehead and neck",
                "Practice relaxation techniques and deep breathing",
                "Maintain regular sleep schedule and avoid sleep deprivation",
                "Monitor headache patterns and potential triggers",
                "Avoid strong smells and noisy environments",
                "Consult doctor if headaches are frequent or severe"
            ],
            "diet": [
                "Stay well hydrated with water and herbal teas",
                "Eat regular meals to prevent low blood sugar headaches",
                "Include magnesium-rich foods like nuts, seeds, and leafy greens",
                "Consume ginger tea for its anti-inflammatory properties",
                "Avoid common headache triggers like aged cheese and processed meats",
                "Include omega-3 rich foods for anti-inflammatory benefits",
                "Eat foods rich in riboflavin (B2) like eggs and lean meats",
                "Avoid caffeine withdrawal if you regularly consume caffeine",
                "Include fresh fruits and vegetables for antioxidants",
                "Eat small, frequent meals to maintain stable blood sugar"
            ]
        }),
        
        frozenset(["Nausea"]): ("Monitor Nausea", {
            "precautions": [
                "Drink small sips of water or clear fluids regularly to stay hydrated",
                "Avoid greasy, spicy, or heavy meals until nausea subsides",
                "Rest in a comfortable position and avoid sudden movements",
                "Use ginger tea or ginger candies for natural relief",
                "Practice deep breathing and relaxation techniques",
                "Avoid strong odors and stuffy environments",
                "Eat small, bland meals when able to eat",
                "Get fresh air and proper ventilation",
                "Use acupressure wrist bands if helpful",
                "Consult physician if nausea is severe, persistent, or accompanied by other symptoms"
            ],
            "diet": [
                "Drink clear fluids like water, herbal tea, or clear broths",
                "Eat bland foods like crackers, toast, or plain rice",
                "Include ginger in tea or meals for natural anti-nausea effects",
                "Avoid fatty, fried, or strongly flavored foods",
                "Eat small, frequent meals instead of large ones",
                "Include peppermint tea for its soothing properties",
                "Avoid dairy products if they worsen nausea",
                "Eat slowly and chew food thoroughly",
                "Include electrolyte drinks if vomiting occurs",
                "Avoid cooking smells if they trigger nausea"
            ]
        }),
        
        frozenset(["Vomiting"]): ("Monitor Vomiting", {
            "precautions": [
                "Take small sips of water or oral rehydration solution to prevent dehydration",
                "Avoid solid food until vomiting stops, then eat bland foods gradually",
                "Rest and avoid strenuous activities until fully recovered",
                "Use cool compresses on forehead and back of neck",
                "Practice deep breathing to control nausea",
                "Avoid strong smells and triggers",
                "Maintain good hygiene to prevent spreading infection",
                "Rest in comfortable position with head elevated",
                "Use ginger or peppermint for natural relief",
                "Seek medical attention if vomiting is frequent, contains blood, or persists for more than 24 hours"
            ],
            "diet": [
                "Start with clear liquids - water, ORS, clear broths",
                "Gradually introduce BRAT diet - bananas, rice, applesauce, toast",
                "Avoid dairy, fatty, and spicy foods initially",
                "Include ginger tea or ginger ale for stomach settling",
                "Eat small amounts frequently rather than large meals",
                "Stay hydrated with electrolyte solutions",
                "Avoid acidic juices and carbonated drinks",
                "Include plain crackers or dry toast",
                "Consume probiotic foods once vomiting stops",
                "Gradually return to normal diet over 2-3 days"
            ]
        }),
        
        frozenset(["Insomnia"]): ("Monitor Sleep", {
            "precautions": [
                "Maintain a regular sleep schedule, going to bed and waking up at consistent times",
                "Avoid caffeine or heavy meals close to bedtime",
                "Create a calm and dark sleeping environment",
                "Practice relaxation techniques like deep breathing or meditation",
                "Limit screen time before bed and use blue light filters",
                "Use bedroom only for sleep and intimacy",
                "Get regular exercise but not too close to bedtime",
                "Avoid long naps during the day",
                "Establish a relaxing pre-sleep routine",
                "Consult doctor if insomnia persists affecting daily life"
            ],
            "diet": [
                "Eat tryptophan-rich foods like turkey, milk, and bananas",
                "Include magnesium sources like almonds, spinach, and pumpkin seeds",
                "Have complex carbohydrates with dinner to promote sleepiness",
                "Avoid heavy, rich meals within 2-3 hours of bedtime",
                "Drink herbal teas like chamomile or lavender before bed",
                "Include tart cherry juice which contains natural melatonin",
                "Eat warm milk with turmeric or honey",
                "Avoid caffeine after 2 PM",
                "Include calcium-rich foods for nerve function",
                "Eat light snack if hungry before bed"
            ]
        }),
        
        frozenset(["Anxiety & Depression"]): ("Monitor Mental Health", {
            "precautions": [
                "Engage in regular physical activity to improve mood and reduce stress",
                "Practice mindfulness, meditation, or relaxation exercises daily",
                "Maintain social connections and talk to supportive friends or family",
                "Set realistic goals and break tasks into manageable steps",
                "Establish daily routine and structure",
                "Limit exposure to stressful news and social media",
                "Practice gratitude and positive thinking",
                "Get adequate sunlight exposure daily",
                "Keep a journal to express thoughts and feelings",
                "Consider consulting a therapist or counselor if feelings persist"
            ],
            "diet": [
                "Eat omega-3 rich foods like salmon, walnuts, and flaxseeds",
                "Include complex carbohydrates for steady energy and serotonin production",
                "Consume magnesium-rich foods for nerve relaxation",
                "Include B-vitamin sources for nervous system support",
                "Eat protein-rich foods with each meal",
                "Include probiotic foods for gut-brain connection",
                "Avoid excessive caffeine and sugar",
                "Stay well hydrated with water and herbal teas",
                "Include antioxidant-rich fruits and vegetables",
                "Eat regular, balanced meals throughout day"
            ]
        }),
        
        frozenset(["Blurred Vision"]): ("Monitor Vision", {
            "precautions": [
                "Take regular breaks from screens and avoid prolonged reading",
                "Ensure adequate lighting while reading or working",
                "Use proper prescription glasses if needed",
                "Practice eye exercises and blinking regularly",
                "Protect eyes from UV light with sunglasses",
                "Maintain proper distance from screens",
                "Use artificial tears if eyes feel dry",
                "Monitor for other symptoms like eye pain or headaches",
                "Avoid rubbing eyes excessively",
                "Schedule an eye check-up if vision changes persist"
            ],
            "diet": [
                "Eat foods rich in vitamin A like carrots and sweet potatoes",
                "Include lutein and zeaxanthin sources like leafy greens",
                "Consume omega-3 rich foods for eye health",
                "Include vitamin C rich fruits and vegetables",
                "Eat zinc-rich foods for retinal health",
                "Include antioxidant-rich berries and fruits",
                "Stay well hydrated with water",
                "Include vitamin E sources like nuts and seeds",
                "Eat foods containing beta-carotene",
                "Maintain balanced nutrition for overall eye health"
            ]
        }),
        
        frozenset(["Numbness"]): ("Monitor Numbness", {
            "precautions": [
                "Avoid activities that may worsen numbness or cause injury",
                "Maintain proper posture to prevent nerve compression",
                "Change positions frequently to improve circulation",
                "Protect numb areas from extreme temperatures",
                "Wear proper footwear and check feet daily if foot numbness",
                "Practice gentle exercises to improve circulation",
                "Avoid prolonged pressure on affected areas",
                "Monitor for changes in sensation or movement",
                "Keep affected limbs warm and comfortable",
                "Consult neurologist to check for underlying causes"
            ],
            "diet": [
                "Eat B-vitamin rich foods for nerve health",
                "Include magnesium sources for nerve function",
                "Consume omega-3 fatty acids for anti-inflammatory benefits",
                "Include alpha-lipoic acid sources like spinach and broccoli",
                "Eat antioxidant-rich fruits and vegetables",
                "Include zinc-rich foods for nerve repair",
                "Stay well hydrated with water",
                "Include vitamin E sources for nerve protection",
                "Avoid excessive alcohol which can worsen nerve damage",
                "Eat balanced meals with variety of nutrients"
            ]
        }),
        
        frozenset(["Weight Loss"]): ("Monitor Weight", {
            "precautions": [
                "Track your weight regularly and maintain records",
                "Maintain balanced diet rich in nutrients and calories",
                "Consult physician to rule out underlying conditions",
                "Monitor appetite and eating patterns",
                "Include strength training to maintain muscle mass",
                "Keep food diary to track intake",
                "Address any digestive issues promptly",
                "Manage stress which can affect appetite",
                "Get adequate sleep and rest",
                "Seek guidance from nutritionist for proper diet"
            ],
            "diet": [
                "Include high-calorie healthy foods like nuts and avocados",
                "Eat protein-rich foods to maintain muscle mass",
                "Consume complex carbohydrates for energy",
                "Include healthy fats from olive oil, nuts, and seeds",
                "Eat small, frequent meals throughout the day",
                "Include calorie-dense smoothies and shakes",
                "Add nutritious toppings to meals",
                "Stay well hydrated with calorie-containing fluids",
                "Include dairy products if tolerated",
                "Eat balanced meals with all food groups"
            ]
        }),

        # 2-symptom pairs neurological
        frozenset(["Headache", "Nausea"]): ("Migraine", {
            "precautions": [
                "Rest in a quiet, dark room to ease headache and nausea",
                "Stay hydrated with small sips of water",
                "Avoid foods that trigger migraines",
                "Use cold compress on forehead and back of neck",
                "Practice relaxation exercises to reduce tension",
                "Take prescribed migraine medication if available",
                "Avoid strong smells and bright lights",
                "Monitor symptoms for improvement or worsening",
                "Use ginger for nausea relief",
                "Consult doctor if symptoms persist or worsen"
            ],
            "diet": [
                "Drink ginger tea for nausea relief",
                "Eat small, bland meals when able",
                "Include magnesium-rich foods",
                "Stay hydrated with electrolyte drinks",
                "Avoid common migraine triggers",
                "Eat regular meals to prevent low blood sugar",
                "Include anti-inflammatory foods",
                "Avoid caffeine and alcohol",
                "Eat easily digestible foods",
                "Include B-vitamin rich foods"
            ]
        }),
        
        frozenset(["Headache", "Vomiting"]): ("Migraine", {
            "precautions": [
                "Rest in comfortable position and avoid bright lights",
                "Drink fluids to stay hydrated and prevent dehydration",
                "Use cold packs for headache relief",
                "Take small sips of water or electrolyte solutions",
                "Avoid strong odors and triggers",
                "Practice deep breathing exercises",
                "Rest in quiet, dark environment",
                "Use acupressure points for relief",
                "Monitor for signs of severe dehydration",
                "Seek medical advice if vomiting is severe or persistent"
            ],
            "diet": [
                "Start with clear liquids and electrolyte solutions",
                "Gradually introduce bland foods when vomiting stops",
                "Include ginger for nausea control",
                "Avoid solid foods until vomiting subsides",
                "Stay hydrated with small frequent sips",
                "Include BRAT diet foods when able to eat",
                "Avoid triggers like caffeine and chocolate",
                "Eat small amounts frequently",
                "Include soothing herbal teas",
                "Gradually return to normal diet"
            ]
        }),
        
        frozenset(["Nausea", "Vomiting"]): ("Migraine / Gastro Issue", {
            "precautions": [
                "Take small sips of water or ORS to prevent dehydration",
                "Avoid solid foods until symptoms subside",
                "Rest in comfortable position and monitor symptoms",
                "Use ginger or peppermint for natural relief",
                "Practice deep breathing to control nausea",
                "Avoid strong smells and triggers",
                "Maintain good hygiene to prevent spreading",
                "Rest with head elevated",
                "Use cool compresses if helpful",
                "Seek medical help if symptoms persist beyond 24 hours"
            ],
            "diet": [
                "Start with clear liquids and oral rehydration solutions",
                "Gradually introduce bland foods like crackers and toast",
                "Include ginger tea or ginger ale",
                "Avoid dairy, fatty, and spicy foods",
                "Eat small amounts frequently",
                "Stay hydrated with electrolyte drinks",
                "Include plain rice or bananas when able",
                "Avoid acidic and carbonated drinks",
                "Consume probiotic foods later",
                "Gradually return to normal diet"
            ]
        }),
        
        frozenset(["Headache", "Insomnia"]): ("Stress Disorder", {
            "precautions": [
                "Practice relaxation techniques like deep breathing",
                "Maintain regular sleep schedule and limit screens",
                "Avoid caffeine and heavy meals before bed",
                "Create calming bedtime routine",
                "Manage stress through meditation or yoga",
                "Use comfortable sleeping environment",
                "Practice good sleep hygiene",
                "Address underlying stress factors",
                "Get regular exercise during day",
                "Consider professional counseling if needed"
            ],
            "diet": [
                "Eat tryptophan-rich foods at dinner",
                "Include magnesium sources for relaxation",
                "Consume complex carbohydrates with evening meal",
                "Avoid caffeine after noon",
                "Drink calming herbal teas before bed",
                "Include B-vitamin rich foods",
                "Eat regular balanced meals",
                "Avoid heavy meals before bedtime",
                "Include omega-3 foods for brain health",
                "Stay well hydrated throughout day"
            ]
        }),
        
        frozenset(["Insomnia", "Fatigue"]): ("Sleep Disorder", {
            "precautions": [
                "Establish consistent sleep routine daily",
                "Avoid excessive caffeine or stimulants",
                "Include light exercise and short naps",
                "Create optimal sleep environment",
                "Practice relaxation techniques before bed",
                "Limit daytime napping to 20-30 minutes",
                "Manage stress and anxiety",
                "Get sunlight exposure during day",
                "Avoid electronic devices before bed",
                "Consult sleep specialist if persistent"
            ],
            "diet": [
                "Eat tryptophan-rich foods in evening",
                "Include magnesium-rich foods for sleep quality",
                "Have light carbohydrate snack before bed",
                "Avoid large meals close to bedtime",
                "Drink chamomile or lavender tea",
                "Include calcium sources for nerve function",
                "Eat balanced meals throughout day",
                "Avoid caffeine and alcohol",
                "Include protein with each meal",
                "Stay hydrated but limit fluids before bed"
            ]
        }),
        
        frozenset(["Fatigue", "Numbness"]): ("Neuropathy / Diabetes", {
            "precautions": [
                "Monitor blood sugar levels regularly if diabetic",
                "Take rest and avoid prolonged physical strain",
                "Protect numb areas from injury",
                "Practice gentle exercises for circulation",
                "Maintain proper posture and positioning",
                "Avoid activities that worsen symptoms",
                "Wear comfortable, proper-fitting shoes",
                "Check feet daily for any injuries",
                "Manage underlying health conditions",
                "Consult doctor if numbness persists"
            ],
            "diet": [
                "Eat balanced meals with controlled carbohydrates",
                "Include B-vitamin rich foods for nerve health",
                "Consume magnesium sources for energy and nerve function",
                "Include omega-3 foods for anti-inflammatory benefits",
                "Eat iron-rich foods if anemia is concern",
                "Include antioxidant-rich fruits and vegetables",
                "Stay well hydrated with water",
                "Avoid excessive sugar and processed foods",
                "Include lean proteins for sustained energy",
                "Eat small, frequent meals"
            ]
        }),
        
        frozenset(["Numbness", "Weight Loss"]): ("Diabetes / Metabolic Issue", {
            "precautions": [
                "Track weight and dietary habits carefully",
                "Maintain regular blood sugar checks",
                "Follow prescribed diet plan consistently",
                "Protect numb areas from injury and infection",
                "Monitor for other symptoms developing",
                "Practice good foot care if foot numbness",
                "Attend regular medical check-ups",
                "Manage stress and get adequate rest",
                "Follow treatment plan as directed",
                "Seek medical attention for persistent symptoms"
            ],
            "diet": [
                "Follow balanced diabetic diet if applicable",
                "Include high-calorie nutritious foods",
                "Eat protein-rich foods to maintain muscle mass",
                "Consume complex carbohydrates for energy",
                "Include healthy fats for calorie density",
                "Eat small, frequent meals throughout day",
                "Include B-vitamin sources for nerve health",
                "Stay well hydrated with water",
                "Include magnesium-rich foods",
                "Eat nutrient-dense foods"
            ]
        }),
        
        frozenset(["Fatigue", "Weight Loss"]): ("Diabetes / Thyroid", {
            "precautions": [
                "Ensure balanced diet with adequate calories",
                "Monitor blood sugar and thyroid levels",
                "Consult healthcare provider if symptoms continue",
                "Track weight changes regularly",
                "Manage stress and get adequate rest",
                "Practice gentle exercise as tolerated",
                "Address any underlying health issues",
                "Follow medical advice and treatment plans",
                "Monitor energy levels and activity tolerance",
                "Keep regular medical appointments"
            ],
            "diet": [
                "Eat calorie-dense healthy foods",
                "Include protein with each meal for muscle maintenance",
                "Consume complex carbohydrates for sustained energy",
                "Include healthy fats like nuts and avocados",
                "Eat small, frequent meals throughout day",
                "Include iron-rich foods if anemia is concern",
                "Stay well hydrated with nutritious fluids",
                "Include B-vitamin rich foods for energy",
                "Eat balanced meals with all nutrients",
                "Include energy-boosting snacks"
            ]
        }),

        # JOINTS & MUSCLES
        frozenset(["Joint Pain", "Swelling", "Fatigue"]): ("Arthritis", {
            "precautions": [
                "Exercise gently to maintain joint mobility",
                "Apply hot or cold compresses to reduce pain and swelling",
                "Consult rheumatologist for diagnosis and management",
                "Use assistive devices if needed for joint protection",
                "Maintain healthy weight to reduce joint stress",
                "Practice proper posture and body mechanics",
                "Take prescribed anti-inflammatory medications",
                "Balance rest with gentle movement",
                "Use joint protection techniques",
                "Consider physical therapy for customized exercises"
            ],
            "diet": [
                "Eat anti-inflammatory foods like fatty fish and berries",
                "Include turmeric and ginger in cooking",
                "Consume omega-3 rich foods for inflammation reduction",
                "Avoid nightshade vegetables if they worsen symptoms",
                "Include calcium-rich foods for bone health",
                "Eat vitamin D sources or get safe sun exposure",
                "Include antioxidant-rich fruits and vegetables",
                "Choose lean proteins for muscle support",
                "Eat whole grains for sustained energy",
                "Stay hydrated with anti-inflammatory herbal teas"
            ]
        }),
        
        frozenset(["Joint Pain", "Fever", "Fatigue"]): ("Rheumatic Fever", {
            "precautions": [
                "Seek prompt medical attention and follow antibiotics",
                "Rest adequately to support recovery",
                "Monitor symptoms and report any worsening",
                "Take prescribed medications completely",
                "Practice good oral hygiene to prevent infections",
                "Avoid strenuous activities during acute phase",
                "Monitor heart symptoms carefully",
                "Follow up with cardiologist if needed",
                "Complete full antibiotic course",
                "Get regular medical monitoring"
            ],
            "diet": [
                "Eat anti-inflammatory foods to reduce joint inflammation",
                "Include protein-rich foods for tissue repair",
                "Consume vitamin C rich foods for immune support",
                "Stay well hydrated with water and broths",
                "Include iron-rich foods if anemia develops",
                "Eat small, frequent meals if appetite is poor",
                "Choose soft, easy-to-eat foods if throat sore",
                "Avoid processed foods and focus on whole foods",
                "Include zinc-rich foods for immune function",
                "Eat balanced meals with variety of nutrients"
            ]
        }),
        
        frozenset(["Joint Pain", "Swelling"]): ("Arthritis", {
            "precautions": [
                "Use gentle exercises to improve flexibility",
                "Apply compresses to manage swelling",
                "Avoid overexertion to prevent joint damage",
                "Use proper body mechanics during activities",
                "Maintain healthy weight to reduce joint stress",
                "Take prescribed anti-inflammatory medications",
                "Use joint protection techniques",
                "Practice range-of-motion exercises",
                "Apply topical pain relief creams if helpful",
                "Consult doctor for proper treatment plan"
            ],
            "diet": [
                "Eat anti-inflammatory foods regularly",
                "Include turmeric and ginger in meals",
                "Consume omega-3 rich foods for joint health",
                "Avoid inflammatory foods like processed items",
                "Include calcium and vitamin D sources",
                "Eat antioxidant-rich fruits and vegetables",
                "Include lean proteins for muscle support",
                "Stay well hydrated with water",
                "Include magnesium-rich foods for muscle function",
                "Eat balanced, nutritious meals"
            ]
        }),
        frozenset(["Joint Pain"]): ("Arthritis / Joint Issue", {
            "precautions": [
                "Apply warm compress to stiff joints in the morning",
                "Use cold packs after activity to reduce inflammation",
                "Practice gentle range-of-motion exercises daily",
                "Avoid high-impact activities that stress joints",
                "Maintain healthy weight to reduce pressure on joints",
                "Use proper posture and body mechanics when lifting",
                "Take prescribed anti-inflammatory medications as directed",
                "Use assistive devices if needed (canes, braces)",
                "Practice relaxation techniques to manage pain",
                "Consult rheumatologist for proper diagnosis and treatment"
            ],
            "diet": [
                "Eat anti-inflammatory foods like fatty fish and berries",
                "Include turmeric and ginger in meals for natural relief",
                "Consume omega-3 rich foods (salmon, walnuts, flaxseeds)",
                "Avoid processed foods and refined sugars that increase inflammation",
                "Include calcium-rich foods for bone health (dairy, leafy greens)",
                "Eat vitamin D sources or get safe sun exposure",
                "Include antioxidant-rich fruits and vegetables",
                "Choose lean proteins for muscle support around joints",
                "Stay well hydrated with water and herbal teas",
                "Include magnesium-rich foods (nuts, seeds, whole grains)"
            ]
        })

    }


        # predicted = None
        predicted = None
        precautions = []
        diet = []

        for key, value in disease_map.items():
            if key.issubset(selected):
                predicted = value[0]  # Disease name
                disease_data = value[1]  # The dictionary with precautions and diet
                precautions = disease_data.get("precautions", [])
                diet = disease_data.get("diet", [])
                break

        if predicted:
            st.success(f"🩸 **Predicted Disease:** {predicted}")
            
            # Display Precautions
            st.info("### 🩹 Precautions to Take:")
            for i, p in enumerate(precautions, 1):
                st.markdown(f"{i}. {p}")
            
            # Display Diet
            st.info("### 🍽️ Diet Recommendations:")
            for i, d in enumerate(diet, 1):
                st.markdown(f"{i}. {d}")
            
            st.markdown("""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    width:100%;
                    margin-top:30px;
                ">
                    <div style="
                        text-align:center;
                        font-size:22px;
                        font-weight:700;
                        color:#cfd9ff;
                        background:rgba(47,49,54,0.85);
                        border:1px solid rgba(114,137,218,0.5);
                        border-radius:12px;
                        padding:12px 20px;
                        display:inline-block;
                        box-shadow:0px 0px 20px rgba(114,137,218,0.3);
                    ">
                    🌙 More Smart Health Tips & Lifestyle Suggestions Coming Soon 🌙
                    </div>
                </div>
            """, unsafe_allow_html=True)

        else:
            st.warning("⚠️ No exact match found. Try selecting more symptoms for better accuracy.")