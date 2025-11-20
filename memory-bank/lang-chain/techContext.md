- Python 3.11.9
- pip 25.2
- `langchain` package installed.
- `langchain-perplexity` package installed.
- `python-dotenv` package installed.
- Virtual environment located at `C:\gemini projects\lang-chain\venv`

- Updated `prompt_template.py` to use `ChatPromptTemplate.from_messages` for defining prompts, allowing for explicit system and user message roles. The example now demonstrates a translation task, replacing the previous joke generation example.

- Applied optimizations to `clearString.py`'s `remove_citations_and_bold` function, including pre-compiling regex patterns, streamlining string stripping, and using `functools.singledispatch` for type-based dispatch.

- Extracted `formalize_text` function into `text_utils.py` for reusability and updated `lcel_example.py` to import it, demonstrating modular code organization.

- **Project Refactoring:** The project has been refactored into a modular architecture.
    - A central `main.py` at the root serves as an interactive menu-driven entry point.
    - All core application logic is now inside the `app/` directory.
    - `app/config.py` centralizes environment variable loading.
    - `app/llm_provider.py` provides a singleton instance of the `ChatPerplexity` model.
    - Example scripts are organized under `app/examples/`.
    - Utility functions are grouped in `app/utils/`.

- **Dependency Updates:**
    - Installed `langchain-community`.
    - Upgraded `langchain` to `1.0.1`.
    - Upgraded `langchain-perplexity` to `1.0.0`.
    - Upgraded `langchain-core` to `1.0.0`.
    - These upgrades were necessary to resolve dependency conflicts.

- **Interactive Examples:**
    - The "AI Translator" (`prompt_template.py`) is now an interactive tool that takes user input for the languages and text to be translated.
    - The "List Generator" (`commaSeparatedList.py`) is an interactive tool for creating lists of items based on user-defined categories and contexts.
    - Both examples have been enhanced with more specific prompts and output parsers to ensure clean, predictable output.