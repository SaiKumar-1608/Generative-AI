import streamlit as st
from ctransformers import AutoModelForCausalLM

# Title
st.title("Llama-2 GGUF Chatbot")
#st.subheader("Chat with an AI model locally!")
# Load GGUF Model (Ensure model file is in the same directory or provide a full path)
@st.cache_resource
def load_model():
    model_path = "C:/Users/arpan.ghosh/Documents/Modulr/Teaching_Project/llama-2-7b-chat.Q4_K_M.gguf"  # Update if necessary
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="llama",  # Use "mistral" if using a Mistral model
        gpu_layers=0  # Set to 0 for CPU-only
    )
    return model
model = load_model()

# User Input
user_input = st.text_area(" Enter your message:", placeholder="Type something...")

if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Thinking... "):
            response = model(user_input)
            st.success(" AI Response:")
            st.write(response)
    else:
        st.warning(" Please enter some text before generating a response.")