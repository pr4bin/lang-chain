from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from app.llm_provider import llm
from app.utils.clearString import remove_citations_and_bold

def run(category: str, context: str, count: int):

    # Initialize the output parser
    parser = CommaSeparatedListOutputParser()

    # Create a prompt template
    template = """
You are a helpful assistant. List {count} {category} {context}.
Provide only the list as a comma-separated list, with no additional explanations or commentary.

List:
"""
    prompt = ChatPromptTemplate.from_template(template)


    # Create a chain that combines the prompt, model, and output processing
    chain = prompt | llm | parser

    # Invoke the chain with the user's input
    response = chain.stream({
        "count": count,
        "category": category,
        "context": context
    })

    # Print the structured response
    for item in response:
        if isinstance(item, list):
            for sub_item in item:
                yield f"- {remove_citations_and_bold(sub_item).strip()}\n"
        else:
            yield f"- {remove_citations_and_bold(item).strip()}\n"