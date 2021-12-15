###################### If Statements ######################

### Logical tests ###

# True and False

print(1 == 1)
print(1 != 2)
print(2 < 3)
print(2 <= 2)
print(9 >= 6)

print(1 != 1)
print(1 == 2)
print(2 > 3)
print(2 < 2)
print(9 < 6)

### The if-elif...else chain ###

# Three is a Crowd

def crowd_test(name):
    if len(name) > 3 :
        print("room being crowed")
    

nom = ["Claude", "Ugo", "Loic", "Alexandra"]

crowd_test(nom)
nom.pop()
crowd_test(nom)

# Three is a Crowd - Part 2

def crowd_test2(name):
    if len(name) > 3 :
        print("room being crowed")
    else :
        print("not so many people finally")
    

nom2 = ["Claude", "Ugo", "Loic", "Alexandra"]

crowd_test2(nom2)
nom2.pop()
crowd_test2(nom2)

# Six is a Mob

def crowd_test3(name):
    if len(name) > 5 :
        print("room being mob, there are {} person(s)".format(len(name)))
    elif len(name) <= 5 and len(name) >= 3 :
        print("room being crowed, there are {} person(s)".format(len(name)))
    elif len(name) == 1 or len(name) == 2 :
        print("room not being crowded, there are {} person(s)".format(len(name)))
    else :
        print("room being empty, there are {} person(s)".format(len(name)))
    

nom3 = ["Claude", "Ugo", "Loic", "Alexandra", "Namadia", "Clémence"]

crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)
nom3.pop()
crowd_test3(nom3)


### Overall Challenges ###

def calcul_point(liste_alien):
    somme = 0
    for i in liste_alien:
        if i == "red":
            somme = somme + 5
        elif i == "green":
            somme = somme + 10
        else:
            somme = somme + 20
    print(somme)

alien = ["red", "blue", "blue","red", "green", "blue","red", "green", "blue", "blue"]

calcul_point(alien)
