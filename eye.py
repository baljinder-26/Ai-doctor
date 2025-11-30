import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
from datetime import datetime
import pandas as pd

def ankhen():
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .test-section {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .risk-high {
        background-color: #ffcccc;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #ff0000;
    }
    .risk-medium {
        background-color: #fff3cd;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #ffc107;
    }
    .risk-low {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #28a745;
    }
    .result-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

    class EyeHealthChecker:
        def __init__(self):
            self.snellen_chart = {
                '20/20': ['E', 'F', 'P', 'T', 'O', 'Z', 'L', 'D'],
                '20/30': ['E', 'F', 'P', 'T', 'O', 'Z', 'L'],
                '20/40': ['E', 'F', 'P', 'T', 'O', 'Z'],
                '20/50': ['E', 'F', 'P', 'T', 'O'],
                '20/70': ['E', 'F', 'P', 'T'],
                '20/100': ['E', 'F', 'P'],
                '20/200': ['E', 'F']
            }
            self.user_data = {}
            
        def _initialize_session_state(self):
            if 'test_results' not in st.session_state:
                st.session_state.test_results = {
                    'snellen': {},
                    'grid': {},
                    'symptoms': {},
                    'last_test_date': None
                }
        
        def snellen_test(self):
            st.subheader("🔤 Visual Acuity Test (Distance Vision)")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### 📋 Instructions:")
                st.markdown("""
                1. **Position yourself** 20 feet (6 meters) from your screen
                2. **Cover one eye** at a time during testing
                3. **Read the letters** from top to bottom
                4. **Note the smallest line** where you can read most letters correctly
                5. **Ensure proper lighting** in the room
                """)
                
                distance = st.slider("📏 Distance from screen (feet)", 1, 20, 10, 
                                   help="Adjust based on your actual distance from screen")
                
                # Generate interactive Snellen chart
                st.markdown("### 👁️ Vision Test Chart")
                st.info("Read the letters aloud starting from the top")
                
                test_results = {}
                for acuity, letters in self.snellen_chart.items():
                    font_size = max(16, 42 - list(self.snellen_chart.keys()).index(acuity) * 5)
                    letters_display = ' '.join(letters)
                    
                    # Add interactive element for each line
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        st.markdown(f"<h4 style='font-size:{font_size}px; margin: 10px 0;'>{acuity}: {letters_display}</h4>", 
                                  unsafe_allow_html=True)
                    with col_b:
                        can_read = st.checkbox(f"Read {acuity}", key=f"read_{acuity}")
                        if can_read:
                            test_results[acuity] = True
                
                # Store results
                if test_results:
                    best_acuity = list(test_results.keys())[-1]
                    st.session_state.test_results['snellen']['best_acuity'] = best_acuity
                    st.session_state.test_results['snellen']['test_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            with col2:
                st.markdown("### Record Your Results📊")
                
                st.markdown("#### Left Eye Results")
                left_eye = st.selectbox("Left Eye Acuity", list(self.snellen_chart.keys()), 
                                      key="left_acuity", index=2)
                left_correct = st.slider("Letters correct (Left)", 0, len(self.snellen_chart[left_eye]), 
                                       len(self.snellen_chart[left_eye]), key="left_correct")
                
                st.markdown("#### Right Eye Results")
                right_eye = st.selectbox("Right Eye Acuity", list(self.snellen_chart.keys()), 
                                       key="right_acuity", index=2)
                right_correct = st.slider("Letters correct (Right)", 0, len(self.snellen_chart[right_eye]), 
                                        len(self.snellen_chart[right_eye]), key="right_correct")
                
                if st.button("🔍 Analyze Vision Results", key="analyze_snellen", use_container_width=True):
                    self.analyze_snellen_results(left_eye, right_eye, left_correct, right_correct)
        
        def analyze_snellen_results(self, left_eye, right_eye, left_correct, right_correct):
            st.markdown("### 📈 Vision Test Analysis")
            
            acuity_scores = {
                '20/20': {'category': 'Excellent', 'risk': 'low', 'recommendation': 'Maintain regular eye exams'},
                '20/30': {'category': 'Good', 'risk': 'low', 'recommendation': 'Routine monitoring recommended'},
                '20/40': {'category': 'Fair', 'risk': 'medium', 'recommendation': 'Consider professional evaluation'},
                '20/50': {'category': 'Moderate Impairment', 'risk': 'medium', 'recommendation': 'Schedule eye exam soon'},
                '20/70': {'category': 'Poor', 'risk': 'high', 'recommendation': 'Professional evaluation needed'},
                '20/100': {'category': 'Severe Impairment', 'risk': 'high', 'recommendation': 'Urgent professional care'},
                '20/200': {'category': 'Legal Blindness', 'risk': 'critical', 'recommendation': 'Immediate medical attention'}
            }
            
            col1, col2 = st.columns(2)
            
            with col1:
                left_data = acuity_scores.get(left_eye, {})
                risk_class = f"risk-{left_data.get('risk', 'low')}"
                st.markdown(f'<div class="result-card {risk_class}">', unsafe_allow_html=True)
                st.markdown(f"**👁 Left Eye Analysis**")
                st.markdown(f"**Acuity:** {left_eye}")
                st.markdown(f"**Category:** {left_data.get('category', 'Unknown')}")
                st.markdown(f"**Letters Correct:** {left_correct}/{len(self.snellen_chart[left_eye])}")
                st.markdown(f"**Recommendation:** {left_data.get('recommendation', 'Consult professional')}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                right_data = acuity_scores.get(right_eye, {})
                risk_class = f"risk-{right_data.get('risk', 'low')}"
                st.markdown(f'<div class="result-card {risk_class}">', unsafe_allow_html=True)
                st.markdown(f"**👁 Right Eye Analysis**")
                st.markdown(f"**Acuity:** {right_eye}")
                st.markdown(f"**Category:** {right_data.get('category', 'Unknown')}")
                st.markdown(f"**Letters Correct:** {right_correct}/{len(self.snellen_chart[right_eye])}")
                st.markdown(f"**Recommendation:** {right_data.get('recommendation', 'Consult professional')}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Overall assessment
            if left_correct < 6 or right_correct < 6:
                st.warning("""
                ⚠️ **Reading Difficulty Detected**
                You may have difficulty reading small print. Consider consulting an eye care professional 
                for comprehensive evaluation.
                """)
            
            critical_levels = ['20/70', '20/100', '20/200']
            if left_eye in critical_levels or right_eye in critical_levels:
                st.error("""
                🚨 **Significant Vision Impairment Detected**
                
                Please consult an ophthalmologist or optometrist for proper diagnosis and treatment. 
                Early intervention can help preserve vision.
                """)
            elif left_eye in ['20/40', '20/50'] or right_eye in ['20/40', '20/50']:
                st.info("""
                💡 **Moderate Vision Changes**
                
                Consider scheduling a comprehensive eye exam to assess your vision needs 
                and discuss potential corrective options.
                """)
        
        def grid_vision_test(self):
            st.subheader("🔲 Amsler Grid Test (Central Vision Check)")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### 📋 Instructions for Central Vision Screening:")
                st.markdown("""
                1. **Wear reading glasses** if you normally use them
                2. **Cover one eye** at a time during testing
                3. **Focus on the center dot** with your uncovered eye
                4. **Check carefully** if any lines appear:
                   - Wavy, curved, or distorted
                   - Blurred or missing
                   - Dark areas or spots
                5. **Repeat** for the other eye
                6. **Test in good lighting** conditions
                """)
                
                # Create enhanced Amsler grid
                fig, ax = plt.subplots(figsize=(10, 10))
                
                # Draw main grid
                for i in range(-10, 11):
                    ax.axhline(y=i/10, color='blue', linewidth=1, alpha=0.7)
                    ax.axvline(x=i/10, color='blue', linewidth=1, alpha=0.7)
                
                # Add coordinate markers
                for i in range(-10, 11, 2):
                    ax.text(i/10, 1.05, str(abs(i)), ha='center', va='center', fontsize=8, color='gray')
                    ax.text(-1.05, i/10, str(abs(i)), ha='center', va='center', fontsize=8, color='gray')
                
                # Center dot with crosshairs
                ax.plot(0, 0, 'ro', markersize=10, label='Focus Point')
                ax.axhline(y=0, color='red', linewidth=2, alpha=0.5)
                ax.axvline(x=0, color='red', linewidth=2, alpha=0.5)
                
                ax.set_xlim(-1.1, 1.1)
                ax.set_ylim(-1.1, 1.1)
                ax.set_aspect('equal')
                ax.set_title('Amsler Grid - Central Vision Test', fontsize=16, pad=20)
                ax.axis('off')
                ax.legend(loc='upper right')
                
                st.pyplot(fig, use_container_width=True)
            
            with col2:
                st.markdown("### 📝 Record Observations")
                
                st.markdown("#### 👁 Left Eye")
                left_issues = st.multiselect(
                    "Left Eye - Select all that apply:",
                    ["Straight lines appear wavy", "Blurred areas", "Dark spots", 
                     "Missing lines", "Distorted center", "Everything looks normal"],
                    key="left_grid",
                    default=["Everything looks normal"]
                )
                
                st.markdown("#### 👁 Right Eye")
                right_issues = st.multiselect(
                    "Right Eye - Select all that apply:",
                    ["Straight lines appear wavy", "Blurred areas", "Dark spots", 
                     "Missing lines", "Distorted center", "Everything looks normal"],
                    key="right_grid",
                    default=["Everything looks normal"]
                )
                
                if st.button("🔍 Check Grid Results", key="analyze_grid", use_container_width=True):
                    self.analyze_grid_results(left_issues, right_issues)
        
        def analyze_grid_results(self, left_issues, right_issues):
            st.markdown("### 📊 Grid Test Analysis")
            
            concerning_issues = ["Straight lines appear wavy", "Dark spots", "Missing lines", "Distorted center"]
            warning_issues = ["Blurred areas"]
            
            left_concerning = any(issue in left_issues for issue in concerning_issues)
            right_concerning = any(issue in right_issues for issue in concerning_issues)
            left_warning = any(issue in left_issues for issue in warning_issues)
            right_warning = any(issue in right_issues for issue in warning_issues)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if left_concerning:
                    st.error("""
                    **👁 Left Eye: Concerning Results**
                    
                    Wavy lines, dark spots, or distortions could indicate macular issues.
                    **Recommendation:** Consult an ophthalmologist promptly.
                    """)
                elif left_warning:
                    st.warning("""
                    **👁 Left Eye: Blurriness Detected**
                    
                    Blurred areas should be monitored and evaluated by an eye care professional.
                    """)
                else:
                    st.success("""
                    **👁 Left Eye: Normal Results**
                    
                    No concerning central vision issues detected.
                    """)
            
            with col2:
                if right_concerning:
                    st.error("""
                    **👁 Right Eye: Concerning Results**
                    
                    Wavy lines, dark spots, or distortions could indicate macular issues.
                    **Recommendation:** Consult an ophthalmologist promptly.
                    """)
                elif right_warning:
                    st.warning("""
                    **👁 Right Eye: Blurriness Detected**
                    
                    Blurred areas should be monitored and evaluated by an eye care professional.
                    """)
                else:
                    st.success("""
                    **👁 Right Eye: Normal Results**
                    
                    No concerning central vision issues detected.
                    """)
            
            if left_concerning or right_concerning:
                st.error("""
                🚨 **Important: Possible Macular Issues Detected**
                
                **Immediate Actions Recommended:**
                1. Schedule an appointment with an ophthalmologist
                2. Avoid rubbing your eyes
                3. Monitor for any sudden changes
                4. Consider retinal imaging for proper diagnosis
                
                These symptoms could indicate conditions like macular degeneration that need professional evaluation.
                """)
        
        def eye_disease_symptom_checker(self):
            st.subheader("🏥 Comprehensive Eye Health Assessment")
            
            st.markdown("### 🔍 Symptom Evaluation")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 👁️ Eye Symptoms")
                symptoms = st.multiselect(
                    "Select all symptoms you're experiencing:",
                    [
                        "Redness in eyes", "Eye pain", "Blurred vision", "Double vision",
                        "Floaters or spots", "Flashes of light", "Dry eyes", "Watery eyes",
                        "Sensitivity to light", "Night vision problems", "Halos around lights",
                        "Difficulty reading", "Eye fatigue", "Headaches after visual tasks",
                        "Itchy eyes", "Swollen eyelids", "Discharge from eyes", "None of the above"
                    ],
                    key="symptoms"
                )
            
            with col2:
                st.markdown("#### 🩺 Health Conditions & Risk Factors")
                risk_factors = st.multiselect(
                    "Select applicable risk factors:",
                    [
                        "Diabetes", "High blood pressure", "Family history of glaucoma",
                        "Family history of macular degeneration", "Over 60 years old",
                        "Smoker", "High nearsightedness", "Previous eye injury/surgery",
                        "Autoimmune diseases", "Taking steroid medications", "None"
                    ],
                    key="risk_factors"
                )
                
                age_group = st.selectbox(
                    "Age Group:",
                    ["Under 18", "18-39", "40-59", "60+"]
                )
            
            if st.button("🔍 Analyze My Eye Health", key="analyze_symptoms", use_container_width=True):
                self.analyze_symptoms_risks(symptoms, risk_factors, age_group)
        
        def analyze_symptoms_risks(self, symptoms, risk_factors, age_group):
            st.markdown("### 📋 Comprehensive Health Assessment")
            
            # Emergency symptoms analysis
            emergency_symptoms = ["Eye pain", "Double vision", "Flashes of light", "Sudden vision loss"]
            urgent_symptoms = ["Redness in eyes", "Blurred vision", "Floaters or spots", "Halos around lights"]
            
            has_emergency = any(symptom in symptoms for symptom in emergency_symptoms)
            has_urgent = any(symptom in symptoms for symptom in urgent_symptoms)
            
            # Risk assessment
            risk_score = 0
            high_risk_factors = ["Diabetes", "Family history of glaucoma", "Family history of macular degeneration"]
            medium_risk_factors = ["High blood pressure", "Over 60 years old", "High nearsightedness"]
            
            for factor in risk_factors:
                if factor in high_risk_factors:
                    risk_score += 3
                elif factor in medium_risk_factors:
                    risk_score += 2
                else:
                    risk_score += 1
            
            # Display results
            if has_emergency:
                st.error("""
                🚨 **EMERGENCY: Seek Immediate Medical Attention**
                
                **Critical Symptoms Detected:**
                - These symptoms could indicate retinal detachment, acute glaucoma, or other serious conditions
                - Do not wait - visit emergency room or eye specialist immediately
                - Avoid driving yourself to the hospital
                
                **Conditions to Rule Out:**
                • Retinal detachment
                • Acute angle-closure glaucoma  
                • Optic neuritis
                • Stroke-related vision issues
                """)
            
            elif has_urgent:
                st.warning("""
                ⚠️ **URGENT: Schedule Eye Exam Within 1-2 Weeks**
                
                **Concerning Symptoms Detected:**
                - These symptoms require prompt professional evaluation
                - Contact an ophthalmologist or optometrist soon
                - Monitor for any worsening symptoms
                
                **Potential Conditions:**
                • Macular degeneration
                • Diabetic retinopathy
                • Cataracts
                • Glaucoma
                """)
            
            elif symptoms and "None of the above" not in symptoms:
                st.info("""
                💡 **Recommendation: Schedule Routine Eye Exam**
                
                **Mild to Moderate Symptoms:**
                - Regular eye exams are important for maintaining eye health
                - Consider scheduling within the next 1-3 months
                - Monitor symptoms for any changes
                
                **Preventive Care:**
                • Comprehensive dilated eye exam
                • Vision acuity testing
                • Eye pressure measurement
                """)
            else:
                st.success("""
                ✅ **No Concerning Symptoms Reported**
                
                **Maintenance Recommendations:**
                - Continue with regular eye exams based on your age and risk factors
                - Practice good eye hygiene and protection
                - Maintain healthy lifestyle habits
                """)
            
            # Risk factor analysis
            st.markdown("### 🎯 Risk Factor Analysis")
            
            if risk_score >= 6:
                st.error(f"""
                **HIGH RISK PROFILE** (Score: {risk_score})
                
                Due to your risk factors, more frequent comprehensive eye exams are recommended:
                - Annual dilated eye exams
                - Regular monitoring of specific risk conditions
                - Early intervention if needed
                """)
            elif risk_score >= 3:
                st.warning(f"""
                **MODERATE RISK PROFILE** (Score: {risk_score})
                
                Regular eye examinations every 1-2 years are recommended:
                - Comprehensive eye health evaluation
                - Baseline measurements for future comparison
                - Preventive care discussions
                """)
            else:
                st.success(f"""
                **LOW RISK PROFILE** (Score: {risk_score})
                
                Standard eye examination schedule is appropriate:
                - Every 2 years for adults under 60
                - Annual exams recommended for adults 60+
                """)
        
        def generate_report(self):
            st.subheader("📋 Comprehensive Eye Health Report")
            
            # User information
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🎯 Personalized Recommendations")
                st.markdown("""
                **Based on Your Assessment:**
                
                ✅ **Regular Monitoring:**
                - Monthly self-check using provided tests
                - Note any vision changes in a diary
                - Compare results over time
                
                ✅ **Professional Care:**
                - Schedule comprehensive eye exams regularly
                - Discuss family history with your eye doctor
                - Keep updated prescription if needed
                
                ✅ **Lifestyle Habits:**
                - Wear UV-protected sunglasses outdoors
                - Follow 20-20-20 rule for screen time
                - Maintain balanced diet rich in antioxidants
                - Stay hydrated for eye moisture
                - Avoid smoking
                """)
            
            with col2:
                st.markdown("### 🚨 When to Seek Immediate Care")
                st.markdown("""
                **Emergency Symptoms:**
                - Sudden vision loss or blurring
                - Severe eye pain or injury
                - Flashes of light or new floaters
                - Double vision or distorted vision
                - Halos around lights with pain
                - Redness with pain and vision changes
                
                **Urgent Concerns:**
                - Gradual vision changes
                - Persistent eye discomfort
                - Chronic dry eyes affecting daily life
                - Family history of eye diseases
                """)
                
                st.markdown("### 📞 Resources")
                st.markdown("""
                - American Academy of Ophthalmology
                - National Eye Institute
                - Local ophthalmology clinics
                - Emergency eye care services
                """)
            
            # Generate downloadable report
            if st.button("📄 Generate Detailed Report", key="download_report", use_container_width=True):
                report_content = self._create_detailed_report()
                
                st.download_button(
                    label="⬇️ Download Full Report",
                    data=report_content,
                    file_name=f"eye_health_report_{datetime.now().strftime('%Y%m%d')}.txt",
                    mime="text/plain",
                    key="final_download"
                )
        
        def _create_detailed_report(self):
            report = f"""
            COMPREHENSIVE EYE HEALTH REPORT
            Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}
            
            =============================================
            IMPORTANT: EDUCATIONAL TOOL ONLY
            This report is for informational purposes only
            and does not replace professional medical advice.
            Always consult qualified eye care professionals.
            =============================================
            
            RECOMMENDATIONS:
            
            1. PROFESSIONAL EYE CARE:
            - Regular comprehensive eye examinations
            - Age-appropriate screening schedules
            - Discussion of family history and risk factors
            
            2. DAILY EYE HEALTH PRACTICES:
            - 20-20-20 Rule: Every 20 minutes, look 20 feet away for 20 seconds
            - Proper lighting for reading and screen work
            - UV protection with quality sunglasses
            - Eye protection during sports and hazardous activities
            
            3. NUTRITION AND LIFESTYLE:
            - Diet rich in leafy greens, colorful fruits and vegetables
            - Omega-3 fatty acids for dry eye management
            - Adequate hydration
            - Smoking cessation
            - Blood pressure and diabetes management
            
            4. MONITORING AND SELF-CARE:
            - Monthly vision self-checks
            - Prompt reporting of vision changes
            - Proper contact lens hygiene if applicable
            - Regular cleaning of glasses
            
            EMERGENCY PROTOCOLS:
            - Sudden vision changes: Seek immediate care
            - Eye injuries: Do not rub, seek emergency care
            - Chemical exposures: Flush with water and seek care
            - Persistent pain or redness: Professional evaluation needed
            
            =============================================
            REMEMBER: Early detection saves vision.
            Regular professional eye care is essential
            for maintaining lifelong eye health.
            =============================================
            """
            return report

    # Initialize session state
    checker = EyeHealthChecker()
    checker._initialize_session_state()

    # Main application
    st.markdown('<h1 class="main-header">Comprehensive Eye Health Checker 👁️</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center;'>
    <h3 style='color: #1f77b4; margin-top: 0;'>Welcome to Your Personal Eye Health Assessment</h3>
    <p>
    This comprehensive tool helps you monitor your eye health through scientifically-validated screening methods. 
    Track your vision quality, identify potential issues early, and maintain optimal eye health throughout your life.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # st.warning("""
    # **⚠️ Important Medical Disclaimer:** 
    # This application is an educational self-assessment tool only. It is not a substitute for professional medical advice, 
    # diagnosis, or treatment. Always seek the advice of qualified eye care professionals with any questions you may have 
    # regarding medical conditions.
    # """)
    
    # Create navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏠 Dashboard", 
        "👁️ Vision Test", 
        "🔲 Grid Test", 
        "🏥 Health Check"
    ])
    
    with tab1:
        st.markdown("""
        ## 🎯 Eye Health Monitoring Dashboard
        
        ### Available Assessments:
        
        **🔤 Visual Acuity Test** 
        - Measure distance vision clarity
        - Compare against standard Snellen chart
        - Track changes over time
        
        **🔲 Amsler Grid Test** 
        - Screen for central vision problems
        - Detect macular degeneration signs
        - Monitor for distortions
        
        **🏥 Comprehensive Health Assessment**
        - Evaluate symptoms and risk factors
        - Personalized recommendations
        - Professional referral guidance
        
        ### 📊 Why Regular Monitoring Matters:
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Early Detection**
            - 80% of vision impairment is preventable
            - Regular screening catches issues early
            - Better treatment outcomes
            """)
        
        with col2:
            st.markdown("""
            **Preventive Care**
            - Monitor age-related changes
            - Track vision stability
            - Identify risk factors
            """)
        
        with col3:
            st.markdown("""
            **Health Awareness**
            - Understand eye health basics
            - Learn warning signs
            - Make informed decisions
            """)
        
        st.info("👆 **Select the test tabs above to begin your comprehensive eye health assessment**")
    
    with tab2:
        with st.container():
            st.markdown('<div class="test-section">', unsafe_allow_html=True)
            checker.snellen_test()
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        with st.container():
            st.markdown('<div class="test-section">', unsafe_allow_html=True)
            checker.grid_vision_test()
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        with st.container():
            st.markdown('<div class="test-section">', unsafe_allow_html=True)
            checker.eye_disease_symptom_checker()
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Report generation section
    st.markdown("---")
    checker.generate_report()
    
    # Enhanced footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <h4>🔬 Evidence-Based Eye Health Monitoring</h4>
        <p>Educational Tool Only • Not for Medical Diagnosis • Always Consult Eye Care Professionals</p>
        <p style='font-size: 0.8em;'>Regular comprehensive eye exams are essential for maintaining vision health throughout life.</p>
    </div>
    """, unsafe_allow_html=True)

# Run the application
if __name__ == "__main__":
    ankhen()