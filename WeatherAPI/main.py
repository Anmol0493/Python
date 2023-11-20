import requests
import json

YOUR_API_KEY = "deaac00dc4934aacaf285838232807"

city = input("Enter name of city: ")

url = f"http://api.weatherapi.com/v1/current.json?key={YOUR_API_KEY}&q={city}"

result = requests.get(url)
weatherDict = json.loads(result.text)
print(weatherDict["current"]["temp_c"])