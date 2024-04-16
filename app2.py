import google.generativeai as genai
from PIL import Image
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 10000,
}


def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image, prompt])
    return response.text


# initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")
st.header("🌿 Smart Plant Disease Analyzer using Gemini 👨🏻‍💻")

uploaded_file = st.file_uploader("Choose and Image", accept_multiple_files=False, type=[
    "png", "jpg", "jpeg", "img", "webp"])

input = st.text_input("Input Prompt: ", key="input")


submit = st.button("Tell me about the  image")

input_prompt = """
Access and process information from the internet to analyze the uploaded image of a plant. Identify the most likely disease or issue affecting the plant based on the visual symptoms and any additional information provided by the farmer.

Generate a step-by-step guide for the farmer, written in clear and concise language, that includes:

Disease Identification: State the most likely disease or issue affecting the plant.
Symptom Breakdown: Describe the key symptoms observed in the image and how they relate to the identified disease.
Preventative Measures: List actionable steps the farmer can take to prevent the spread of the disease to other plants.
Treatment Options: Outline readily available treatment options for the farmer, prioritizing organic solutions whenever possible. Include instructions for application (if applicable).
Further Assistance: Provide contact information for a local agricultural extension office or relevant helpline for the farmer to consult a plant specialist if needed.
Provide correct links to websites

               """

# If ask button is clicked


if submit:
    image = Image.open(uploaded_file)
    response = get_gemini_response(input_prompt, image, input)
    st.write(response)
