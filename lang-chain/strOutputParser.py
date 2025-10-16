import os
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from clearString import remove_citations_and_bold # Import your function

# Load environment variables from .env file
load_dotenv()

# Get the API key and model from environment variables
api_key = os.getenv("PPLX_API_KEY")
model_name = os.getenv("PPLX_MODEL")

# Initialize the model
model = ChatPerplexity(model=model_name, api_key=api_key)

# Initialize the output parser (StrOutputParser is often implicit, but explicit for clarity)
parser = StrOutputParser()

# Create a prompt template that encourages bold text and citations
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a creative storyteller. Include some **bold text** and a citation like [1] in your story."),
        ("user", "Tell me a short story about a brave knight.")
    ]
)

# Create a chain: prompt -> model -> parser -> remove_citations_and_bold
chain = prompt | model | parser | remove_citations_and_bold

# Invoke the chain
cleaned_response = chain.invoke({})

print("--- Cleaned Response (Directly from Chain) ---")
print(cleaned_response)