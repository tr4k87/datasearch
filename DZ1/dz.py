import requests
import json

client_id = "YKFEPGLEPWCPY3Y5Q4SKLHIRZBS3KNJTFI5KNXBTL4SYKZZE"
client_secret = "OCZ02TQ31DC02YWRZDAMMUYHAN3XCU4FO5CO1OKRNZVKWUE0"

url = "https://api.foursquare.com/v3/places/search"

city = input("Введите название города: ")
category = input('Введите категорию ')
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": category
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3yrgVepARWJQvodetQOJ+wPmHfg/Zbt03m9i/cE58Avo="
}

response = requests.get(url, params=params,headers=headers)

if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["address"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

