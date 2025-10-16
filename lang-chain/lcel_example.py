import os
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from text_utils import formalize_text # <--- Import formalize_text
from langchain_core.output_parsers import StrOutputParser # <--- Add this import
from clearString import remove_citations_and_bold # <--- Add this import

# Load environment variables from .env file
load_dotenv()

# Get the API key and model from environment variables
api_key = os.getenv("PPLX_API_KEY")
model_name = os.getenv("PPLX_MODEL")

# Initialize the model
model = ChatPerplexity(model=model_name, api_key=api_key)

# --- Prompt for Informal Summary ---
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant that provides short, informal summaries about topics."),
        ("user", "Summarize {topic} in a few sentences.")
    ]
)
# --- Build the LCEL Chain ---
# The output of the model (raw text) will be piped directly into our custom formalize_text function.
chain = prompt | model | StrOutputParser() | formalize_text | remove_citations_and_bold # <--- Modified chain

# --- Invoke the Chain ---
response = chain.invoke({"topic": "artificial intelligence using LangChain"})

# --- Print the Formalized Response ---
print(response)
