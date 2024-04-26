from app import *
import requests
import re

AIRTABLE_BASE_ID = "appMj7i4u9zlsXGxx"
AIRTABLE_TABLE_NAME = "Users"
AIRTABLE_API_TOKEN = "patPfaFULxG8Buqpz.a2c61d6bd922cb354731622f871f541cbf328d7950a7a523cb1c84e53117b770"

def add_user(username, password) : 
    
    endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
    "records": [
        {
        "fields": {
            "username" : username,  
            "password" : password
        }
        },
        {
        "fields": {}
        }
    ]
    }

    r = requests.post(endpoint, headers=headers, json=data)
    print(r.json())


def get_user(user, info) :
    endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}?filterByFormula=(username='{user}')"
    headers = {
            "Authorization": f"Bearer {AIRTABLE_API_TOKEN}",
            "Content-Type": "application/json"
        }
    r = requests.get(endpoint, headers=headers)
    print(r.json())
    if info == 1:
        pattern = r"(?<='username': ')( *)\w+( *)\w+( *)"
        match = re.search(pattern, str(r.json()))
        if match: 
            print(match.group())
    if info == 2:
        pattern = r"(?<='password': ')( *)\w+( *)\w+( *)"
        match = re.search(pattern, str(r.json()))
        if match: 
            print(match.group())
    if info == 3:
        pattern = r"(?<='Money': )\d+"
        match = re.search(pattern, str(r.json()))
        if match: 
            print(match.group())

# get_user('karl', 3)

# {'records': [{'id': 'reclHbbi0vkkeTY8K', 'createdTime': '2024-04-25T14:13:13.000Z', 'fields': {'Money': 1000, 'username': 'karl', 'password': 'lele'}}]}