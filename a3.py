# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645

from ds_client import send

def main():
    print("Welcome to the ICS 32 server communications")
    ans = 'y'
    while ans == 'y' or ans == "Y":
        username = input("Enter the username : ")
        password = input("Enter the password : ")
        bio = input("Enter a few lines of bio data : ")
        message = input("Enter the message that you would like to send the server : ")
        srv_ip = input("Enter the server IP address : ")
        srv_port = input("Enter the server port : ")
        send(srv_ip, srv_port, username, password, message, bio)
        ans = input("Would you like to continue Y/N : ")


if __name__ == "__main__":
    main()