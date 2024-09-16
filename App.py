import streamlit as st
from transformers import pipeline
import emoji

# Set up the Hugging Face sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Function to map labels to human-readable sentiment
def get_sentiment_label(label):
    if label == "LABEL_0":
        return "Negative", "😢"
    elif label == "LABEL_1":
        return "Neutral", "😐"
    elif label == "LABEL_2":
        return "Positive", "😊"

# Custom CSS for desktop and mobile responsiveness
st.markdown(
    """
    <style>
    /* Global Styling */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #F9F9F9;
    }
    /* Header Styling */
    .header {
        font-size: 3vw; /* Scales with viewport width */
        font-weight: 600;
        color: #4A90E2;
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px 8px #aaa;
    }
    /* Subheader Styling */
    .subheader {
        font-size: 1.5vw; /* Scales with viewport width */
        color: #333;
        text-align: center;
        margin-bottom: 30px;
        padding: 0 20px;
        line-height: 1.5;
    }
    /* Sentiment box responsive style */
    .sentiment-box {
        background-color: #E3F2FD;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
        max-width: 50%; /* Responsive width */
        margin-left: auto;
        margin-right: auto;
    }
    /* Textarea style */
    textarea {
        width: 100%;
        font-size: 16px;
    }
    /* Button Style */
    button {
        background-color: #4A90E2;
        color: white;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        max-width: 300px; /* Fixed max width for button */
        margin: 10px auto;
        display: block;
    }
    button:hover {
        background-color: #357ABD;
    }
    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4A90E2;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #FFFFFF;
        text-decoration: none;
        font-weight: bold;
    }
    /* Link hover effects */
    .footer a:hover {
        color: #FFD700; /* Gold hover color */
        text-decoration: underline;
    }
    .footer p {
        margin: 5px 0;
    }
    /* Media Queries for mobile devices */
    @media screen and (max-width: 600px) {
        .header {
            font-size: 7vw;
        }
        .subheader {
            font-size: 5vw;
        }
        .sentiment-box {
            max-width: 90%;
        }
        button {
            font-size: 16px;
            padding: 10px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Subheader with responsive typography
st.markdown('<p class="header">Twitter Sentiment Analysis</p>', unsafe_allow_html=True)
st.markdown(
    '''
    <p class="subheader">
    Analyze sentiments using the pre-trained model <strong>cardiffnlp/twitter-roberta-base-sentiment</strong>. 
    This RoBERTa-based model is fine-tuned on Twitter data to capture the informal language of social media, categorizing tweets into Positive, Neutral, or Negative sentiments.
    </p>
    ''',
    unsafe_allow_html=True
)

# Input section with responsive design
input_text = st.text_area("Enter a tweet or text for sentiment analysis:", height=100)

# Add interactivity for the button with hover effect and responsiveness
if st.button("Analyze Sentiment"):
    if input_text:
        # Perform sentiment analysis
        result = sentiment_analysis(input_text)[0]
        label = result['label']
        score = result['score']

        # Map label to sentiment and emoji
        sentiment, emoji_icon = get_sentiment_label(label)

        # Display result
        st.markdown(
            f"""
            <div class="sentiment-box">
                <h3><b>Sentiment:</b> {sentiment} {emoji_icon}</h3>
                <h4><b>Confidence Score:</b> {score:.2f}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Please enter a tweet or text for analysis.")

# Footer with LinkedIn and GitHub links, mobile-friendly and interactive
st.markdown(
    """
    <div class="footer">
        <p>Developed with ❤️ by <a href="https://www.linkedin.com/in/muhammad-nadeem-5a1517242/" target="_blank">Muhammad Nadeem</a></p>
        <p>Find the code on <a href="https://github.com/NadeemMughal" target="_blank">GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

