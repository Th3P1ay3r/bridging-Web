# List of usernames
usernames = ['admin', 'jaden', 'sophia', 'mike', 'emma']

# Loop through usernames and print greetings
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again")