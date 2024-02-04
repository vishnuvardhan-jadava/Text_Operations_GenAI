# Text_Operations_GenAI

```markdown
# Text Summarizer using Gemini Pro

This project uses the `Gemini Pro` model from `Google GenerativeAI` to summarize or paraphrase text. The application is built with `Streamlit`.

## Setup

1. Clone the repository.
2. Install the required libraries: `streamlit`, `google.generativeai`, and `python-dotenv`.
3. Create a `.env` file in the root directory and add your `API_KEY` for `Google GenerativeAI`.

## Usage

Run the Streamlit app with the command: `streamlit run app.py`

In the app, you can enter your text in the input field and choose to either `Summarize` or `Paraphrase` the text. The result will be displayed on the webpage.

## Functions

- `get_response(prompt: str) -> str`: This function takes a prompt and returns a response from the `Gemini Pro` model.
- `perform_action(action: str) -> None`: This function takes the user input and the operation that the user wants to perform on their input. It does not return anything, instead, it writes the output on the webpage.
```
