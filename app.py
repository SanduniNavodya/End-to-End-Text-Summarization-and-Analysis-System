import sys
import os

# Add the path to the src folder containing textSummarizer
sys.path.append(os.path.abspath('src'))

import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

# Set up the page configuration for full-screen layout
st.set_page_config(page_title="Text Summarizer", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Title styling */
        h1 {
            text-align: center;
            color: #4CAF50;
            font-size: 3rem;
            margin-bottom: 20px;
        }

        /* Centered description */
        .description {
            text-align: center;
            font-size: 1.5rem;
            color: rgba(127, 140, 141, 0.8); 
            font-weight: semi-bold; 
            margin-bottom: 30px;
        }

        /* Text area styling */
        textarea {
            width: 100%;
            height: 300px !important;
            font-size: 1.2rem;
            border: 2px solid #2ECC71;
            border-radius: 8px;
            padding: 15px;
            background: #F4F6F7;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Output box styling */
        .output-box {
            width: 100%;
            height: 300px;
            font-size: 1.2rem;
            border: 2px solid #2ECC71;
            border-radius: 8px;
            padding: 15px;
            background: #ECF0F1;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
            color: #2C3E50;
            margin-top: 27px; /* Adds space before the box */
        }

        /* Button styling */
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px !important;
            font-size: 1.2rem;
            cursor: pointer;
            
        }

        /* Center button at the bottom */
        .center-button {
            display: flex;
            justify-content: center;
            position: fixed;
            left: 0;
            right: 0;
            bottom: 20px; /* Adjust as needed for spacing from the bottom */
            padding: 10px;
            background-color: transparent;
            
        }

        .stButton button:hover {
            background-color: #45A049 !important;
        }

        /* Warning and error messages */
        .stWarning, .stError {
            text-align: center;
            color: #E74C3C;
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Text Summarization Tool")

# Description
st.markdown("""
    <div class="description">
        This tool allows you to summarize any text you input. 
        Just type or paste your text in the box on the left, and view the summarized version on the right. Click the "Summarize Text" button at the bottom to generate the summary.
    </div>
""", unsafe_allow_html=True)

# Create two columns for input and output
col1, col2 = st.columns(2)

# Input column
with col1:
    st.subheader("Enter Text")
    input_text = st.text_area("Input your text here:", placeholder="Type or paste your text here...")

# Output column
with col2:
    st.subheader("Summarized Text")
    summary_placeholder = st.empty()  # Placeholder for the output box
    summary_placeholder.markdown('<div class="output-box"></div>', unsafe_allow_html=True)

# Add a fixed bottom button centered in the container
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button("Summarize Text"):
    if input_text.strip():
        try:
            # Predict the summary using your existing pipeline
            obj = PredictionPipeline()
            summary = obj.predict(input_text)

            # Update the summary output box
            summary_placeholder.markdown(f'<div class="output-box">{summary}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error occurred during summarization: {e}")
    else:
        st.warning("Please enter some text to summarize.")
st.markdown('</div>', unsafe_allow_html=True)
