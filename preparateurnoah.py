#Programme qui permet prépare l'utilisation du programme permettant de gérer les rapports de dépistage

# coding: utf-8
import tkinter as tk


import pyautogui
import preparateur_fenetre
from pynput.keyboard import *
duree = 0.1

"""
fenetre = preparateur_fenetre.PreparateurNoah()
fenetre.mainloop()

if fenetre.lancement == 0:
    exit()
"""


def press_on(key):
    if key == Key.f7:
        print(pyautogui.position())

with Listener(on_press=press_on) as listener:
    listener.join()

"""
# On clique sur la barre de recherche
pyautogui.click(90, 1060)
time.sleep(duree)
# On écrit noah
keyboard.write("noah")
time.sleep(duree)
# On allume NOAH
pyautogui.click(215, 510)
time.sleep(5)
# On selectionne OK
pyautogui.click(915, 650)
time.sleep(5)
# On selectionne parcourir patient
pyautogui.click(40, 175)
time.sleep(duree)
# On rentre le nom test
keyboard.write("configuration")
time.sleep(duree)
# On selectionne le patient test
pyautogui.click(55, 340)
time.sleep(duree)
# On demarre calisto
pyautogui.click(95, 75)
time.sleep(duree)
"""