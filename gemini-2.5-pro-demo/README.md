# Gemini 2.5 Pro API Call Demo

This project is a simple Python script to demonstrate how to call the `gemini-2.5-pro` model using the `google-generativeai` library.

## Setup

1.  **Install the required library:**

    ```bash
    pip install google-generativeai
    ```

2.  **Set your API Key:**

    You need to get an API key from Google AI Studio and set it as an environment variable named `GOOGLE_API_KEY`.

    -   Get your key here: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

    -   **On Windows:**

        ```bash
        setx GOOGLE_API_KEY "YOUR_API_KEY"
        ```

    -   **On macOS/Linux:**

        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```

    *You may need to restart your terminal for the changes to take effect.*

## Running the script

Once you have installed the library and set up your API key, you can run the script:

```bash
python main.py
```
