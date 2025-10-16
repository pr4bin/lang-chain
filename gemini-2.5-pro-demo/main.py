
import os
import sys
import google.generativeai as genai

# --- Python Version Check ---
# The google-generativeai library requires Python 3.9 or higher.
# This check ensures the user is running a compatible version.
if sys.version_info < (3, 9):
    print("ERROR: This script requires Python 3.9 or higher.")
    print(f"You are using Python {sys.version.split()[0]}. Please upgrade your Python version.")
    exit()

# --- Configuration ---
# Load the API key from the environment variable 'GOOGLE_API_KEY'.
# This is the recommended and secure way to handle API keys, as described
# in the README.md file.
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: The 'GOOGLE_API_KEY' environment variable was not found.")
    print("Please follow the setup instructions in README.md to set your API key.")
    exit()

genai.configure(api_key=api_key)

# --- Model Interaction ---
def call_gemini():
    """
    This function calls the Gemini 2.5 Pro model with a simple prompt.
    """
    try:
        # Create the model
        model = genai.GenerativeModel('gemini-2.5-pro')

        # Send a prompt to the model
        prompt = "Describe the color blue to someone who has never seen it."
        safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE',
        }
        response = model.generate_content(prompt, safety_settings=safety_settings)

        # Print the response
        print("--- Gemini 2.5 Pro Response ---")
        print(response.text)
        print("-----------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have the 'google-generativeai' library installed.")
        print("You can install it by running: pip install google-generativeai")

if __name__ == "__main__":
    call_gemini()
