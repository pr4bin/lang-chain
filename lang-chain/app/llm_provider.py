"""Initializes and provides the LLM instance and invocation functions."""

from langchain_community.cache import InMemoryCache
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from . import config
from .utils.clearString import remove_citations_and_bold


# Initialize the model with settings from the config file and a cache
llm = ChatPerplexity(
    model=config.PPLX_MODEL,
    api_key=config.PPLX_API_KEY,
    cache=InMemoryCache()
)

def invoke_llm(prompt: str):
    """
    Invokes the language model with a given prompt and returns the raw response.
    """
    return llm.invoke(prompt)

def get_clean_llm_response(prompt: str):
    """
    Invokes the language model and returns a cleaned string response,
    removing citations and bold markdown.
    """
    # Create a simple chain for prompt -> model -> clean_output
    chain = (
        ChatPromptTemplate.from_template(prompt)
        | llm
        | StrOutputParser()
        | remove_citations_and_bold
    )
    return chain.invoke({})
