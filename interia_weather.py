from bs4 import BeautifulSoup as bs
import requests as r


def download_weather(link = "https://pogoda.interia.pl/polska"):
    city_list = []
    temperature_list = []
    response = r.get(link)
    soup = bs(response.text, 'html.parser')
    
    find_city = soup.find_all('span', class_='weather-map-container-list-item-name')
    find_temperature = soup.find_all('span', class_='weather-map-container-list-item-temp')
    
    for city in find_city:
        city_list.append(city.text)
        
    for temperature in find_temperature:
        temperature_list.append(temperature.text)
        
    return dict(zip(city_list, temperature_list))



def download_specific_weather(link):
    city_name = link.split("-")[2].split(",")[0]
    
    response = r.get(link)
    soup = bs(response.text, 'html.parser')
    
    temperature = soup.find('div', class_='weather-currently-temp-strict')
    perceptible_temperature = soup.find('span', class_='weather-currently-details-value')
    pressure = soup.find('span', class_= 'steady')
    wind = soup.find('span', class_= 'weather-currently-details-value')
    air_quality = soup.find('div', class_= 'value')
    return {'Miasto': city_name.capitalize(), 'temperatura': temperature.text, 'Temperatura odczuwalna': perceptible_temperature.text, 
             'Ciśnienie': ' '.join(pressure.text.split()), 'Wiatr': wind.text, 'Jakość powietrza': air_quality.text}



def long_term_weather(link):
    response = r.get(link)
    soup = bs(response.text, 'html.parser')
    
    city_name = link.split("-")[2].split(",")[0]
    
    dates = soup.find_all('span', class_= 'date')
    days_temperatures = soup.find_all('span', class_= 'weather-forecast-longterm-list-entry-forecast-temp')
    nights_temperatures = soup.find_all('span', class_= 'weather-forecast-longterm-list-entry-forecast-lowtemp')
    winds_mean = soup.find_all('span', class_ = 'weather-forecast-longterm-list-entry-wind-value')
    winds_max = soup.find_all('span', class_ = 'weather-forecast-longterm-list-entry-wind-hit')
    precipitations = soup.find_all('span', class_ = 'weather-forecast-longterm-list-entry-precipitation-value')
    numbers_of_hours_sunshine = soup.find_all('span', 'weather-forecast-longterm-list-entry-pressure-value')

    dates_list = [date.text for date in dates]
    days_temperatures_list = [day_temperature.text for day_temperature in days_temperatures]
    nights_temeratures_list = [night_temperature.text for night_temperature in nights_temperatures]
    winds_mean_list = [wind_mean.text for wind_mean in winds_mean]
    winds_max_list = [wind_max.text for wind_max in winds_max]
    precipitations_list = [precipitation.text for precipitation in precipitations]
    numbers_of_hours_sunshine_list = [number_of_hour_sunshine.text for number_of_hour_sunshine in numbers_of_hours_sunshine]

    weather_dict = {}

    for i in range(len(dates_list)):
        date = dates_list[i]
        weather_dict[date] = {
            'Miasto': city_name,
            'Pogoda w dzień': days_temperatures_list[i],
            'Pogoda w nocy': nights_temeratures_list[i],
            'Średnia prędkość wiatru': winds_mean_list[i],
            'Maksymalna prędkość wiatru': winds_max_list[i],
            'Opady': precipitations_list[i],
            'Liczba godzin słonecznych': numbers_of_hours_sunshine_list[i]
        }
    return weather_dict




