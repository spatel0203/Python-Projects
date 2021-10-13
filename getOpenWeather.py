import json, sys, requests
from pprint import pprint
APPID = '7639e7c7731b03f0d7e502ef1918a99f'
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:4])
firstUrl=f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=7639e7c7731b03f0d7e502ef1918a99f"
url=f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid=7639e7c7731b03f0d7e502ef1918a99f"
response1 = requests.get(firstUrl)
try:
    response1.raise_for_status()
except:
    raise Exception("Incorrect Location")
weatherData1=json.loads(response1.text)
response = requests.get(url)
try:
    response.raise_for_status()
except:
    raise Exception("Incorrect Location")
weatherData=json.loads(response.text)
w=weatherData["list"]
for i in range(0,40):
    if w[i]["dt_txt"][8:10] == w[i-1]["dt_txt"][8:10]:
        continue
    print(w[i]["dt_txt"] + ": ")
    print("\t" + "Description: " + w[i]["weather"][0]["description"])
    print("\t" + "Current Temp: " + str((w[i]["main"]["temp"]*1.8-459.67))[0:4] + " degrees Fahrenheit")
    print("\t" + "Feels Like: " + str((w[i]["main"]["feels_like"]*1.8-459.67))[0:4] + " degrees Fahrenheit")
    print("\t" + "Min Temp: " + str((w[i]["main"]["temp_min"]*1.8-459.67))[0:4] + " degrees Fahrenheit")
    print("\t" + "Max Temp: " + str((w[i]["main"]["temp_max"]*1.8-459.67))[0:4] + " degrees Fahrenheit")
