from pprint import pprint
from bs4 import BeautifulSoup
import requests
import time

url = 'https://myhire.co.ke/location/car-hire-nairobi/'
ajax = 'https://myhire.co.ke/wp-admin/admin-ajax.php?orderby=new&check_single_location=is_location&action' \
       '=st_filter_cars_ajax_location&page=1&isajax_location=8&posts_per_page=8&id_location=7058 '
carToHiretext = requests.get(ajax).json()

carToHire = (carToHiretext['content'])
soup = BeautifulSoup(carToHire, 'lxml')

cars = soup.find_all('div', class_='car-type plr15')

for car in cars:
    print(car.text)
