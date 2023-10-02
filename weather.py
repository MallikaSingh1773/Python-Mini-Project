import requests

city = input("Enter the name of the city:\n")

url = f"http://api.weatherapi.com/v1/current.json?key=3f893cf71e1c4fc1bcf121206230709&q={city}&aqi=no"
try:
    response = requests.get(url)
    response.raise_for_status()  

    weather_data = response.json()

    if 'error' in weather_data:
        print(f"Error: {weather_data['error']['message']}")
    else:
        location = weather_data['location']
        current = weather_data['current']

        print(f"Weather in {location['name']}, {location['region']}, {location['country']}:")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Wind Speed: {current['wind_kph']} km/h")
        print(f"Relative Humidity: {current['humidity']}%")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except KeyError:
    print("Invalid response format. Please check your API request.")
