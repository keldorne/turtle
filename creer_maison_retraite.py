import tkinter as tk
from pathlib import Path
from ttkthemes import ThemedStyle
from tkinter import ttk
from tkinter import END
import sqlite3
from Google import create_service

class fenetreCreationContact(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.nom_maison_retraite = str()
        self.nom_cadre_sante = str()
        self.numero_telephone = str()
        self.adresse_postale = str()
        self.adresse_email = str()
        self.creer_fenetre()

    def bouton_enregistrer(self):
        try:
            self.nom_maison_retraite = "MR " + self.entry_nom_maison_retraite.get().upper()
            self.nom_cadre_sante = self.entry_nom_cadre_sante.get().upper()
            self.numero_telephone = self.entry_numero_telephone.get()
            self.adresse_postale = self.entry_adresse_postale.get()
            self.adresse_email = self.entry_adresse_email.get()
        except:
            print("Erreur d'enregistrement dans la classe")

        # On enregistre dans la base de donnée
        connection = sqlite3.connect("test3.db")
        try:
            connection = sqlite3.connect("test3.db")
            cursor_maison_retraite = connection.cursor()
            cursor_referent = connection.cursor()
            db_maison_retraite = (cursor_maison_retraite.lastrowid, self.nom_maison_retraite, self.adresse_postale)
            cursor_maison_retraite.execute('INSERT INTO INFO_MAISON_RETRAITE VALUES(?,?,?)', db_maison_retraite)
            id_maison_retraite = cursor_maison_retraite.lastrowid

            db_referent = (cursor_referent.lastrowid, id_maison_retraite, 2, self.nom_cadre_sante, "", "",
                           self.numero_telephone, self.adresse_email)
            cursor_referent.execute('INSERT INTO INFO_HUMAIN VALUES(?,?,?,?,?,?,?,?)', db_referent)
            id_referent = cursor_referent.lastrowid
            connection.commit()
            connection.close()
            print("enregistrement réussi")
        except Exception as e:
            print("erreur enregistrment base de donnée", e)
            connection.rollback()
            connection.close()

        # On enregistre le contact sur google contacts
        # Paramètres d'authentification
        CLIENT_SECRET_FILE = Path("tolkienetjason", "client_creercontact.json")
        API_NAME = 'people'
        API_VERSION = 'v1'
        SCOPES = ['https://www.googleapis.com/auth/contacts']

        # Appel de la fonction d'authentification
        service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        service.people().createContact(body={
            "organizations": [
                {
                    "name": self.nom_maison_retraite
                }
            ],
            "phoneNumbers": [
                {
                    'value': self.numero_telephone,
                    "type": self.nom_cadre_sante
                }
            ],
            "emailAddresses": [
                {
                    'value': self.adresse_email
                }
            ],
            "addresses": [
                {
                    "formattedValue": self.adresse_postale
                }
            ],
            "memberships": [
                {
                    "contactGroupMembership": {
                        "contactGroupResourceName": "contactGroups/1c576d7f8bd43294"
                    }
                }
            ]

        }).execute()


        # On efface les entrées pour eviter les doublons
        self.entry_nom_maison_retraite.delete(0, END)
        self.entry_nom_cadre_sante.delete(0, END)
        self.entry_numero_telephone.delete(0, END)
        self.entry_adresse_postale.delete(0, END)
        self.entry_adresse_email.delete(0, END)

    def bouton_effacer(self):
        self.entry_nom_maison_retraite.delete(0, END)
        self.entry_nom_cadre_sante.delete(0, END)
        self.entry_numero_telephone.delete(0, END)
        self.entry_adresse_postale.delete(0, END)
        self.entry_adresse_email.delete(0, END)

    def creer_fenetre(self):
        # Theme fenetre
        #self.title(bg = "white")
        style = ThemedStyle(self)
        style.theme_use('equilux')
        bg = style.lookup('TLabel', 'background')
        fg = style.lookup('TLabel', 'foreground')
        self.configure(bg=style.lookup('TLabel', 'background'))
        self.title("Panneau d'enregistrment des maisons de retraite")

        label_nom_maison_retraite = ttk.Label(self, text="Nom de la maison de retraite :")
        label_adresse_postale = ttk.Label(self, text="Adresse de la maison de retraite")
        label_nom_cadre_sante = ttk.Label(self, text="Nom de la cadre santé")
        label_numero_telephone = ttk.Label(self, text="Numéro de téléphone")
        label_adresse_email = ttk.Label(self, text="Adresse E-mail")

        self.entry_nom_maison_retraite = ttk.Entry(self, width=50)
        self.entry_adresse_postale = ttk.Entry(self, width=50)
        self.entry_nom_cadre_sante = ttk.Entry(self, width=50)
        self.entry_numero_telephone = ttk.Entry(self, width=50)
        self.entry_adresse_email = ttk.Entry(self, width=50)

        bouton_effacer = ttk.Button(self, text="EFFACER", command=self.bouton_effacer)
        bouton_enregistrer = ttk.Button(self, text="ENREGISTRER", command=self.bouton_enregistrer)

        label_nom_maison_retraite.grid(row=0, column=0)
        label_adresse_postale.grid(row=1, column=0)
        label_nom_cadre_sante.grid(row=2, column=0)
        label_numero_telephone.grid(row=3, column=0)
        label_adresse_email.grid(row=4, column=0)

        self.entry_nom_maison_retraite.grid(row=0, column=1)
        self.entry_adresse_postale.grid(row=1, column=1)
        self.entry_nom_cadre_sante.grid(row=2, column=1)
        self.entry_numero_telephone.grid(row=3, column=1)
        self.entry_adresse_email.grid(row=4, column=1)


        bouton_effacer.grid(row=5, column=0)
        bouton_enregistrer.grid(row=5, column=1)


albert = fenetreCreationContact()
albert.mainloop()


