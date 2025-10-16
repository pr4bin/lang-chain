import os
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain_perplexity import ChatPerplexity

def main():
    """
    An example script to demonstrate usage of the Perplexity API with LangChain.
    """
    # 1. Get API key from user and set it as an environment variable
    if not os.environ.get("PPLX_API_KEY"):
        try:
            os.environ["PPLX_API_KEY"] = getpass.getpass("Enter your Perplexity API key: ")
        except Exception as e:
            print(f"Could not read API key: {e}")
            return

    # 2. Instantiate the ChatPerplexity model
    # You can change the model name to any of the available Perplexity models.
    # The "llama-3.1" models are available to Pro users.
    # We'll use a model available on the free tier to avoid authentication issues.
    # See https://docs.perplexity.ai/docs/model-cards for a list of models.
    try:
        llm = ChatPerplexity(model="llama-3-sonar-small-32k-online", temperature=0.7)
    except Exception as e:
        print(f"Failed to instantiate the model. Check your API key and model name. Error: {e}")
        return

    # 3. Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "{input}")
    ])

    # 4. Create a chain and invoke it
    chain = prompt | llm
    question = "What is the capital of France?"
    print(f"Asking: {question}")
    try:
        response = chain.invoke({"input": question})
    except Exception as e:
        print(f"An error occurred while invoking the chain: {e}")
        return

    # 5. Print the content of the response
    print("\nResponse:")
    print(response.content)

    # 6. Accessing search results metadata (if available)
    if "search_results" in response.additional_kwargs:
        print("\n--- Search Results ---")
        for result in response.additional_kwargs["search_results"]:
            print(f"- {result.get('title')}: {result.get('url')}")

if __name__ == "__main__":
    main()
