# Steps to Integrate Chat-GPT API into your project

Documentation: https://platform.openai.com/docs/overview




## Step 1: Create an account at OpenAI

- Go to [OpenAI](https://openai.com) and create an account. Note that you will get $5 in free credit if this is a new account.

## Step 2: Take a look at the Documentation

- Go to the [OpenAI API documentation](https://platform.openai.com/docs/overview) and take a look at the documentation.
- The documentation provides a detailed overview of the API and how to use it.
- You can also find code examples in various programming languages to help you get started.
- The [Quickstart](https://platform.openai.com/docs/quickstart) section provides a step-by-step guide to help you get started with the API.

## Step 3: Install the packages for the project
To add npm packages for this project, run the following command:
```bash
npm install
```

To install the Python packages for this project, run the following command:
```bash
pip install -r requirements.txt
```

## Step 4: Setup your API Key
- You will need to set up your API key to access the GPT-3 API. Get an API key from the OpenAI dashboard. Go to: https://platform.openai.com/api-keys after signing up.
- From there, generate a "secrect key." You will need this key to authenticate requests to the GPT-3 API in your code.
- **DO NOT PUSH** this key to GitHub. You should store it in a `.env` file (provided for you).

## Chat Completion
- OpenAI offers many services, including chat completion.
- The system prompt is the hidden prompt that the model sees when generating completions. It generally consists of the usage context (how the system should act) and format/structure of repsonses.
- The messages are the conversation history. The model will use this context to generate completions. The message history should be saved and appended to with each turn in the conversation. Note that the role switch between `user` and `assistant` is important to get the desired response (ChatGPT is the assistant).
- The `response` variable will be the completion of the conversation, i.e., the next assistant respone given the message history.
- Note the `choices` attribute of the response object. This is the array of completions, with each completion being a dictionary with the `role` and `content` attributes.

A simple JavaScript example that uses the chat completions API can be found at `index.js`

A simple Python example that uses the chat completions API can be found at `main.py`