# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645

import socket

import json
from ds_protocol import join

def send(server:str, port:str, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''

  '''profile = Profile(username, password, bio)
  profile.save_profile(server)'''
  try:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((server,int(port)))

    print(f"client connected to {server} on {port}")
    join_msg = join(username, password)
    client.send(join_msg.encode('utf-8'))

    resp = client.recv(1024).decode()
    print(resp)
    response_json = json.loads(resp)
    print(response_json)
    return True
  except Exception as e:
      print("Error:", e)
      return False
