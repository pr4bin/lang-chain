import os
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv
from clearString import remove_citations_and_bold 


# Load environment variables from .env file
load_dotenv()

# Get the API key and model from environment variables
api_key = os.getenv("PPLX_API_KEY")
model_name = os.getenv("PPLX_MODEL")

# Initialize the model
model = ChatPerplexity(model=model_name, api_key=api_key)

# Initialize the output parser
parser = CommaSeparatedListOutputParser()

# Create a prompt template for listing landmarks
# We instruct the LLM to return a comma-separated list
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. List items name without description as a comma-separated list"),
        ("user", "List the top 3 famous landmarks in {city}")
    ]
)

# Create a chain that combines the prompt, model, and parser
# The output of the model will be passed to the parser
chain = prompt | model | parser | remove_citations_and_bold

# Invoke the chain with a city
response = chain.invoke({"city": "hyderabad"})

# Print the structured response
print(response)