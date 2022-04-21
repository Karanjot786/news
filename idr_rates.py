import requests


url = 'https://floatrates.com/daily/idr.json'
User = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 ' \
       'Safari/537.36 '
json_data = requests.get(url).json()

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

