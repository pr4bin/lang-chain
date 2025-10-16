import os
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key and model from environment variables
api_key = os.getenv("PPLX_API_KEY")
model_name = os.getenv("PPLX_MODEL")

# Define the system message template
system_template = "Translate the following from English into {language}"

# Define the user message template
user_template = "{text}"

# Create the ChatPromptTemplate from these messages
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", user_template)
    ]
)

# Initialize the model
model = ChatPerplexity(model=model_name, api_key=api_key)

# Create a chain that combines the prompt and the model
chain = prompt | model

# Invoke the chain with language and text for translation
response = chain.invoke({"language": "Spanish", "text": "Hello, how are you?"})

# Print the response
print(response.content)