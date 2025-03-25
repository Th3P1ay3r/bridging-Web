# immutable object
dimensions = (200, 50) # 0 and 1
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250

my_t = (500,)
print(type(my_t))

print("original dimension")
for dimension in dimensions:
    print (dimension)

dimensions = (400, 100)
print("Modified Dimensions")
for dimension in dimensions:
    print(dimension)