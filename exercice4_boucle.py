###################### While Loopes and Input ######################

### What is a while loop ? ###

# Growing Strength

strength = 5
print("The player begin with {} of strength\n".format(strength))
while strength < 10:
    print("The player has currently {}".format(strength))
    strength = strength + 1
    print("The player has {} of strength\n".format(strength))
    
print("The player is too strong and move up to a new level of this game")

### Accepting user input ###

# Game Preferences

games = ["Zelda", "Ori", "Final Fantasy", "Donkey Kong Country"]

new_game = input("What game do you play ?")
games.append(new_game)

for i in games :
    print(i)

### Using while loops to keep your programs running ###

games = ["Zelda", "Ori", "Final Fantasy", "Donkey Kong Country"]

new_game = input("What game do you play ?")
while new_game != "quit":
    new_game = input("What game do you play ?")
    if new_game != "quit":
        games.append(new_game)

print("The list of the games :")
for i in games:
    print("\t- {}".format(i))

### Overall Challenges ###

gauss_addition = list(range(1,101))

somme = 0
pop_first = 0
pop_final = 0

while len(gauss_addition) > 0:
    pop_first = gauss_addition.pop(0)
    pop_final = gauss_addition.pop()
    somme = somme + pop_first + pop_final
    
print(somme)