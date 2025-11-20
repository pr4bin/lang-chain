import os
from langchain_community.document_loaders import TextLoader

def run():
    """Loads a sample text file and prints its content and metadata."""
    # Define the path to the sample document relative to the project root
    # Note: This assumes the script is run from the project root (e.g., via main.py)
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_document.txt')
    absolute_path = os.path.abspath(file_path)

    # Initialize the TextLoader with the absolute file path
    loader = TextLoader(absolute_path)

    try:
        # Load the documents
        documents = loader.load()

        # Print the loaded documents
        print(f"Loaded {len(documents)} document(s).")
        for doc in documents:
            print("--- Document Content ---")
            print(doc.page_content)
            print("--- Document Metadata ---")
            print(doc.metadata)
            print("-" * 30)
    except FileNotFoundError:
        print(f"Error: The file '{absolute_path}' was not found.")
        print("Please make sure the 'sample_document.txt' file exists in the project root directory.")