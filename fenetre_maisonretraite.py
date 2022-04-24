import shutil
import tkinter as tk
import os
from os import listdir
from pathlib import Path
from ttkthemes import ThemedStyle
from tkinter import ttk
import pickle
from fonctiondekev import showMessage

class FenetreDossierMaisonRetraite(tk.Tk):
    def __init__(self, chemin_calisto):
        tk.Tk.__init__(self)
        self.nom_maison_retraite = []
        self.chemin_calisto = Path(chemin_calisto)
        self.variable_etat_dossier = tk.StringVar()
        self.variable_etat_dossier.set(listdir(self.chemin_calisto))
        self.entry_maison_retraite = []
        self.label_de_letat = []
        self.type_depistage =[]
        self.mode_recuperation = int()
        self.creer_fenetre()

    def bouton_recuperation(self):
        try:
            # On charge l'ancien nom de retraite enregistré
            sauvegarde_maison_retraite = pickle.load(open("files/maison_retraite.dat", "rb"))
            # On compare la sauvegarde avec le nom du dossier actuel
            if listdir(self.chemin_calisto)[0] == sauvegarde_maison_retraite:
                self.mode_recuperation = 1
                self.nom_maison_retraite = sauvegarde_maison_retraite
                self.destroy()
            else:
                print("Recuperation impossible le nom de la maison de retraite ne corespond pas")
                showMessage("Recuperation impossible le nom de la maison de retraite ne corespond pas", 'warning')
        except:
            print("Il n'y a pas de sauvegarde de maison de retraite")
            showMessage("Il n'y a pas de sauvegarde de maison de retraite correspondante", 'warning')


    def bouton_creer(self):
        print(self.entry_maison_retraite.get())
        if self.entry_maison_retraite.get() == "":
            showMessage("Veuillez entrer un nom d'établissement", 'warning')
        elif not self.entry_maison_retraite.get() == "" and len(listdir(self.chemin_calisto)) >= 1:
            showMessage("Il ne doit y avoir qu'un établissement", 'warning')
        else:
            try:
                self.nom_maison_retraite = "MR "+ self.entry_maison_retraite.get().upper()
                # On cré le dossier de la Maison de retraite dans le dossier du Calisto
                os.mkdir(Path(self.chemin_calisto, self.nom_maison_retraite))
                # On enregistre le nom de la maison de retraite
                self.variable_etat_dossier.set(listdir(self.chemin_calisto))
                pickle.dump(self.nom_maison_retraite, open("files/maison_retraite.dat", "wb"))
            except:
                print("le dossier existe déjà")
                showMessage("Le dossier existe déjà", 'warning')

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
            # Si c'est me cas on enregistre le nom de la maison de retraite
            self.nom_maison_retraite = listdir(self.chemin_calisto)[0]
            print(self.nom_maison_retraite)
            self.mode_recuperation = 0
            self.destroy()

        # Si il n'y a pas qu'un seul dossier où que le nom de la maison de retraite est vide on indique qu'on ne la connait pas
        elif self.nom_maison_retraite == []:
            showMessage("Veuillez entrer un nom d'établissement", 'warning')

        # On ferme la fenetre


    def creer_fenetre(self):

        # Theme fenetre
        #self.title(bg = "white")
        style = ThemedStyle(self)
        style.theme_use('equilux')
        bg = style.lookup('TLabel', 'background')
        fg = style.lookup('TLabel', 'foreground')
        self.configure(bg=style.lookup('TLabel', 'background'))

        label_etat_dossier = ttk.Label(self, text="Etat du dossier Calisto :")
        label_de_letat = ttk.Label(self, textvariable=self.variable_etat_dossier)
        label_de_lentree = ttk.Label(self, text="Entrez le nom de la maison de retraite")
        label_separateur = ttk.Label(self, text="__________________________________________________________________________________________________")
        self.entry_maison_retraite = ttk.Entry(self, width=30)
        bouton_creer = ttk.Button(self, text="CREER DOSSIER", command=self.bouton_creer)
        bouton_effacer = ttk.Button(self, text="EFFACER DOSSIER", command=self.bouton_effacer)
        bouton_enregistrer = ttk.Button(self, text="ENREGISTRER", command=self.bouton_enregistrer)
        bouton_recuperation = ttk.Button(self, text="RECUPERER SESSION PRECEDENTE INTERROMPUE",
                                         command=self.bouton_recuperation)

        label_etat_dossier.grid(row=0, column=0)
        label_de_letat.grid(row=0, column=1, columnspan=2)
        label_de_lentree.grid(row=1, column=0)
        self.entry_maison_retraite.grid(row=1, column=1)
        bouton_creer.grid(row=2, column=0)
        bouton_effacer.grid(row=2, column=1)
        bouton_enregistrer.grid(row=2, column=2)
        label_separateur.grid(row=3, columnspan=3)
        bouton_recuperation.grid(row=4, columnspan=3)

"""
chemin_calisto = Path(Path(__file__).parent.absolute(), "mode_test", "DocumentCalisto")
chemin_liste_referent = Path(Path(__file__).parent.absolute(), "mode_test", "fichier_test", "Liste Referents.xlsx")
dossier_sauvegarde = Path(Path(__file__).parent.absolute(), "mode_test", "Depistages")
app1 = FenetreDossierMaisonRetraite(chemin_calisto)
app1.mainloop()
"""
