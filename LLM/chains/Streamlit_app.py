import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# App Title
st.title("Gemini AI Chain Selector")
st.markdown("Choose a type of AI workflow to run.")

# Dropdown to select chain
option = st.selectbox("Choose a Chain Type", [
    "Simple Chain: Topic → 5 Interesting Facts",
    "Sequential Chain: Report + Summary",
    "Conditional Chain: Feedback Sentiment Response"
])

st.divider()

# 1. Simple Chain
if option.startswith("Simple Chain"):
    topic = st.text_input("Enter a Topic:", "cricket")
    if st.button("Generate Facts"):
        prompt = f"Generate 5 interesting facts about {topic}."
        response = model.generate_content(prompt)
        st.subheader("Generated Facts:")
        st.write(response.text)

# 2. Sequential Chain
elif option.startswith("Sequential Chain"):
    topic = st.text_input("Enter a Topic:", "Unemployment in India")
    if st.button("Generate Report and Summary"):
        with st.spinner("Generating report..."):
            report_prompt = f"Generate a detailed report on {topic}."
            report = model.generate_content(report_prompt).text

        with st.spinner("Summarizing..."):
            summary_prompt = f"Generate a 5 pointer summary from the following text:\n\n{report}"
            summary = model.generate_content(summary_prompt).text

        st.subheader("Summary:")
        st.write(summary)

# 3. Conditional Chain
elif option.startswith("Conditional Chain"):
    feedback = st.text_area("Enter Feedback:", "This phone is amazing and works smoothly.")
    if st.button("Classify and Respond"):
        sentiment_prompt = f"Classify the sentiment of the following feedback as positive or negative only:\n\n{feedback}"
        sentiment = model.generate_content(sentiment_prompt).text.strip().lower()

        if "positive" in sentiment:
            response_prompt = f"Write an appropriate response to this positive feedback:\n\n{feedback}"
        elif "negative" in sentiment:
            response_prompt = f"Write an appropriate response to this negative feedback:\n\n{feedback}"
        else:
            response_prompt = "Could not determine the sentiment."

        if "feedback" in response_prompt:
            reply = model.generate_content(response_prompt).text
            st.subheader("Detected Sentiment:")
            st.success(sentiment.capitalize())
            st.subheader("Response:")
            st.write(reply)
        else:
            st.error(response_prompt)
