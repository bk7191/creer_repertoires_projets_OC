# coding: utf-8

import os

repertoire_de_travail = r"C:\Users\xxxx\PycharmProjects\projet"

for i in range(5,12):
    creer = "{0}_{1}".format(repertoire_de_travail, str(i))
    i+=1
    if not os.path.exists(creer):
        os.makedirs(creer)
