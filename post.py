import requests
import json
data={'d':"value"}
while True:
	url="http://localhost:5000/todos/todo1"
	#data_json = json.dumps(data)
	#headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=data)
	print(response.text)