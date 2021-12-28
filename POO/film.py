class Film :
    def __init__(self, name):
        self.name = name
    
    def watch(self):
        print("bon visionnage !")
    
class FilmCasette(Film):
    pass

film = Film("blablabla")
film_cassette = FilmCasette("blobloblo")

print(film.name)
print(film.watch())

film_cassette.name
film_cassette.watch()

