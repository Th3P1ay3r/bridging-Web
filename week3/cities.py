cities = {
    "yangon": {
        "country": "myanmar",
        "population": 5.1,
        "fact": "Home to the Shwedagon Pagoda, a 2,500-year-old golden stupa.",
    },
    "bangkok": {
        "country": "thailand",
        "population": 11.23,
        "fact": "Known for its vibrant street food scene and over 400 temples.",
    },
    "tokyo": {
        "country": "japan",
        "population": 37.1,
        "fact": "The world's most populous metropolitan area.",
    },
    "aukland": {
        "country": "new zealand",
        "population": 1.71,
        "fact": "Nicknamed the 'City of Sails' due to its large number of yachts.",
    },
    "toranto": {
        "country": "canada",
        "population": 2.8,
        "fact": "Hosts the tallest free-standing structure in the Western Hemisphere, the CN Tower.",
    },
}

# for city, details in cities.items():
#     print(f"\nCity: {city.title()}")
#     print("-" * 20)
#     print(f"Country: {details['country'].title()}")
#     print(f"Population: {details['population']} million")
#     print(f"Fun Fact: {details['fact']}")

for city, info in cities.items():
    print(f"{city}'s information")
    for k, v in info.items():
        print(f"\t{k} {v}")
    print()