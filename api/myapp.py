import requests
import json

URL="http://localhost:8000/studentapi/"

#read
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url= URL,headers = headers, data = json_data)
    data = r.json()
    print(data)

#create
def post_data():
    data = {'name':'Ravii','roll':107,'city':'Mumbaii'}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

#update
def update_data():
    data = {'id':4,'name':'Ravii','roll':104,'city':'Indoreee'}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url= URL,headers = headers, data = json_data)
    data = r.json()
    print(data)

#delete
def delete_data():
    data = {'id':4}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
# get_data()

delete_data()


