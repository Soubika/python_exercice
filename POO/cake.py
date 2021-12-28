# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:13:22 2021

@author: Soubika
"""

class Cake :
    def __init__(self, flavor):
        self.flavor = flavor
        print("le gateau est : {}".format(flavor))
    
    
    def cut_in_part(self):
        print("le gâteau est coupé en 4 parts")

cake = Cake("chocolate")
print(cake.flavor)
cake.cut_in_part()
cake2 = Cake("Banana")
print(cake2.flavor)
