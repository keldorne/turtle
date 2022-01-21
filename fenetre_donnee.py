import tkinter as tk
from tkinter import END


class FenetreDonnee(tk.Tk):
    # Constructeur
    def __init__(self):
        tk.Tk.__init__(self)
        self.nom_patient = []
        self.prenom_patient = []
        self.nom_accompagnant = []
        self.prenom_accompagnant = []
        self.telephone_accompagnant = []
        self.mail_accompagnant = []
        self.variable_sexe_patient = tk.IntVar()
        self.sexe_patient = "Homme"

        # Passage des instanciations des entrées pour les fonctions copier et clear
        self.entry_nom_patient = []
        self.entry_prenom_patient = []
        self.entry_nom_accompagnant = []
        self.entry_prenom_accompagnant = []
        self.entry_telephone_accompagnant = []
        self.entry_mail_accompagnant = []
        self.creer_fenetre()

    # Définition du bouton tout effacer
    def fenetre_clear(self):
        print("On efface les entrées")
        self.entry_nom_patient.delete(0, END)
        self.entry_prenom_patient.delete(0, END)
        self.entry_nom_accompagnant.delete(0, END)
        self.entry_prenom_accompagnant.delete(0, END)
        self.entry_telephone_accompagnant.delete(0, END)
        self.entry_mail_accompagnant.delete(0, END)

    # Définition du bouton pour copier le nom du patient dans le nom de l'accompagnant
    def enregistrer(self):
        self.nom_patient = self.entry_nom_patient.get()
        self.prenom_patient = self.entry_prenom_patient.get()
        self.nom_accompagnant = self.entry_nom_accompagnant.get()
        self.prenom_accompagnant = self.entry_prenom_accompagnant.get()
        self.telephone_accompagnant = self.entry_telephone_accompagnant.get()
        self.mail_accompagnant = self.entry_mail_accompagnant.get()
        self.destroy()

    def copier(self):
        print("On copie le nom du patient dans le nom de l'accompagnant")
        self.entry_nom_accompagnant.delete(0, END)
        self.entry_nom_accompagnant.insert(0, self.entry_nom_patient.get())

    def choix_sexe(self):
        if self.variable_sexe_patient.get() == 0:
            self.sexe_patient = "Homme"
        else:
            self.sexe_patient = "Femme"

    def creer_fenetre(self):
        # Paramètres initiaux
        self.resizable(False, False)
        self.geometry('+600+750')
        self.title('Coordonnées patient/accompagnant')

        # Création des labels
        label_nom_patient = tk.Label(self, text="Nom patient :")
        label_prenom_patient = tk.Label(self, text="Prénom patient :")
        label_nom_accompagnant = tk.Label(self, text="Nom accompagnant :")
        label_prenom_accompagnant = tk.Label(self, text="Prénom accompagnant :")
        label_telephone_accompagnant = tk.Label(self, text="Téléphone accompagnant :")
        label_mail_accompagnant = tk.Label(self, text="E-mail accompagnant :")
        label_sexe_patient = tk.Label(self, text="Sexe du patient :")

        # Création des boutons
        bouton_fin = tk.Button(self, text="Enregistrer", command=self.enregistrer)
        bouton_clear = tk.Button(self, text="Tout effacer", command=self.fenetre_clear)
        bouton_copier = tk.Button(self, text="Copier Nom.P->Nom.A", command=self.copier)
        bouton_choix_sexe_homme = tk.Radiobutton(self, text="Homme", variable=self.variable_sexe_patient, value=0,
                                                 command=self.choix_sexe)
        bouton_choix_sexe_femme = tk.Radiobutton(self, text="Femme", variable=self.variable_sexe_patient, value=1,
                                                 command=self.choix_sexe)

        # Création des entrées + récupération dans les variables de classe
        self.entry_nom_patient = tk.Entry(self, width=35)
        self.entry_prenom_patient = tk.Entry(self, width=35)
        self.entry_nom_accompagnant = tk.Entry(self, width=35)
        self.entry_prenom_accompagnant = tk.Entry(self, width=35)
        self.entry_telephone_accompagnant = tk.Entry(self, width=35)
        self.entry_mail_accompagnant = tk.Entry(self, width=35)

        # Disposition des widgets
        label_sexe_patient.grid(row=0, column=0)
        label_nom_patient.grid(row=1, column=0)
        label_prenom_patient.grid(row=2, column=0)
        label_nom_accompagnant.grid(row=3, column=0)
        label_prenom_accompagnant.grid(row=4, column=0)
        label_telephone_accompagnant.grid(row=5, column=0)
        label_mail_accompagnant.grid(row=6, column=0)

        bouton_choix_sexe_homme.grid(row=0, column=1)
        bouton_choix_sexe_femme.grid(row=0, column=2)
        self.entry_nom_patient.grid(row=1, column=1)
        self.entry_prenom_patient.grid(row=2, column=1)
        self.entry_nom_accompagnant.grid(row=3, column=1)
        self.entry_prenom_accompagnant.grid(row=4, column=1)
        self.entry_telephone_accompagnant.grid(row=5, column=1)
        self.entry_mail_accompagnant.grid(row=6, column=1)

        bouton_fin.grid(row=7, column=0)
        bouton_clear.grid(row=7, column=2)
        bouton_copier.grid(row=1, column=2)


