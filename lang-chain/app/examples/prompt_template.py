from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.llm_provider import llm
from app.utils.clearString import remove_citations_and_bold

async def run(input_language: str, output_language: str, text: str):
    """Demonstrates an interactive prompt template for a translation task."""

    # Define the prompt template
    template = """
You are a professional translator. Translate the following text from {input_language} to {output_language}.
Provide only the translated text, with no additional explanations, commentary, or citations.

Original text: {text}

Translated text:
"""

    # Create the ChatPromptTemplate
    prompt = ChatPromptTemplate.from_template(template)

    # Create a chain that combines the prompt, model, and output processing
    chain = prompt | llm | StrOutputParser() | remove_citations_and_bold

    return chain.astream({
        "input_language": input_language,
        "output_language": output_language,
        "text": text
    })