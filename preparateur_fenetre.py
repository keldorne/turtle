# coding: utf-8
import shutil
import tkinter as tk
import os
from os import listdir
from pathlib import Path
from ttkthemes import ThemedStyle
from tkinter import ttk

class PreparateurNoah(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.lancement = int()
        self.creer_fenetre()

    def bouton_poursuivre(self):
        self.lancement = 1
        self.destroy()

    def bouton_annuler(self):
        self.lancement = 0
        self.destroy()

    def creer_fenetre(self):

        # Theme fenetre
        #self.title(bg = "white")
        style = ThemedStyle(self)
        style.theme_use('equilux')
        bg = style.lookup('TLabel', 'background')
        fg = style.lookup('TLabel', 'foreground')
        self.configure(bg=style.lookup('TLabel', 'background'))

        label_l1 = ttk.Label(self, text="Ce programme permet de prépare l'utilisation de l'aide à l'écriture des rapports de dépistage")
        label_l1et1 = ttk.Label(self, text="_________________________________________________________________")
        label_l2 = ttk.Label(self,text="Attention prérequis avant de le lancer ! ! ! ! ! ! ! !")
        label_l3 = ttk.Label(self, text="-> Régler la résolution à 1920 x 1080")
        label_l4 = ttk.Label(self, text="-> Régler la mise à l'échelle à 100%")
        label_l5 = ttk.Label(self, text="-> Allumer Calisto en plein écran et ne rien toucher pendant l'éxécution")
        label_l6 = ttk.Label(self, text="_________________________________________________________________")
        bouton_poursuivre = ttk.Button(self, text="Poursuivre", command=self.bouton_poursuivre)
        bouton_annuler = ttk.Button(self, text="Annuler", command=self.bouton_annuler)

        label_l1.grid(row=0, column=1)
        label_l1et1.grid(row=1, column=1)
        label_l2.grid(row=2, column=1)
        label_l3.grid(row=3, column=1)
        label_l4.grid(row=4, column=1)
        label_l5.grid(row=5, column=1)
        label_l6.grid(row=6, column=1)
        bouton_annuler.grid(row=7, column=0)
        bouton_poursuivre.grid(row=7, column=2)


"""
chemin_calisto = Path(Path(__file__).parent.absolute(), "mode_test", "DocumentCalisto")
chemin_liste_referent = Path(Path(__file__).parent.absolute(), "mode_test", "fichier_test", "Liste Referents.xlsx")
dossier_sauvegarde = Path(Path(__file__).parent.absolute(), "mode_test", "Depistages")
app1 = FenetreDossierMaisonRetraite(chemin_calisto)
app1.mainloop()
"""


