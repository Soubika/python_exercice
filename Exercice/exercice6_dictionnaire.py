###################### Dictionaries ######################

### What are dictionaries ? ###

# Pet Names

pets = {
    "pancake" : "dog",
    "cake" : "snake",
    "butter" : "cat"
}

for name, pet in pets.items():
    print("{} is a {}".format(name, pet))

# Polling Friends

manga = "what is your favorite manga ?"

question = {
    "Dean" : "I like the most 'One Piece'",
    "Sam" : "I think I like 'DBZ",
    "Castiel" : "I don't like any manga"
    }

for name, response in question.items():
    print("{}, {}".format(name,manga))
    print("{}\n".format(response))

### Common operations with dictionaries ###

#Pet Names 2

def name_pet(dictionnaire):
    for name, pet in dictionnaire.items():
        print("{} is a {}".format(name, pet))
    print("-----")

pets2 = {
    "pancake" : "dog",
    "cake" : "snake",
    "butter" : "cat"
}

name_pet(pets2)
pets2["cake"] = "python"
name_pet(pets2)
pets2["honey"] = "bear"
name_pet(pets2) 
del pets2['cake']

# Weight Lifting

def weight_lifting(dico):
    for name, number in dico.items():
        print(" I did {} {}".format(number, name))
    print("-----")

exercice = {
    "bench presses" : 10,
    "push-up" : 15,
    "squats" : 20,
    "dead lift" : 25,
    "pull-ups" : 30,
    "curls" : 35
}

weight_lifting(exercice)
exercice["squats"] = 50
weight_lifting(exercice)
exercice["dips"] = 40
weight_lifting(exercice) 
del exercice['pull-ups']

### Looping through a dictionary ###

# Mountain Heights

mountains = {
    "Everest" : 8848,
    "Aconcagua" : 6959,
    "Denali" : 6190,
    "Kilimandjaro" : 5892,
    "Elbrouz" : 5892
    }

print("There the five tallest Mountains of the world\n")
for name in mountains:
    print("{}".format(name))
    
print("----------\n\nThere the five size of the five tallest mountains of the world\n")
for elevation in mountains.values():
    print("{}".format(elevation))
    
print("----------\n\nThere the five tallest Mountains of the world with their size\n")   
for name, elevation in mountains.items():
    print("{} is {} meters tall".format(name, elevation))

# Mountain Heights 2

mountains = {
    "Everest" : 8848,
    "Aconcagua" : 6959,
    "Denali" : 6190,
    "Kilimandjaro" : 5892,
    "Elbrouz" : 5892
    }

print("There the five tallest Mountains of the world alphabetically\n")
for name in sorted(mountains):
    print("{}".format(name))
    
print("----------\n\nThere the five size of the five tallest mountains of the world alphabetically\n")
for name, elevation in sorted(mountains.items()):
    print("{}".format(elevation))
    
print("----------\n\nThere the five tallest Mountains of the world with their size alphabetically\n")   
for name, elevation in sorted(mountains.items()):
    print("{} is {} meters tall".format(name, elevation))

### Nesting ###

# Mountain Heights 3


# Mountain Heights 4




### Overall Challenges ###
