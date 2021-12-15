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

### Looping through a dictionary ###

### Nesting ###

### Overall Challenges ###
