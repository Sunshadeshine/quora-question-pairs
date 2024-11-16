import streamlit as st
import helper
import pickle
from streamlit_extras.switch_page_button import switch_page
from time import sleep

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Initialize session state for question history
if "history" not in st.session_state:
    st.session_state.history = []

# Apply custom styles
st.markdown("""
    <style>
        /* Background and Theme */
        .stApp {
            background: linear-gradient(135deg, #2a5298, #1e3c72);
            color: white;
            font-family: 'Inter', sans-serif;
        }

        /* Title */
        h1 {
            font-size: 3.8em;
            font-weight: 900;
            text-align: center;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        /* Description */
        p {
            font-size: 1.2em;
            text-align: center;
            margin-bottom: 30px;
            color: #ffffff;
        }

        /* Input Boxes */
        .stTextInput > div > input {
            height: 55px;
            font-size: 1.5em;
            border-radius: 12px;
            padding: 15px;
        }

        /* Buttons */
        .stButton button {
            background: linear-gradient(90deg, #ff6a00, #ee0979);
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            padding: 15px 25px;
            margin: 20px 0;
        }

        .stButton button:hover {
            transform: scale(1.1);
            box-shadow: 0px 4px 10px rgba(255, 105, 135, 0.4);
        }

        /* Result Box */
        .result-box {
            text-align: center;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            font-size: 1.5em;
            margin-top: 30px;
            animation: fadeIn 1s ease-in-out;
        }

        /* Fade-in Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Floating Button */
        .floating-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(90deg, #ff6a00, #ee0979);
            color: white;
            padding: 15px;
            border-radius: 50%;
            font-size: 1.5em;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            z-index: 1000;
        }

        .floating-btn:hover {
            transform: scale(1.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🔍 AI-Powered Question Similarity Checker</h1>", unsafe_allow_html=True)
st.markdown("<p>Quickly detect question similarities with accuracy and ease.</p>", unsafe_allow_html=True)

# Input areas for questions
q1 = st.text_input('❓ Enter Question 1', placeholder="Type your first question here...")
q2 = st.text_input('❓ Enter Question 2', placeholder="Type your second question here...")

# Analyze button with a loading spinner
if st.button('🚀 Analyze'):
    if q1 and q2:
        with st.spinner('Analyzing questions...'):
            sleep(1.5)  # Simulate processing time
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

        # Store to history
        st.session_state.history.append((q1, q2, result))

        # Display the result
        if result:
            st.markdown("""
                <div class="result-box">
                    ✅ <strong>These questions are duplicates.</strong>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="result-box">
                    ❌ <strong>These questions are not duplicates.</strong>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Please enter both questions before analyzing.")

# Question history
if st.session_state.history:
    st.markdown("### Recently Analyzed Questions")
    for idx, (question1, question2, result) in enumerate(st.session_state.history[-5:]):
        result_text = "✅ Duplicate" if result else "❌ Not Duplicate"
        st.write(f"{idx+1}. *Q1:* {question1} | *Q2:* {question2} → {result_text}")

# Floating Help Button
st.markdown("""
    <div class="floating-btn" onclick="window.open('https://support.yourcompany.com', '_blank')">
        ❔
    </div>
""", unsafe_allow_html=True)