'''
Premier jour Python
Exercice :
    - variable
    - string
    - number
'''

# Variable

ma_premiere_varaible = "Salut le monde !"
print(ma_premiere_varaible)
ma_premiere_varaible = "J'ai faim !!!"
print(ma_premiere_varaible)

# String

citation = "Pierre Desproges dit 'Je n\'ai jamais bu du vin à outrance, d\'ailleurs je ne sais même pas où c\'est'"
print(citation)

nom = "bisoo"
print(nom.title())
print(nom.capitalize())
print(nom.upper())

prenom ="Soubika"

print(nom + " " + prenom)

nom2 = "blabla"
prenom2 = "bloblo"
phrase = nom2 + " " + prenom2 + " est vraiment très gentil"
print(phrase)

print(nom.lstrip())
print(nom.rstrip())
print(nom.strip())


# Number

def aritmetique(a, b) :
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a**b)
    
    
aritmetique(1,2)

a = 0.1
b = 0.2

print("{:.2f}".format(a+b))

def aritmetique2(a, b) :
    print("Le resultat de {} + {} est {}".format(a, b, a+b))
    print("Le resultat de {} - {} est {}".format(a, b, a-b))
    print("Le resultat de {} * {} est {}".format(a, b, a*b))
    print("Le resultat de {} / {} est {}".format(a, b, a/b))
    print("Le resultat de {} % {} est {}".format(a, b, a%b))
    print("Le resultat de {} puissance {} est {}".format(a, b, a**b))
    
aritmetique2(2,3)