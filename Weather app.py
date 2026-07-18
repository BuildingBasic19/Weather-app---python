import requests
import json 

def weather_call():
    api_key = "paste_your_API_key"
    city = "Delhi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    responce = requests.get(url)
    data = responce.json()
    
    temprature = data["main"] ["temp"]
    wind_speed = data["wind"]["speed"]
    return temprature, wind_speed, city

def main ():
    try:
        temprature , wind_speed , city  = weather_call()
        print(f"temprature of {city} is {temprature} and windspeed is {wind_speed}")
    except Exception as e:
        print("requested information was not found")
    
    
if __name__ == "__main__":
     main()