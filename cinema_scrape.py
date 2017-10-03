from bs4 import BeautifulSoup
import requests
from pprint import pprint

week_dict = {}

gym_name = input("Enter gym name please : ")
full_url = "http://www.goldsgym.com/" + gym_name + '/cardio-cinema-schedule/'

page = requests.get(full_url)
soup = BeautifulSoup(page.text, "lxml")

cardio_table = soup.find('table', attrs={'id': 'tbl_cardio_cinema'})

for tr in cardio_table.find_all('tr'):
    data = tr.find_all('td')

    date_data = data[0].text.split()
    date_as_string = date_data[1]
    day_of_week = date_data[0]

    day_dict = {}
    day_dict['date'] = date_as_string
    day_dict['morning'] = data[1].text.strip()
    day_dict['afternoon'] = data[2].text.strip()
    day_dict['evening'] = data[3].text.strip()

    week_dict[day_of_week] = day_dict

pprint(week_dict)
