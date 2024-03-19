from pyairtable import Api
import os
from openai import OpenAI
import requests
from dotenv import load_dotenv
from typing import List
from pprint import pprint

# importing sample code to avoid polluting the code
from sample import code_1, errors_1

# load environment variables
load_dotenv()

# credentials
BASE_ID = os.environ["BASE_ID"]
TABLE_ID = os.environ["TABLE_ID"]
API_KEY = os.environ["API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# initialize airtable client
api = Api(API_KEY)
# table = api.get_table(BASE_ID,TABLE_ID)

openai_client = OpenAI(api_key=OPENAI_API_KEY)

class ChatGPTAssistant:
  def __init__(self, openai_api_key: str, model: str = "gpt-3.5-turbo"):
    self.openai_client = OpenAI(api_key=openai_api_key)
    self.model_version = model
    self.sprig_docs = self.load_sprig_docs()
    self.chat_messages = [
      { "role": "user", "content": self.sprig_docs },
    ]

  def chat_completion(self, query: str):
    messages = self.chat_messages + [
      {"role": "user", "content": query}
    ]

    completion = self.openai_client.chat.completions.create(
      model=self.model_version,
      messages=messages
    )
    assistant_completion = completion.choices.pop().message.content

    # add assitant completion to the history
    self.chat_messages += [
      { "role": "assistant", "content": assistant_completion }
    ]

    # the chat messages history will only be mutated if the chat completion succeeds
    self.chat_messages = messages
    
    # return the assitant completion to the user if they want to use it for anything whatsoever
    return assistant_completion

  def build_code_prompt(self, code: str, error_logs: str = ""): 
    prompt = "Here is a piece of code: " + f"\n ```\n{code} \n```" + "\n it is showing me these errors" + f"\n```\n{error_logs} \n ```" + "\n identify the issue in the code and suggest a fix. write the full code with the issue fixed."
    return prompt

  @staticmethod
  def load_sprig_docs() -> str:
    sprig_docs_url = "https://raw.githubusercontent.com/hackclub/sprig/main/docs/docs.md"
    return str(requests.get(sprig_docs_url).content)

"""
The response returned by ChatGPT contains code wrapped in blocks by backticks
with the language specified at the end of the opening three backticks
```js
```

This function takes advantage of this information to split the completion text
by three backticks.

If we start counting from 1, the code within the backticks will always fall
at even number indices. 

So, we can get only the text at those indices knowing that it's a block of code from the completion.

We then slice away the text upto the first new line as they're usually the language specifier.

"""
def get_code_blocks(source: str, delimiter: str = "```") -> List[str]:
  results = []
  for i, x in enumerate(source.split(delimiter)):
    if (i+1) % 2 != 0: continue
    # remove the dangling language specifier 
    first_newline = x.find("\n")
    results.append(x[first_newline+1:])
  return results


gpt_assitant = ChatGPTAssistant(OPENAI_API_KEY)

# completion = gpt_assitant.chat_completion("How do I create a new level in Sprig?")
code_prompt = gpt_assitant.build_code_prompt(code_1, errors_1)
completion = gpt_assitant.chat_completion(code_prompt)

codes = get_code_blocks(completion)
print(codes[-1])