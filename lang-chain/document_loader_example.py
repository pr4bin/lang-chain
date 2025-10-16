from langchain_community.document_loaders import TextLoader

# Define the path to your sample document
file_path = "sample_document.txt" # Relative path from the script's location

# Initialize the TextLoader with the file path
loader = TextLoader(file_path)

# Load the documents
# The load() method returns a list of Document objects
documents = loader.load()

# Print the loaded documents
print(f"Loaded {len(documents)} document(s).")
for doc in documents:
    print("--- Document Content ---")
    print(doc.page_content)
    print("--- Document Metadata ---")
    print(doc.metadata)
    print("-" * 30)