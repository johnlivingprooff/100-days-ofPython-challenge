#!/usr/bin/python3

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country = {}
    for key, value in travel_log[0].items():
        if key == "country":
            new_country[key] = country
        elif key == "visits":
            new_country[key] = visits
        elif key == "cities":
            new_country[key] = cities

    travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



