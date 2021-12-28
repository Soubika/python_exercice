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

mountains = {
    "Everest" : [8848, 29028],
    "Aconcagua" : [6959, 22831],
    "Denali" : [6190, 20308],
    "Kilimandjaro" : [5892, 19330],
    "Elbrouz" : [5892, 19330]
    }


for montain in mountains.keys():
    print(montain)


for montain in mountains.values():
    print(montain[0])

for montain in mountains.values():
    print(montain[1])

for key, values in mountains.items():
    print("{} is {} meters tall, or {} feet".format(key, values[0], values[1]))

# Mountain Heights 4

mountains = {
    "Everest" : {'elevation': 8848, "range" : "Himalaya"},
    "Aconcagua" : {'elevation': 6959, "range" : "Cordillère des Andes"},
    "Denali" : {'elevation': 6190, "range" : "Chaîne d'Alaska"},
    "Kilimandjaro" : {'elevation': 5892, "range" : "Vallée du Grand Rift"},
    "Elbrouz" : {'elevation': 5892, "range" : "Caucase"},
    }


for k in mountains.keys():
    print("name : {}".format(k))



### Overall Challenges ###
