import requests
import pyttsx3
import speech_recognition as sr

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_city_by_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please tell me the city name")
        print("Listening...")
        audio = r.listen(source)

    try:
        city = r.recognize_google(audio)
        print(f"City: {city}")
        return city
    except:
        speak("Sorry, I couldn't understand")
        return None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        speak("City not found")
        return

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    result = f"The temperature in {city} is {temp} degree Celsius with {description}"
    print(result)
    speak(result)

if __name__ == "__main__":
    speak("Hello, I am your weather assistant")

    choice = input("Type or Speak? (t/s): ").lower()

    if choice == "s":
        city = get_city_by_voice()
    else:
        city = input("Enter city name: ")

    if city:
        get_weather(city)
