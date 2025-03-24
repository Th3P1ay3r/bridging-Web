even_numbers = list(range(2,11,2)) # start, stop, step
print(even_numbers)

num_list = [4,5,6,7,8]
num_list2 = list(range(4,9))
a_tuple= (4,)
print(type(a_tuple))
b_tuble=tuple([4,5,6])

squares = []
tubes =[]
for value in range(1,11): #generate number sequences 1 through 10
    square = value ** 2
    squares.append(square)
    
print(f"square list\n  {squares}")
print(f"cube list \n{tubes}")
#list comprehension - generate the smae list in one line of code

square_list = [value **2 for vlaue in range(1,11)]
print(square_list)