"""4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list"""

threes = list(range(3,31,3))
for three in threes:
    print(three)
    
cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(f"first ten tubes")
print(cubes)
cube_list = [value ** 3 for value in range(1,11)]
print("using list comprehension - cube list")
print(cube_list)