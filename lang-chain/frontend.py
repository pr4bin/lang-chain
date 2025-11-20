import asyncio
from contextlib import redirect_stdout
import io

from reactpy import component, html, use_state, use_callback

from app.examples import (
    prompt_template,
    lcel_example,
    commaSeparatedList,
    document_loader_example,
    rag_example
)

EXAMPLES = {
    "AI Translator": prompt_template,
    "List Generator": commaSeparatedList,
    "LCEL Example": lcel_example,
    "Document Loader": document_loader_example,
    "RAG Example": rag_example,
}

@component
def App():
    active_example, set_active_example = use_state(None)
    output, set_output = use_state("")
    is_running, set_is_running = use_state(False)

    # State for AI Translator
    translator_input_lang, set_translator_input_lang = use_state("English")
    translator_output_lang, set_translator_output_lang = use_state("French")
    translator_text, set_translator_text = use_state("Hello, how are you?")

    # State for List Generator
    list_category, set_list_category = use_state("Top 5 Indian web series")
    list_context, set_list_context = use_state("on Netflix in 2024")
    list_count, set_list_count = use_state("5")

    # State for LCEL Example
    lcel_topic, set_lcel_topic = use_state("artificial intelligence using LangChain")

    # State for RAG Example
    rag_question, set_rag_question = use_state("What is the document about?")
    rag_file, set_rag_file = use_state("sample_document.txt")

    @use_callback
    async def handle_run_example(event):
        if not active_example:
            return

        set_is_running(True)
        set_output("Running...")

        async def task():
            try:
                module = EXAMPLES[active_example]
                if active_example == "AI Translator":
                    stream = await module.run(translator_input_lang, translator_output_lang, translator_text)
                    temp_output = ""
                    async for chunk in stream:
                        temp_output += chunk
                        set_output(temp_output)
                elif active_example == "List Generator":
                    stream = module.run(list_category, list_context, int(list_count))
                    temp_output = ""
                    for chunk in stream:
                        temp_output += chunk
                        set_output(temp_output)
                elif active_example == "LCEL Example":
                    response = module.run(lcel_topic)
                    set_output(response)
                elif active_example == "RAG Example":
                    response = module.run(rag_question, rag_file)
                    set_output(response)
                else:
                    with io.StringIO() as string_io, redirect_stdout(string_io):
                        module.run()
                        captured_output = string_io.getvalue()
                    set_output(captured_output)
            except Exception as e:
                set_output(f"An error occurred: {e}")
            finally:
                set_is_running(False)

        asyncio.create_task(task())

    def get_input_fields():
        if active_example == "AI Translator":
            return html.div({"class": "mb-3"},
                html.label({"class": "form-label"}, "Input Language"),
                html.input({"type": "text", "class": "form-control", "value": translator_input_lang, "onChange": lambda event: set_translator_input_lang(event['target']['value'])}),
                html.label({"class": "form-label"}, "Output Language"),
                html.input({"type": "text", "class": "form-control", "value": translator_output_lang, "onChange": lambda event: set_translator_output_lang(event['target']['value'])}),
                html.label({"class": "form-label"}, "Text to Translate"),
                html.textarea({"class": "form-control", "rows": 3, "value": translator_text, "onChange": lambda event: set_translator_text(event['target']['value'])})
            )
        elif active_example == "List Generator":
            return html.div({"class": "mb-3"},
                html.label({"class": "form-label"}, "Category"),
                html.input({"type": "text", "class": "form-control", "value": list_category, "onChange": lambda event: set_list_category(event['target']['value'])}),
                html.label({"class": "form-label"}, "Context"),
                html.input({"type": "text", "class": "form-control", "value": list_context, "onChange": lambda event: set_list_context(event['target']['value'])}),
                html.label({"class": "form-label"}, "Number of Items"),
                html.input({"type": "number", "class": "form-control", "value": list_count, "onChange": lambda event: set_list_count(event['target']['value'])})
            )
        elif active_example == "LCEL Example":
            return html.div({"class": "mb-3"},
                html.label({"class": "form-label"}, "Topic"),
                html.input({"type": "text", "class": "form-control", "value": lcel_topic, "onChange": lambda event: set_lcel_topic(event['target']['value'])})
            )
        elif active_example == "RAG Example":
            return html.div({"class": "mb-3"},
                html.label({"class": "form-label"}, "Question"),
                html.input({"type": "text", "class": "form-control", "value": rag_question, "onChange": lambda event: set_rag_question(event['target']['value'])}),
                html.label({"class": "form-label"}, "File"),
                html.select({"class": "form-select", "value": rag_file, "onChange": lambda event: set_rag_file(event['target']['value'])},
                    html.option({"value": "sample_document.txt"}, "sample_document.txt"),
                    html.option({"value": "Complete Nextjs Mastery Guide- From Beginner to Expert.pdf"}, "Complete Nextjs Mastery Guide- From Beginner to Expert.pdf")
                )
            )
        return None

    return html.div({"class": "container mt-4"},
        html.head(
            html.link({"rel": "stylesheet", "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"})
        ),
        html.h1({"class": "mb-4"}, "LangChain Examples"),
        html.div({"class": "btn-group mb-4"},
            *[html.button(
                {
                    "type": "button",
                    "class": f"btn { 'btn-primary' if active_example == name else 'btn-outline-primary' }",
                    "onClick": lambda event, name=name: set_active_example(name),
                    "disabled": is_running,
                },
                name
            ) for name in EXAMPLES]
        ),
        html.div({"class": "row"},
            html.div({"class": "col-md-6"},
                html.h2("Input"),
                get_input_fields(),
                html.button(
                    {
                        "type": "button",
                        "class": "btn btn-success w-100",
                        "onClick": handle_run_example,
                        "disabled": not active_example or is_running,
                    },
                    "Run Example"
                ),
            ),
            html.div({"class": "col-md-6"},
                html.h2("Output"),
                html.pre({"class": "bg-light p-3", "style": {"minHeight": "300px", "white_space": "pre-wrap", "word_wrap": "break-word", "overflow_x": "hidden"}}, output)
            )
        )
    )


