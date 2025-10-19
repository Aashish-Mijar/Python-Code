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