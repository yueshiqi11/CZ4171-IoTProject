import requests

resp = requests.post("http://192.168.1.6:5000", files={'file': open('ten.jpg', 'rb')})

print(resp.text)