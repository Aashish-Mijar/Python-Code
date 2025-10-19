"""
1- twilio client setup
2- user inputs
3- scheduling logic
4- send message
"""

# step -1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2 twilio credentials
account_sid = "ACc25b7bfb10d0770313058cd12f990d13"
auth_token = "45be853fd2866a24a9cde6030edd6916" 

client = Client(account_sid, auth_token)

# step-3 design send message function
def send_whatsapp_message(receipent_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886', 
            body = message_body, 
            to=f'whatsapp:{receipent_number}' 
            )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')

# step - 4 user input
name = input("Enter the recipient name = ")
recipent_number = input("Enter the recipient number with country code (e.g, +977)")
message_body = input(f"Enter the message you want to send to {name}: ")

# step - 5

