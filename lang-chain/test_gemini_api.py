import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Debug: Check if environment variable is loaded
print("GEMINI_API_KEY loaded:", "GEMINI_API_KEY" in os.environ)
print("GEMINI_MODEL loaded:", "GEMINI_MODEL" in os.environ)

if "GEMINI_API_KEY" in os.environ:
    print("API Key:", os.environ["GEMINI_API_KEY"][:10] + "...")
else:
    print("ERROR: GEMINI_API_KEY not found in environment")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
try:
    client = genai.Client()
    print("Client created successfully")
    
    # List available models
    print("\n=== Checking Available Models ===")
    try:
        models = client.models.list()
        print("Available models:")
        for model in models:
            print(f"  - {model.name}")
            if hasattr(model, 'supported_generation_methods'):
                print(f"    Supported methods: {model.supported_generation_methods}")
    except Exception as list_error:
        print(f"Error listing models: {list_error}")
    
    # Try with the model from .env file
    model_name = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")
    print(f"\nTesting model: {model_name}")
    
    response = client.models.generate_content(
        model=model_name, contents="Explain how AI works in a few words"
    )
    print("Response received:")
    print(response.text)
    
except Exception as e:
    print(f"Error: {e}")
    print("Trying alternative model names...")
    
    # Try different model names
    alternative_models = ["gemini-pro", "gemini-1.5-flash", "gemini-1.5-pro"]
    for model in alternative_models:
        try:
            print(f"Trying model: {model}")
            response = client.models.generate_content(
                model=model, contents="Hello"
            )
            print(f"Success with {model}: {response.text[:50]}...")
            break
        except Exception as e2:
            print(f"Failed with {model}: {e2}")
