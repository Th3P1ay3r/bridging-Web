users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFullname : {full_name.title()}")
    print(f"\tLocation: {location.title()}")

person_info = {
    "person1": {"userid": "00111", "email": "albert@gmial.com", "city": "london"},
    "person2": {"userid": "0000112", "email": "paul@gmial.com", "city": "Newyork"},
    "person3": {"userid": "000113", "email": "kevin@gmail.com", "city": "Aukland"},
}

print("*" * 80)  # replicating star
print(person_info)
print("*" * 80)

for person_name, person_info in person_info.items():
    print(person_name)
    for key, value in person_info.items():
        print(f"\t{key} {value}")
