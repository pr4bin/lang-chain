import re
from functools import singledispatch
from typing import List

# --- OPTIMIZATION: Pre-compile regex patterns ---
CITATION_PATTERN = re.compile(r'\[\d+\]')
BOLD_PATTERN = re.compile(r'\*\*(.*?)\*\*')

@singledispatch
def remove_citations_and_bold(text):
    """Generic function to remove citations and bold markdown."""
    raise NotImplementedError(f"Type {type(text)} not supported for remove_citations_and_bold.")

@remove_citations_and_bold.register(str)
def _(text: str) -> str:
    """Removes citations and bold markdown from a single string."""
    # --- OPTIMIZATION: Streamline stripping ---
    text = text.strip()
    # Check for and remove outer quotes if present
    if (text.startswith("'") and text.endswith("'")) or \
       (text.startswith('"') and text.endswith('"')):
        text = text[1:-1].strip() # Remove outer quotes and then strip again

    # --- OPTIMIZATION: Use pre-compiled patterns ---
    text = CITATION_PATTERN.sub('', text)
    text = BOLD_PATTERN.sub(r'\1', text)

    return text.strip().rstrip('.')


@remove_citations_and_bold.register(list)
def _(text: List[str]) -> List[str]:
    """Removes citations and bold markdown from each string in a list and returns a new list."""
    return [remove_citations_and_bold(item) for item in text]