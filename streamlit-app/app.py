import streamlit as st
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Apply custom styles using st.markdown for CSS
st.markdown("""
    <style>
        /* Background color */
        .stApp {
            background-color: #f7f7f7;
        }

        /* Title styling */
        h1 {
            color: #f64c72;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-top: -50px;
        }

        /* Input box styling */
        input {
            background-color: #fffcf5;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #ccc;
        }

        /* Button styling */
        button {
            background-color: #ff686b;
            border: none;
            border-radius: 12px;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
        }

        /* Footer styling */
        .footer {
            text-align: center;
            font-size: 14px;
            padding: 20px;
            background-color: #ff686b;
            color: white;
            border-radius: 10px;
            margin-top: 50px;
        }

        .footer a {
            color: #ffe75e;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Set the title and description
st.markdown("<h1>🔍 Duplicate Question Pair Detector</h1>", unsafe_allow_html=True)
st.markdown("""
    <p style="text-align:center; font-size:18px; color:#444;">
        Enter two questions below, and we'll check if they are duplicates using machine learning.
    </p>
""", unsafe_allow_html=True)

# Input areas for the questions with some spacing
q1 = st.text_input('❓ Enter Question 1', placeholder="Type your first question here...")
q2 = st.text_input('❓ Enter Question 2', placeholder="Type your second question here...")

# Center the button
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

# Button to trigger the model prediction
if st.button('🚀 Check for Duplicates'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    # Display result with better formatting and colors
    if result:
        st.markdown("""
            <div style="text-align:center;">
                <h2 style='color:#2ecc71;'>✅ These questions are duplicates.</h2>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align:center;">
                <h2 style='color:#e74c3c;'>❌ These questions are not duplicates.</h2>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Adding footer with links and space
# st.markdown("""
#     <div class="footer">
#         Made with ❤️ using <a href="https://streamlit.io/" target="_blank">Streamlit</a>
#     </div>
# """, unsafe_allow_html=True)