from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.llm_provider import llm
from app.utils.text_utils import clean_and_formalize

def run(topic: str):
    """Demonstrates a more complex LCEL chain with a custom utility function."""
    # --- Prompt for Informal Summary ---
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an assistant that provides short, informal summaries about topics."),
            ("user", "Summarize {topic} in a few sentences.")
        ]
    )

    # --- Build the LCEL Chain ---
    chain = prompt | llm | StrOutputParser() | clean_and_formalize

    # --- Invoke the Chain ---
    response = chain.invoke({"topic": topic})

    # --- Return the Formalized Response ---
    return response
