import os
from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PPLX_API_KEY")
model_name = os.getenv("PPLX_MODEL")

model = ChatPerplexity(model=model_name, api_key=api_key)

message = model.invoke("your one liner intro")

print(message.content)
