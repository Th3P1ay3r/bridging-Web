usernames = ['admin', 'jaden', 'sophia', 'mike', 'emma']
if len(usernames)==0:
    print("we need to find some users")
else:
    for user in range(0,len(usernames)):
        print(usernames.pop())
print ("after using pop function")
print(usernames)