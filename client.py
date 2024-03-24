import requests

response = requests.post(
    "http://localhost:8000/poem/invoke",
    json = {'input':{'topic':"My best friend"}})

print(response.json()['output']['content'])