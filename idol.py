import requests

url = "https://raw.githubusercontent.com/haku1806/idol-image/main/idol.txt"
r = requests.get(url)
image = r.text
print(len(image))    