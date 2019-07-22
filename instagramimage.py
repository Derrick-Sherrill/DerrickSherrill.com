import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.instagram.com/p/Bz8RbKcgY90/'
response = requests.get(url)
soup = BeautifulSoup(response.text)

image = soup.find("meta", property="og:image")
image_url = image['content']

webbrowser.open(image_url, new=0, autoraise=True)
