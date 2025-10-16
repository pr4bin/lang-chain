-	Python 3.11.9
-	pip 25.2
-	`langchain` package installed.
-	`langchain-perplexity` package installed.
-	`python-dotenv` package installed.
-	Virtual environment located at `C:\gemini projects\lang-chain\venv`

- Updated `prompt_template.py` to use `ChatPromptTemplate.from_messages` for defining prompts, allowing for explicit system and user message roles. The example now demonstrates a translation task, replacing the previous joke generation example.

- Applied optimizations to `clearString.py`'s `remove_citations_and_bold` function, including pre-compiling regex patterns, streamlining string stripping, and using `functools.singledispatch` for type-based dispatch.

- Extracted `formalize_text` function into `text_utils.py` for reusability and updated `lcel_example.py` to import it, demonstrating modular code organization.