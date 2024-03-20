from pyairtable import Api
import os
from dotenv import load_dotenv
import json

from main import ChatGPTAssistant

# load environment variables
load_dotenv()

# credentials
BASE_ID = os.environ["BASE_ID"]
TABLE_ID = os.environ["TABLE_ID"]
API_KEY = os.environ["API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# initialize airtable client
api = Api(API_KEY)

dataset = []

client = ChatGPTAssistant(OPENAI_API_KEY)

def build_prompt_response(code: str, errors: str, response: str):
  text = "### User: " \
  + "Here is a piece of code \n" \
  + "```\n" \
  + f"{code}\n" \
  + "```\n" \
  + "It is showing me these errors" \
  + f"{errors}" \
  + "identify the issue and suggest a fix" \
  + "### Assistant:" \
  + f"{response}"
  return text

def load_requests_data():
  records = api.get_table(BASE_ID, TABLE_ID).all()
  for idx, record in enumerate(records):
    record_fields = record.get("fields")

    if record_fields.get("Fixed Code") == "N/A" or record_fields.get("Fixed Code") == "": continue

    record_code = record_fields.get("Code", "")
    record_error_log = record_fields.get("Error Log", "")

    code_prompt = client.build_code_prompt(record_code, record_error_log)
    completion = client.chat_completion(code_prompt)

    prompt_response = build_prompt_response(record_code, record_error_log, completion)

    dataset.append({
      "text": prompt_response,
    }) 

load_requests_data()

with open("dataset.jsonl", "w") as file:
  file.write(json.dumps(dataset))