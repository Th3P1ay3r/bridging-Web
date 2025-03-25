
my_foods = ['pizza','falafel','carrot', 'cake']#source
friend_foods=my_foods[:]#start zero through the last item
my_foods.append('pepparoni pizza')
friend_foods.append('prawn pizza')

print("My fav pizza are")
for pizza in my_foods:
    print(pizza)
print('\n')
print("My firend pizza are")    
for pizza in friend_foods:
    print(pizza)
print('\n')
print('just change')