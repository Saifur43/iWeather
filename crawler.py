from bs4 import BeautifulSoup
import requests
import urllib


def get(city_name):

    url = "https://www.timeanddate.com/weather/bangladesh/" + city_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    name_box = soup.find('div', attrs={'class': 'h2'})
    name = name_box.text.strip()
    return name


def get_img(city_name):
    url = "https://www.timeanddate.com/weather/bangladesh/" + city_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    img = soup.find('img', attrs={'id': 'cur-weather'})
    img_a = img.get('src')
    img_c = "http://" + str(img_a[2:])
    name = "images/weather.png"
    urllib.request.urlretrieve(img_c, name)