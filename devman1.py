import requests

# Урок 1, шаг 3
url = 'https://wttr.in'
response = requests.get(url)
response.raise_for_status()
print(response.text)

# Урок 1, шаг 4
url_template = 'https://wttr.in/{}'
url = url_template.format('svo')
response = requests.get(url)
response.raise_for_status()
print(response.text)

url_template = 'https://wttr.in/{}'
url = url_template.format('london')
response = requests.get(url)
response.raise_for_status()
print(response.text)

url_template = 'https://wttr.in/{}'
url = url_template.format('Череповец')
response = requests.get(url)
response.raise_for_status()
print(response.text)

# Урок 1, шаг 5
url_template = 'https://wttr.in/{}'
url = url_template.format('Череповец?lang=ru&?M&?n&?q?T')
response = requests.get(url)
response.raise_for_status()
print(response.text)