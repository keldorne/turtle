import shutil
import tkinter as tk
import os
from os import listdir


class FenetreDossierMaisonRetraite(tk.Tk):
    def __init__(self, chemin_calisto):
        tk.Tk.__init__(self)
        self.nom_maison_retraite = []
        self.chemin_calisto = chemin_calisto
        self.variable_etat_dossier = tk.StringVar()
        self.variable_etat_dossier.set(listdir(self.chemin_calisto))
        self.entry_maison_retraite = []
        self.label_de_letat = []
        self.creer_fenetre()

    def bouton_creer(self):
        try:
            # On cré le dossier de la Maison de  retraite dans le dossier du Calisto
            os.mkdir(self.chemin_calisto + f"\\{self.entry_maison_retraite.get()}")
            # On met à jour la fenetre
            self.nom_maison_retraite = self.entry_maison_retraite.get()
            # On enregistre le nom de la maison de retraite
            self.variable_etat_dossier.set(listdir(self.chemin_calisto))
        except:
            print("Rien n'est rempli où le dossier existe déjà")

    def bouton_effacer(self):
        # On efface tout le dossier calisto
        shutil.rmtree(self.chemin_calisto)
        # On recrée le dossier vide
        os.mkdir(self.chemin_calisto)
        self.variable_etat_dossier.set(listdir(self.chemin_calisto))

    def bouton_enregistrer(self):
        listdir_local = listdir(self.chemin_calisto)
        # On verifie que le dossier calisto contient bien uniquement un dossier de la maison de retraite
        if len(listdir_local) == 1:
            # So c'est me cas on enregistre le nom de la maison de retraite
            self.nom_maison_retraite = listdir_local[0]

        # Si il n'y a pas qu'un seul dossier où que le nom de la maison de retraite est vide on indique qu'on ne la connait pas
        elif self.nom_maison_retraite == []:
            self.nom_maison_retraite = "MR INCONNUE"

        # On ferme la fenetre
        self.destroy()

    def creer_fenetre(self):
        label_etat_dossier = tk.Label(self, text="Etat du dossier Calisto :")
        label_de_letat = tk.Label(self, textvariable=self.variable_etat_dossier)
        label_de_lentree = tk.Label(self, text="Entrez le nom de la maison de retraite")
        self.entry_maison_retraite = tk.Entry(self, width=30)
        bouton_creer = tk.Button(self, text="CREER DOSSIER", command=self.bouton_creer)
        bouton_effacer = tk.Button(self, text="EFFACER DOSSIER", command=self.bouton_effacer)
        bouton_enregistrer = tk.Button(self, text="ENREGISTRER", command=self.bouton_enregistrer)

        label_etat_dossier.grid(row=0, column=0)
        label_de_letat.grid(row=0, column=1, columnspan=2)
        label_de_lentree.grid(row=1, column=0)
        self.entry_maison_retraite.grid(row=1, column=1)
        bouton_creer.grid(row=2, column=0)
        bouton_effacer.grid(row=2, column=1)
        bouton_enregistrer.grid(row=2, column=2)