#This Program is designed to get the current weather in Singapore from http://www.weather.gov.sg/home/
#There may be bugs here and there but I most likely will patch them
#This Program currently monitors Singapore Weather Only
import requests
from bs4 import BeautifulSoup as bs
import datetime
web = requests.get('http://www.weather.gov.sg/home/')
soup = bs(web.text, 'html.parser')

#information panel
info = soup.find('div', class_ = 'rec-obs').find_all("li")

#Highest Temperature
high = info[0].h4.text

#Lowest Temperature
low = info[2].h4.text

#Rainfall
rainfall = info[4].h4.text

#All wind info
wind = info[6].h4.text.split('&nbsp')

#Wind Direction
winddirection = wind[0]

#Wind Speed
windspeed = wind[1]+wind[2]

#All current time
alltimeinfo = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#Current Time
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(' ')[1]

#Current Date
datestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(' ')[0]

#Sky
sky = soup.find('div', class_='w-sky').find_all('p')[1].text