import requests

resp = requests.post("http://localhost:5000/disease/dog", files={'file': open('test3.jpg', 'rb')})

print(resp.json())