import requests
from bs4 import BeautifulSoup

def scrape_weather(country, city):
    url = f"https://www.timeanddate.com/weather/{country}/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    temp = ""
    datas = soup.find_all('div', class_='bk-focus__qlook')
    for data in datas:
        temp = data.find('div', class_="h2").get_text(strip=True)
    return temp      

a = scrape_weather("pakistan","karachi")
print(a)