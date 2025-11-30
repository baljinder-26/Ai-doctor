import streamlit as st
from streamlit_lottie import st_lottie
import requests
import s
import folium
from streamlit_folium import st_folium

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def health():
    lottie_patient = load_lottie("https://lottie.host/5b9587db-da28-4f72-b8e0-1e9f8acfab0f/Ph8Dy2Ot5z.json")

    # --- Sidebar animation ---
    with st.sidebar:
        for i in range(1,8):
            st.write("")
        st_lottie(lottie_patient, height=250, key="patient_animation")

    # --- Sidebar button restored to original ---
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
    # --- Main background ---
            discord_bg_url = "https://media.istockphoto.com/id/1340212435/vector/silhouette-of-a-human-kidney-on-a-realistic-rubber-glove-3d-medical-concept-with-the-contour.jpg?s=612x612&w=0&k=20&c=vNadPzLr9BdSGLBObu25lfaypTx709IPFOQRoU9PY5U="
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

            if "show_map" not in st.session_state:
                st.session_state.show_map = False
            if "map_data" not in st.session_state:
                st.session_state.map_data = None

            st.title("HealthFinder 🏥")
            st.write("Find all hospitals in any city")

            # --- Search Page ---
            if not st.session_state.show_map:
                # Simple city input
                city = st.text_input("🏙️ Enter city name:", 
                                   placeholder="e.g., Delhi, Mumbai, London, New York")
                
                find_btn = st.button("🔍 Find All Hospitals")

                if find_btn:
                    if city.strip() == "":
                        st.warning("Please enter a city name.")
                    else:
                        with st.spinner(f"Searching all hospitals in {city}..."):
                            # Search for hospitals in the specified city
                            query = f"hospitals in {city}"
                            url = f"https://nominatim.openstreetmap.org/search?format=json&q={query}&limit=50"
                            response = requests.get(url, headers={'User-Agent': 'HealthFinderApp'}).json()

                            if len(response) == 0:
                                st.error(f"No hospitals found in {city}. Try a different city name.")
                            else:
                                st.session_state.map_data = response
                                st.session_state.show_map = True
                                st.session_state.city = city
                                st.rerun()

            # --- Map + Card Page ---
            else:
                city = st.session_state.city

                if st.button("🔙 Back to Search"):
                    st.session_state.show_map = False
                    st.session_state.map_data = None
                    st.rerun()
                else:
                    hospital_data = st.session_state.map_data
                    
                    if hospital_data:
                        # Calculate center of all hospitals for map
                        lats = [float(h['lat']) for h in hospital_data]
                        lons = [float(h['lon']) for h in hospital_data]
                        center_lat = sum(lats) / len(lats)
                        center_lon = sum(lons) / len(lons)
                        
                        city_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

                        # Add markers for all hospitals
                        for h in hospital_data:
                            name = h.get("display_name", "Hospital")
                            lat = float(h['lat'])
                            lon = float(h['lon'])
                            google_url = f"https://www.google.com/search?q={name.replace(' ', '+')}"
                            
                            # Extract hospital name (first part of display name)
                            hospital_name = name.split(',')[0] if ',' in name else name
                            
                            folium.Marker(
                                [lat, lon],
                                popup=folium.Popup(
                                    f"""
                                    <div style="min-width: 200px;">
                                        <h4>{hospital_name}</h4>
                                        <p style="font-size: 12px; margin: 5px 0;">{name}</p>
                                        <a href='{google_url}' target='_blank' style='
                                            display: inline-block;
                                            padding: 5px 10px;
                                            background: #007bff;
                                            color: white;
                                            text-decoration: none;
                                            border-radius: 3px;
                                            font-size: 12px;
                                            margin-top: 5px;
                                        '>View Details</a>
                                    </div>
                                    """,
                                    max_width=300
                                ),
                                tooltip=hospital_name,
                                icon=folium.Icon(color='red', icon='hospital-o', prefix='fa')
                            ).add_to(city_map)

                        col1, col2 = st.columns([2, 1])
                        with col1:
                            st.write(f"### 🗺 All Hospitals in {city}")
                            st_folium(city_map, width=700, height=500, returned_objects=[])

                        with col2:
                            st.write(f"### 🏥 Hospital List ({len(hospital_data)} found)")
                            for i, h in enumerate(hospital_data[:30], 1):
                                name = h.get("display_name", "Hospital")
                                hospital_name = name.split(',')[0] if ',' in name else name
                                google_url = f"https://www.google.com/search?q={name.replace(' ', '+')}"
                                
                                st.markdown(f"""
                                <div style="
                                    background-color:#f0f2f6; 
                                    padding:12px; 
                                    border-radius:10px; 
                                    margin-bottom:8px;
                                    color:#000000;
                                    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                                    font-size:14px;
                                ">
                                    <div style="font-weight: bold; margin-bottom: 5px;">{i}. {hospital_name}</div>
                                    <div style="font-size: 12px; color: #666; margin-bottom: 8px;">
                                        {name[:100]}{'...' if len(name) > 100 else ''}
                                    </div>
                                    <a href="{google_url}" target="_blank" style="
                                        color:#007bff;
                                        text-decoration:none;
                                        font-size:12px;
                                        font-weight:bold;
                                    ">
                                        🔍 View on Google
                                    </a>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        st.success(f"✅ Found {len(hospital_data)} hospitals and medical facilities in {city}")
                    else:
                        st.error("No hospital data available. Please try searching again.")

                st.markdown("---")
            st.caption("Data provided by OpenStreetMap (Nominatim) — 100% Free & Safe.")