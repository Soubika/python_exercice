###################### More Function ######################

### Default argument values ###

# Games

def games(name = "chess"):
    print("I like playing {}".format(name))

games("switch")
games("snes")
games()

# Favorite Movie

def movies(name = "The Princess Bride"):
    print("My favorite movie is {}".format(name))

movies("Orgueil et Prejugé")
movies("Harry Potter")
movies()

### Position arguments ###

# Favorite Colors

def favorite_color(name = "Jane", color = "Blue"):
    print("{}'s favorite color is {}".format(name, color))

favorite_color("Soubika", "red")
favorite_color("Kessy", "blue")
favorite_color("Cynthia", "pink")

# Phones

def phone_model(phone, model):
    print("{} - {}".format(phone, model))

phone_model("xiaomi", "pocoX3")
phone_model("samsung", "s21")
phone_model("huawei ", "p30")

### Keyword arguments ###

# Sports Teams

def city_sport(city_name = None, sport_name = None):
    print("{} - {}\n".format(city_name, sport_name))

city_sport()
city_sport("Paris", "Judo")
city_sport(city_name="Nancy", sport_name="natation")
city_sport(sport_name="badminton", city_name="Rennes")
city_sport(city_name="Strasbourg")
city_sport(sport_name="Volley-ball")


# World Lannguage

def country_language(country, language = None):
    print("{} - {}".format(country, language))

country_language("France", "français")
country_language(country="Ile Maurice", language="créole")
country_language("Allemagne")

