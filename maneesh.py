import streamlit as st
import time
from pathlib import Path
import base64

# Set page configuration
st.set_page_config(page_title="Maneesh", layout="centered")

# Path to the image
current_dir = Path(__file__).parent
background_image = current_dir / "maneesh.jpeg"

# Encode image to base64
with open(background_image, "rb") as f:
    image_bytes = f.read()
encoded_image = base64.b64encode(image_bytes).decode()

# Set background image and custom CSS styles
st.markdown(f"""
    <style>
    .stApp {{
    background-image: url("data:image/jpeg;base64,{encoded_image}");
    background-size: cover;
    background-position: center;
    }}
    @keyframes rainbow {{
      0% {{color: red;}}
      14% {{color: orange;}}
      28% {{color: yellow;}}
      42% {{color: green;}}
      57% {{color: blue;}}
      71% {{color: indigo;}}
      85% {{color: violet;}}
      100% {{color: red;}}
    }}
    .rainbow-text {{
      font-size: 4em;
      font-family: 'Courier New', Courier, monospace;
      text-align: center;
      animation: rainbow 2s infinite;
    }}
    .pulse {{
      animation: pulse 1.5s infinite;
    }}
    @keyframes pulse {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.1); }}
      100% {{ transform: scale(1); }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Function to display typing effect
def display_typing_effect(text, delay=0.2):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f'<div class="rainbow-text pulse">{text[:i]}</div>', unsafe_allow_html=True)
        time.sleep(delay)

# Delay for 3 seconds to display the image
time.sleep(2)

# Remove the background image after 3 seconds
st.markdown("""
    <style>
    .stApp {
    background-image: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Display "Maneesh's mystery" with typing effect
display_typing_effect("Maneesh's mystery")

# Function to generate dynamic text with typing effect
def display_dynamic_text():
    phrases = ["out in"]
    for phrase in phrases:
        dynamic_placeholder.empty()  # Clear previous text
        display_typing_effect(phrase)

# Create a placeholder for the dynamic text
dynamic_placeholder = st.empty()

# Call the function to display dynamic text
display_dynamic_text()

# Function to display a countdown with typing effect
def display_countdown():
    countdown_placeholder = st.empty()  # Create a placeholder for the countdown
    for i in range(5, 0, -1):
        countdown_placeholder.markdown(f'<div class="rainbow-text pulse">{i}</div>', unsafe_allow_html=True)
        time.sleep(1)
    countdown_placeholder.markdown(f'<div class="rainbow-text pulse">1</div>', unsafe_allow_html=True)  # Display 1 forever

# Call the function to display the countdown
display_countdown()
display_typing_effect("day")
display_typing_effect("Don't miss it!")