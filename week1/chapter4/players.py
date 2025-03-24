players = ['charles','martina', 'micheal', 'florence', 'eli']
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])
some_player =(players[0:3])# starting at index 0 and stops at index 3 (0,1,2)

print(some_player)
print(players[1:4])

#below statement is like players[0:4]
print(players[:4]) #skipping start index means it will use default start index 0
print(players[2:]) #omitting stop index means it will work through the last item

print(players[-3:])

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())