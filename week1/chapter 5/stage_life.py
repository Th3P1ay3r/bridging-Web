age = int(input("enter your age"))
print(type(age))

if age<2:
    print("you are a baby")
    
elif age>=2 and age<4:
    print("you are a tolder")
    
elif age>=4 and age <13:
    print("you are a kid")

elif age>=13 and age<20:
    print("you are a teneager")
    
elif age>20 and age<65:
    print("you are a adult")
    
else:
    print("you are elder")