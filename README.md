# Text Operations using GenAI(gemini pro)

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

## Future work

Future work involves adding more text features like `grammar checker`, `translator`, etc.

## input text
<img width="293" alt="image" src="https://github.com/vishnuvardhan-jadava/Text_Operations_GenAI/assets/83878754/0369470c-e896-4a88-97b3-2007599f974c">

## Summarize Response
<img width="369" alt="image" src="https://github.com/vishnuvardhan-jadava/Text_Operations_GenAI/assets/83878754/fdd2a276-46c5-452a-a94c-7adde2638d3b">

## Paraphrase response
<img width="361" alt="image" src="https://github.com/vishnuvardhan-jadava/Text_Operations_GenAI/assets/83878754/63427bc6-14db-48bb-87b5-39846d615f89">
