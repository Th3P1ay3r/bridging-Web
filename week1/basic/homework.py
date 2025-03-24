name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "Eric"

print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")
print(f"Title Case: {name.title()}")

author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{author} once said, "{quote}"')

famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{famous_person} once said, "{quote}"'
print(message)

name = "\t  John Doe  \n"  # Name with leading tab and trailing newline

print("Original name with whitespace:")
print(f"'{name}'")  # Showing whitespace clearly

# Stripping functions
print("\nUsing lstrip():")
print(f"'{name.lstrip()}'")  # Removes leading whitespace

print("\nUsing rstrip():")
print(f"'{name.rstrip()}'")  # Removes trailing whitespace

print("\nUsing strip():")
print(f"'{name.strip()}'")  # Removes both leading and trailing whitespace

filename = "python_notes.txt"
filename_without_extension = filename.removesuffix(".txt")

print(filename_without_extension)
