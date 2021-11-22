weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])
weather["temperature"] = int(weather["temperature"]) - 5
print(weather)
print(weather.get('country', 'Россия'))
weather['date'] = "27.05.2019"
print(weather)
print(len(weather))
