import requests
dictToSend = {'question':'what is your name?'}
res = requests.post('http://localhost:5000/', json=dictToSend, timeout=10)
# print('response from server:',res.text)
dictFromServer = res.json()
print('response from server:',dictFromServer["name"])