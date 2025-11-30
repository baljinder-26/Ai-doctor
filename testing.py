import streamlit as st
import base64
import time
#https://lottie.host/961c5b72-2a4f-4628-b4e1-bd0557972b2b/kclaamX7MU.json
# ==================== CHATBOT POPUP WINDOW ====================

# Custom CSS for popup chat window
st.markdown("""
<style>
.chat-icon {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #1f77b4, #0288D1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    z-index: 1000;
    border: 3px solid white;
    transition: transform 0.3s ease;
}
.chat-icon:hover {
    transform: scale(1.1);
}
.chat-window {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 350px;
    height: 500px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    z-index: 1001;
    border: 2px solid #e3f2fd;
    display: none;
    flex-direction: column;
}
.chat-window.active {
    display: flex;
}
.chat-header {
    background: linear-gradient(135deg, #1f77b4, #0288D1);
    color: white;
    padding: 15px;
    border-radius: 15px 15px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.chat-header h3 {
    margin: 0;
    font-size: 16px;
}
.close-btn {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    padding: 0;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.close-btn:hover {
    background: rgba(255,255,255,0.2);
}
.chat-messages {
    flex: 1;
    padding: 15px;
    overflow-y: auto;
    background: #fafafa;
}
.chat-input-container {
    padding: 15px;
    border-top: 1px solid #e0e0e0;
    background: white;
    border-radius: 0 0 15px 15px;
}
.emergency-alert {
    background-color: #ffebee;
    border-left: 5px solid #f44336;
    padding: 10px;
    border-radius: 5px;
    margin: 5px 0;
    font-size: 12px;
}
.chat-message {
    margin: 8px 0;
    padding: 10px;
    border-radius: 10px;
    font-size: 14px;
    max-width: 80%;
}
.user-message {
    background: #e3f2fd;
    margin-left: auto;
    text-align: right;
}
.ai-message {
    background: white;
    border: 1px solid #e0e0e0;
    margin-right: auto;
}
.message-time {
    font-size: 10px;
    color: #666;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# Medical avatar
medical_ai_svg = '''
<svg width="30" height="30" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="40" r="25" fill="#ffffff" stroke="#1565C0" stroke-width="2"/>
    <rect x="45" y="25" width="10" height="20" fill="#1f77b4"/>
    <rect x="40" y="30" width="20" height="10" fill="#1f77b4"/>
    <circle cx="42" cy="35" r="3" fill="#1f77b4"/>
    <circle cx="58" cy="35" r="3" fill="#1f77b4"/>
    <rect x="40" y="65" width="20" height="25" rx="5" fill="#ffffff" stroke="#1565C0" stroke-width="2"/>
    <path d="M 35 80 Q 40 75, 45 80 Q 50 85, 55 80 Q 60 75, 65 80" 
          stroke="#1f77b4" stroke-width="2" fill="none"/>
</svg>
'''
medical_avatar = f"data:image/svg+xml;base64,{base64.b64encode(medical_ai_svg.encode()).decode()}"

# Initialize chat session
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hello! I'm AI Doctor. How can I help you today?", "is_emergency": False, "time": "Now"}
    ]

# Response logic
def get_ai_response(user_message):
    user_message_lower = user_message.lower()
    
    emergency_words = ['chest pain', 'difficulty breathing', 'severe bleeding', 'unconscious', 'can\'t breathe', 'crushing pain']
    if any(word in user_message_lower for word in emergency_words):
        return "🚨 **URGENT**: These symptoms may indicate a serious condition. Please seek immediate medical attention!", True
    
    if any(word in user_message_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm AI Doctor. I'm here to help assess your symptoms. Please describe what you're experiencing.", False
    elif any(word in user_message_lower for word in ['hurt', 'pain', 'ache']):
        return "I understand you're in pain. Can you describe the location, type of pain, and severity (1-10)?", False
    elif any(word in user_message_lower for word in ['fever', 'temperature']):
        return "Fever can indicate various conditions. What's your temperature? How long have you had it?", False
    elif any(word in user_message_lower for word in ['headache']):
        return "Headaches can have various causes. Where is the pain located? Is it constant or intermittent?", False
    elif any(word in user_message_lower for word in ['thank', 'thanks']):
        return "You're welcome! Is there anything else I can help you with today?", False
    else:
        return "Thank you for sharing. Could you provide more details about your symptoms and their duration?", False

# Toggle chat function
def toggle_chat():
    st.session_state.chat_open = not st.session_state.chat_open

# Add timestamp to messages
def get_current_time():
    return time.strftime("%H:%M")

# Display chat icon and window
col1, col2 = st.columns([1, 1])
with col2:
    if st.button("🩺", help="Chat with AI Doctor", key="chat_icon"):
        toggle_chat()

# Chat window content
if st.session_state.chat_open:
    # Create an overlay effect
    st.markdown("""
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.1); z-index: 999;">
    </div>
    """, unsafe_allow_html=True)
    
    # Chat window
    st.markdown("""
    <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                width: 400px; height: 600px; background: white; border-radius: 15px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 1000; border: 2px solid #e3f2fd;">
        <div style="background: linear-gradient(135deg, #1f77b4, #0288D1); color: white; 
                    padding: 20px; border-radius: 15px 15px 0 0; display: flex; 
                    justify-content: space-between; align-items: center;">
            <h3 style="margin: 0;">🩺 AI Doctor</h3>
            <button onclick="window.parent.document.querySelector('button[kind=secondary]').click()" 
                    style="background: none; border: none; color: white; font-size: 20px; 
                           cursor: pointer; padding: 5px 10px; border-radius: 50%;">
                ×
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Chat interface in the main area (simplified)
if st.session_state.chat_open:
    st.markdown("### 💬 AI Doctor Chat")
    st.info("💡 Describe your symptoms and get medical guidance")
    
    # Display messages
    for msg in st.session_state.chat_messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style="background: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0; margin-left: 50px;">
                <div>{msg['content']}</div>
                <div style="font-size: 10px; color: #666; text-align: right;">{msg.get('time', '')}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            if msg.get('is_emergency'):
                st.markdown(f"""
                <div style="background: #ffebee; border-left: 5px solid #f44336; padding: 10px; 
                            border-radius: 5px; margin: 5px 0; margin-right: 50px;">
                    <div>{msg['content']}</div>
                    <div style="font-size: 10px; color: #666;">{msg.get('time', '')}</div>
                </div>
                """, unsafe_allow_html=True)
                st.error("🚨 PLEASE SEEK IMMEDIATE MEDICAL ATTENTION!")
            else:
                st.markdown(f"""
                <div style="background: white; border: 1px solid #e0e0e0; padding: 10px; 
                            border-radius: 10px; margin: 5px 0; margin-right: 50px;">
                    <div>{msg['content']}</div>
                    <div style="font-size: 10px; color: #666;">{msg.get('time', '')}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input form
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area("Your message:", placeholder="Describe your symptoms...", height=80)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            send_btn = st.form_submit_button("📤 Send")
        with col2:
            clear_btn = st.form_submit_button("🗑️ Clear")
        with col3:
            close_btn = st.form_submit_button("❌ Close")
    
    if send_btn and user_input.strip():
        # Add user message
        st.session_state.chat_messages.append({
            "role": "user", 
            "content": user_input,
            "time": get_current_time()
        })
        
        # Get AI response
        with st.spinner("AI Doctor is analyzing..."):
            time.sleep(1)
            ai_response, is_emergency = get_ai_response(user_input)
            st.session_state.chat_messages.append({
                "role": "assistant", 
                "content": ai_response, 
                "is_emergency": is_emergency,
                "time": get_current_time()
            })
        
        st.rerun()
    
    if clear_btn:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I'm AI Doctor. How can I help you today?", "is_emergency": False, "time": "Now"}
        ]
        st.rerun()
    
    if close_btn:
        st.session_state.chat_open = False
        st.rerun()

# Simple chat icon for when chat is closed
if not st.session_state.chat_open:
    st.markdown(f"""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
        <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #1f77b4, #0288D1); 
                    border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                    cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 3px solid white;"
             onclick="window.parent.document.querySelector('button[kind=secondary]').click()">
            <img src="{medical_avatar}" width="30" height="30">
        </div>
    </div>
    """, unsafe_allow_html=True)

# Close chat button (hidden but functional)
if st.session_state.chat_open:
    if st.button("Close Chat", key="close_chat_btn"):
        st.session_state.chat_open = False
        st.rerun()

# Disclaimer
st.markdown("---")
st.caption("💡 **Click the AI Doctor icon in the bottom-right to chat!**")
st.caption("**Disclaimer:** AI assistant for guidance only. Always consult healthcare professionals for medical conditions.")