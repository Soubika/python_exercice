from abc import ABC
from datetime import datetime


class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def display(self):
        print("Fichier : {}".format(self.name))
    
class Image(File):
    
    def display(self):
        print("Fichier image : {}".format(self.name))
        
class GIF(Image):
    
    
    def display(self):
        super().display()
        print("L'image est un GIF")

class JPG(Image):
    
    def display(self):
        super().display()
        print("L'image est un JPG")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        print("L'utilisateur {} s'est connecté".format(self.username))

    def post(self, thread, content, file= None):
        if file:
            post = FilePost(self, str(datetime.now()), content, file)
        else:
            post=Post(user=self, time_posted=str(datetime.now()), content=content)

    def make_thread(self, title, content):
        post = Post(self, str(datetime.now()) , content)
        return Thread(title, str(datetime.now()), post)

    def __str__(self):
        return self.username
    
class Moderator(User):
    
    def edit(post, content):
        post.content = content

    def delete(thread, post):
        index = thread.posts.index(post)
        del thread.posts[index]
    
class Post :
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content
        
    def display(self):
        print("Message posté par {} le {} : {}".format(self.user, self.time_posted, self.content))
    
class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file
    
    def display(self):
        super().display()
        print("pièce jointe")
        self.file.display()


class Thread:
    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]
    
    def display(self):
        print("-----------THREAD-----------")
        print("titre : {}, date : {}".format(self.title, self.time_posted))
        print()
        for post in self.posts:
            post.display()
            print()
        print("----------------------------")
        
        def add_post(self, post):
            self.posts.append(post)
    
    
nom_utilisateur = User("Soubika", "azerty")
print(nom_utilisateur)
nom_moderator = Moderator("Jean", "qsdfg")
print(nom_moderator)

livre = nom_utilisateur.make_thread("Les livres c'est la vie", "J'ai envie de continuer mon livre !!!!")
livre.display()
nom_moderator.post(livre, "ok !")
livre.display()





'''
st = Post("Soubika", "20/12/2021", "J'ai envie de lire !!!!!!!")
nouveau_post.display()
reponse = Moderator.edit(nouveau_post, "Tu devrais manger si tu as faim")
reponse.super().display()'''




























