import requests

def get_url(city):
    # You need to obtain your api key from open weather, then give my_api_key the value of your key
    my_api_key = 'fda7542e1133fa0b1b312db624464cf5'
    unit = 'metric'    # To get temperature in Celsius
    weather_query = 'http://api.openweathermap.org/data/2.5/weather?q='
    full_query = weather_query + city + '&units=' + unit + '&APPID=' + my_api
    # This full_api_url results in smth like
    # 'http://api.openweathermap.org/data/2.5/weather?q=Nairobi&units=metric&APPID=YOUR-KEY-HERE'

    return full_query

def fetch_data(full_query):
    url = requests.get(full_query)
    # Parse the json dat so it can be used as a normal dict
    raw_data = url.json()
    # It's a good practice to always close opened urls!
    url.close()

    return raw_data

if __name__ == 'main':
    print("-------------- Know Your City's Weather -------------")
    print('Helooooooooooo')
    # Get city name from the user
    city = input("Enter your city's name: ")
