from pyairtable import Api
import os
from openai import OpenAI

# credentials
BASE_ID = os.environ["BASE_ID"]
TABLE_ID = os.environ["TABLE_ID"]
API_KEY = os.environ["API_KEY"]

# initialize airtable client
api = Api(API_KEY)
# table = api.get_table(BASE_ID,TABLE_ID)

openai_client = OpenAI()

chat_completion = openai_client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "What is Hack Club?"}]
)

print(chat_completion.dict())
