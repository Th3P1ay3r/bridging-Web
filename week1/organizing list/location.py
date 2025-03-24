"""3-8. Seeing the World: Think of at least five places in the world you’d like
to visit.
•
Store the locations in a list. Make sure the list is not in alphabetical order.
•
Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list"""

locations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney']
print(locations)    #printing raw python list
# use temporary sorted() function without affecting the original list
print(sorted(locations))    #printing sorted list

print(f"Original list: \n {locations}")    #printing original list

locations.reverse()
print(f"reverse order of lists: \n {locations}")  

locations.reverse()
print(f"second time reverse order of lists: \n {locations}")

locations.sort() 
print(f"after sorting in alphabetical order \n {locations}")

locations.sort(reverse=True)
print(f"after sorting in reverse alphabetical order \n {locations}")

print(f"Length of the list is {len(locations)}")    #printing length of the list

print(locations[-6]) #index starts from -1 to -5

