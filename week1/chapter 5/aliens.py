alien_colors = ['red', 'green', 'yellow']

# alien_color= input("enter alien colort")
for color in alien_colors:
    if color=='green':
        print("You earned 5 points")
    else:
        print("you fail shoting")

for color in alien_colors:
    if color == 'green':
        print("you earned 5 points.")
    elif color == 'yellow':
        print("you earned 10 points")
    else:
        print("you earned 15 points")