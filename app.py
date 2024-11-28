import sys
import os
import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

# Add the path to the src folder containing textSummarizer
sys.path.append(os.path.abspath('src'))

# Set up the page configuration for a full-screen layout
st.set_page_config(page_title="Text Summarizer", layout="wide")

# Custom CSS for styling the page
st.markdown("""
    <style>
        /* Full screen and centered content */
        .css-ffhzg2 {
            max-width: 100% !important;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Title and header styling */
        h1 {
            font-size: 4rem;
            color: #4CAF50;
            font-weight: 700;
            text-align: center;
        }

        /* Custom description styling */
        .description {
            font-size: 1.2rem;
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }

        /* Styling for input area */
        .stTextInput, .stTextArea {
            font-size: 1.2rem;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #4CAF50;
            width: 100%;
            max-width: 800px;
            margin-bottom: 20px;
        }

        /* Button styling */
        .stButton {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 1.2rem;
            width: 100%;
            max-width: 200px;
            margin: 20px auto;
        }

        /* Styling for the output box */
        .output {
            font-size: 1.2rem;
            color: #555;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            max-width: 800px;
            margin: 20px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Warning and error styling */
        .stWarning, .stError {
            font-size: 1.2rem;
            text-align: center;
            color: #d32f2f;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Text Summarization Tool")

# Description
st.markdown("""
    <div class="description">
        This tool allows you to summarize any text you input.
        Just type or paste your text in the box below, click the "Summarize Text" button, and get the summarized version.
    </div>
""", unsafe_allow_html=True)

# Text input area for summarization
input_text = st.text_area("Enter text here:", height=200, placeholder="Type or paste your text here...")

# When the button is clicked, run prediction
if st.button("Summarize Text"):
    if input_text.strip():
        try:
            # Predict the summary using your existing pipeline
            obj = PredictionPipeline()
            summary = obj.predict(input_text)
            
            # Display the result in a styled output box
            st.subheader("Summarized Text:")
            st.markdown(f'<div class="output">{summary}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error occurred during summarization: {e}")
    else:
        st.warning("Please enter some text to summarize.")
