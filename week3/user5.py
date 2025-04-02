users = [
    {
        "username": "aeinstein",
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    {
        "username": "mcurie",
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
    {
        "username": "elonmusk",
        "first": "elon",
        "last": "musk",
        "location": "washinton D.C",
    },
    {
        "username": "dtrump",
        "first": "donald",
        "last": "trump",
        "location": "washinton D.C",
    },
    {
        "username": "jbiden",
        "first": "joe",
        "last": "biden",
        "location": "washinton D.C",
    },
]

# Improved formatting
for user in users:
    print("\nUser Profile:")
    print("-" * 20)
    for key, value in user.items():
        formatted_key = key.replace("_", " ").title()
        formatted_value = value.title()
        print(f"{formatted_key}: {formatted_value}")
