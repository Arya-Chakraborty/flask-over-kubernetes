import requests
dictToSend = {'question':'what is your name?'}
res = requests.post('http://127.0.0.1:41041/', json=dictToSend, timeout=10)
# print('response from server:',res.text)
dictFromServer = res.json()
print('response from server:',dictFromServer["name"])
