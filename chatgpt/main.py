# Python example of using the ChatGPT API for chat completion
# See https://platform.openai.com/docs/api-reference/ for examples of other APIs you can use

import os
from pprint import pprint
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('../.env')

client = OpenAI()

# Create a generic function that calls the OpenAI API for chat completion
def chat(content):
  completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
      { 'role': 'user', 'content': content }
    ]
  )
  # Convert completions response to a dictionary
  return completion.choices[0].model_dump()

# Print the response from the function call
pprint(chat('What is the most popular name for athletes?'))
pprint(chat('Which dining hall is the best at UCLA?'))


"""
EXAMPLE RESPONSE:

{'finish_reason': 'stop',
 'index': 0,
 'logprobs': None,
 'message': {'content': 'One of the most popular names for athletes is '
                        'Michael. Many successful athletes have been named '
                        'Michael, including Michael Jordan, Michael Phelps, '
                        'and Michael Schumacher.',
             'function_call': None,
             'role': 'assistant',
             'tool_calls': None}}
{'finish_reason': 'stop',
 'index': 0,
 'logprobs': None,
 'message': {'content': 'This is a subjective question and opinions may vary. '
                        'Some popular dining halls at UCLA include Covel '
                        'Commons, De Neve, and Bruin Plate. It is recommended '
                        'to try out different dining halls and see which ones '
                        'you personally prefer based on the food options, '
                        'atmosphere, and overall dining experience.',
             'function_call': None,
             'role': 'assistant',
             'tool_calls': None}}
"""