favorite_numbers = {
    "marie": [1, 2, 3, 4, 7, 9],
    "theingi": [2, 5, 6],
    "shweyi": [1, 2, 3, 4],
    "bob": [5, 6, 7],
}

for user in favorite_numbers.keys():
    print(f"{user}'s favorite numbers:")
    for number in favorite_numbers[user]:  # Removed .values() since it's a list
        print(number, end=" ")
    print("\n")  # Newline after each user's numbers
