# Steps to Integrate Chat-GPT API into your project

Documentation: https://platform.openai.com/docs/overview




## Step 1: Create an account at OpenAI

- Go to [OpenAI](https://beta.openai.com/signup/) and create an account.
- Once you have created an account, you will be able to access the API key.
- You will need this API key to access the GPT-3 API.
- You can find the API key in the API section of the OpenAI dashboard.
- You can also find the API key in the email sent by OpenAI after you have created an account.

## Step 2: Take a look at the Documentation

- Go to the [OpenAI API documentation](https://platform.openai.com/docs/overview) and take a look at the documentation.
- The documentation provides a detailed overview of the API and how to use it.
- You can also find code examples in various programming languages to help you get started.
- The [Quickstart](https://platform.openai.com/docs/quickstart) section provides a step-by-step guide to help you get started with the API.

## Step 3: Install the OpenAI Package
To add the OpenAI node package to your project, run the following command:
```bash
npm install openai
```

To install the OpenAI Python package, run the following command:
```bash
pip install openai
```

## Step 4: Setup your API Key
- You will need to set up your API key to access the GPT-3 API.
- You can get an API key from the OpenAI dashboard. Go to: https://beta.openai.com/account/api-keys after signing up.
- From there, generate a "secrect key." You will need this key to authenticate requests to the GPT-3 API.
- **DO NOT PUSH** this key to GitHub. You should store it in a `.env` file and add the `.env` file to your `.gitignore` file.

  

## Chat Completion
- OpenAI offers many services, including chat completion.
- The system prompt is the hidden prompt that the model sees when generating completions. It generally consists of the usage context (how the system should act) and format/structure of repsonses.
- The messages are the conversation history. The model will use this context to generate completions. The message history should be saved and appended to with each turn in the conversation. Note that the role switch between `user` and `assistant` is important to get the desired response (ChatGPT is the assistant).
- The `response` variable will be the completion of the conversation, i.e., the next assistant respone given the message history.
- Note the `choices` attribute of the response object. This is the array of completions, with each completion being a dictionary with the `role` and `content` attributes.

JavaScript example:
```javascript
import OpenAI from "openai";

// don't actually insert the plain text key here, instead
// import it from a .env file or other gitignore'd file

const openai = new OpenAI({ apiKey: "YOUR_API_KEY"});

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}
main();
```
Python example:
```python
from openai import OpenAI

# don't actually insert the plain text key here, instead 
# import it from a .env file or other gitignore'd file
client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response)
```