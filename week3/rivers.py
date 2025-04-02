rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "ayeyarwady": "myanmar",
    "thanlwin": "myanmar",
    "mekoung": "thai",
}
for river, country in rivers.items():
    print(f"{river.title()} run through {country.title()}.")

print("\nRivers")
for river in rivers:
    print(river)

print("\nCountries")
for country in rivers.values():
    print(country)
