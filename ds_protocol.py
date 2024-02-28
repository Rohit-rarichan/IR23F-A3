# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645

import json
from collections import namedtuple


# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['foo','baz'])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    json_obj = json.loads(json_msg)
    foo = json_obj['foo']
    baz = json_obj['bar']['baz']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(foo, baz)

def join(username:str, password: str):
    join_msg = {"join":{"username": username, "password": password, "token": ''}}
    return json.dumps(join_msg)

def post(message:str, user_token:str, timestamp:str ):
   post_msg = {"token": user_token, "post":{"entry":message, "timestamp": timestamp}}  #or use time.time()
   return json.dumps(post_msg)

def bio_send(bio:str, user_token:str, timestamp:str):
   bio_msg = {"token": user_token, "post":{"entry":bio, "timestamp": timestamp}}
   return json.dumps(bio_msg)



   