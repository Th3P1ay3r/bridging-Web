# Conditional Tests in Python

# 1. Tests for equality and inequality with strings
print("apple" == "apple")  # True
print("apple" != "orange")  # True
print("Apple" == "apple")  # False

# 2. Tests using the lower() method
print("HELLO".lower() == "hello")  # True
print("WORLD".lower() == "World")  # False

# 3. Numerical tests
print(10 == 10)  # True
print(10 != 5)  # True
print(10 > 5)  # True
print(5 < 10)  # True
print(10 >= 10)  # True
print(9 <= 8)  # False

# 4. Tests using 'and' and 'or' keywords
print(5 > 2 and 10 < 20)  # True
print(5 > 10 or 10 > 5)  # True
print(5 > 10 and 10 > 5)  # False

# 5. Test whether an item is in a list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("grape" in fruits)  # False

# 6. Test whether an item is not in a list
print("grape" not in fruits)  # True
print("apple" not in fruits)  # False
