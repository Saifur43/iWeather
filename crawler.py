from bs4 import BeautifulSoup
import requests


def get(city_name):

    url = "https://www.timeanddate.com/weather/bangladesh/" + city_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    name_box = soup.find('div', attrs={'class': 'h2'})
    name = name_box.text.strip()
    return name

