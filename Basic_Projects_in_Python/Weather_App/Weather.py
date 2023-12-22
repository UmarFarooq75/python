import requests
import json
import pyttsx3

def speak(engine, message):
    engine.say(message)
    engine.runAndWait()

def get_weather_data(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=c76df08c4b3342ce91c123621232012&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to fetch weather data for {city}. Status code: {response.status_code}")
        return None

def speak_weather_data(engine, city, temperature):
    weather_message = f"The current weather in {city} is {temperature} degrees Celsius."
    speak(engine, weather_message)

def main():
    engine = pyttsx3.init()
    
    city = input("Enter City Name: ")
    
    weather_data = get_weather_data(city)

    if weather_data:
        temperature = weather_data["current"]["temp_c"]
        speak_weather_data(engine, city, temperature)
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
