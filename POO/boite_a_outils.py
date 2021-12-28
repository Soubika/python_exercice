# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:18:02 2021

@author: Soubika
"""

class Boite_outils:
    def __init__(self):
        self.tools = []
        
    def add_tools(self, tool):
        self.tools.append(tool)
    
    def remove_tools(self, tool):
        index = self.tools.index(tool)
        del self.tools[index]


class Hammer:
    def __init__(self, color):
        self.color = color
    
    def paint(self, color):
        self.color = color
    
    def hammer_in(self, nail):
        nail.hammer_in()
    
    def remove(self, nail):
        nail.remove()

class Screwdriver:
    def __init__(self, size):
        self.size = size
    
    def tighten(self, screw):
        screw.tighten()
    
    def loosen(screw):
        screw.loosen()

class Screw:
    """Vis."""
     
    MAX_TIGHTNESS = 5
    
    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0
    
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1
    
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""
    
    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True
    
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."