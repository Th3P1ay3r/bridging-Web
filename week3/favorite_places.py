favorite_places = {
    "yati": ["POL", "MDY", "Sagaing"],
    "kevin": ["YAY", "Maungmakan", "Ngapali"],
    "andrew": ["Taungyi", "Innlay", "Pintaya"],
}

for name, places in favorite_places.items():
    print(f"Name: {name}")
    for place in places:
        print("\t", place)
    print()
