from .clearString import remove_citations_and_bold

def formalize_text(text: str) -> str:
    """Replaces common contractions and adds a formal closing."""
    text = text.replace("don't", "do not")
    text = text.replace("can't", "cannot")
    text = text.replace("it's", "it is")
    text = text.replace("I'm", "I am")
    text = text.replace("you're", "you are")
    text = text.replace("we're", "we are")
    text = text.replace("they're", "they are")
    text = text.replace("isn't", "is not")
    text = text.replace("aren't", "are not")
    text = text.replace("won't", "will not")
    text = text.replace("wouldn't", "would not")
    text = text.replace("shouldn't", "should not")
    text = text.replace("couldn't", "could not")
    text = text.replace("haven't", "have not")
    text = text.replace("hasn't", "has not")
    text = text.replace("hadn't", "had not")
    text = text.replace("wasn't", "was not")
    text = text.replace("weren't", "were not")
    text = text.replace("doesn't", "does not")
    text = text.replace("didn't", "did not")
    text = text.replace("would've", "would have")
    text = text.replace("could've", "could have")
    text = text.replace("should've", "should have")
    text = text.replace("might've", "might have")
    text = text.replace("must've", "must have")
    text = text.replace("wouldn't have", "would not have")
    text = text.replace("couldn't have", "could not have")
    text = text.replace("shouldn't have", "should not have")
    text = text.replace("mightn't have", "might not have")
    text = text.replace("mustn't have", "must not have")
    
    if not text.endswith(('.', '!', '?')):
        text += "."
    
    return text

def clean_and_formalize(text: str) -> str:
    """Cleans and formalizes the text."""
    cleaned_text = remove_citations_and_bold(text)
    formalized_text = formalize_text(cleaned_text)
    return formalized_text