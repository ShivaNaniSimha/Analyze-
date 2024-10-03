import streamlit as st
from PIL import Image
import google.generativeai as genai
from key import gemini_api_key

# Streamlit app
st.title("Image Analysis")

    # Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    img = Image.open(uploaded_file)
            # Display the image
    st.image(img, caption='Uploaded Image', use_column_width=True)
    if img:
        try:
            genai.configure(api_key=gemini_api_key)

            model = genai.GenerativeModel('gemini-1.5-flash')
            response=model.generate_content(["analyze the picture and give me the details in brief",img],stream=False)
            for responses in response:
                st.write(responses.text)
        except Exception as error:
            st.write("there seems to be a problem please do not leave the page!")
    else:
        st.write("please upload the file")
