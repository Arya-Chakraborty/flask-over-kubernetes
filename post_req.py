import requests
dict_to_send = {'question':'what is your name?'}
res = requests.post('http://127.0.0.1:41041/', json=dict_to_send, timeout=10)
# print('response from server:',res.text)
dict_from_server = res.json()
print('response from server:',dict_from_server["name"])
