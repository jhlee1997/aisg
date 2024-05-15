# Get env variables
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
API_URL = os.getenv('API_URL')
# print(API_URL)


# Define API request function
# Documentation reference: https://huggingface.co/docs/api-inference/quicktour
import requests

headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()


# Define parameters
# Text generation task for GPT2
# documentation reference: https://huggingface.co/docs/api-inference/detailed_parameters#text-generation-task
parameters = dict()
parameters['max_new_tokens'] = 50
parameters['num_return_sequences'] = 1
parameters['temperature'] = 0.8
# print(parameters)


# Accept user input
payload = dict()
payload['inputs'] = input("Input: ")
payload['parameters'] = parameters


# Return generated text
data = query(payload)
print("Generated Text: " + data[0]['generated_text'])