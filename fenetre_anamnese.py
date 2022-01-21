import tkinter as tk
from tkinter import END


class FenetreAnamnese(tk.Tk):
    # Constructeur
    def __init__(self):
        tk.Tk.__init__(self)
        self.text_reponse = [0] * 15
        self.les_items = []
        self.les_labels = []
        self.les_texts = []
        self.creer_fenetre()

    # Définition du bouton tout effacer

    def fenetre_clear(self):
        print("On efface les listes")
        for i in range(len(self.les_items)):
            try:
                self.les_items[i].selection_clear(0, END)
            except:
                pass

    # Définition du bouton enregistrer
    def resultat_recolteur(self):
        for i in range(len(self.les_items)):
            if i == 6:
                self.text_reponse[i] = self.les_items[i].get()
                if self.text_reponse[i] == "":
                    print(f"remarque item {i} pas rempli")
                else:
                    print(self.text_reponse[i])
            else:
                try:
                    self.text_reponse[i] = self.les_items[i].get(self.les_items[i].curselection()[0])
                    print(self.text_reponse[i])
                except:
                    print(f"La liste {i} pas rempli")
        self.destroy()

    def creer_fenetre(self):
        # Paramètres initiaux
        self.resizable(False, False)
        self.title('Anamnèse')

        # Création des label
        label_cognition = tk.Label(self, text="Cognition :")
        label_dejaappareille = tk.Label(self, text="Patient déjà appareillé :")
        label_otoscopie = tk.Label(self, text="Otoscopie :")
        label_prisedempreinte = tk.Label(self, text="Prise d'empreinte :")
        label_remarque = tk.Label(self, text="Remarques :")
        label_avisduresident = tk.Label(self, text="Avis du résident (Si possible) :")
        label_conseildappareillage = tk.Label(self, text="Conseils d'appareillage :")
        label_dome_embout = tk.Label(self, text="Choix dome/embout")

        # Création des boutons
        bouton_fin = tk.Button(self, text="Enregistrer", command=self.resultat_recolteur)
        bouton_clear = tk.Button(self, text="Tout effacer", command=self.fenetre_clear)

        # Création des entrée
        list_cognition = tk.Listbox(self, height=5, width=25, exportselection=0)
        list_cognition.insert(1, "Bonne")
        list_cognition.insert(2, "Moyenne")
        list_cognition.insert(3, "Mauvaise")
        list_cognition.insert(4, "Non Appareillable")

        list_dejaappareille = tk.Listbox(self, height=4, width=25, exportselection=0)
        list_dejaappareille.insert(1, "NON")
        list_dejaappareille.insert(2, "OUI avec dome")
        list_dejaappareille.insert(3, "OUI avec embout")

        list_otoscopieOG = tk.Listbox(self, height=4, activestyle='underline', width=25,
                                      exportselection=0)
        list_otoscopieOG.insert(1, "Ok OG")
        list_otoscopieOG.insert(2, "Cerumen gênant OG")
        list_otoscopieOG.insert(3, "Bouchon OG")

        list_otoscopieOD = tk.Listbox(self, height=4, width=25, exportselection=0)
        list_otoscopieOD.insert(1, "Ok OD")
        list_otoscopieOD.insert(2, "Cerumen gênant OD")
        list_otoscopieOD.insert(3, "Bouchon OD")

        list_prisedempreinteOG = tk.Listbox(self, height=3, width=25, exportselection=0)
        list_prisedempreinteOG.insert(1, "OUI OG")
        list_prisedempreinteOG.insert(2, "NON OG")

        list_prisedempreinteOD = tk.Listbox(self, height=3, width=25, exportselection=0)
        list_prisedempreinteOD.insert(1, "OUI OD")
        list_prisedempreinteOD.insert(2, "NON OD")

        entry_remarque = tk.Entry(self, width=50)

        list_avisduresident = tk.Listbox(self, height=3, width=25, exportselection=0)
        list_avisduresident.insert(1, "OK")
        list_avisduresident.insert(2, "Contre")

        list_conseildappareillageOG = tk.Listbox(self, height=4, width=25, exportselection=0)
        list_conseildappareillageOG.insert(1, "BTE 312 M OG")
        list_conseildappareillageOG.insert(2, "BTE 13 P OG")
        list_conseildappareillageOG.insert(3, "BTE 675 HP OG")

        list_conseildappareillageOD = tk.Listbox(self, height=4, width=25, exportselection=0)
        list_conseildappareillageOD.insert(1, "BTE 312 M OD")
        list_conseildappareillageOD.insert(2, "BTE 13 P OD")
        list_conseildappareillageOD.insert(3, "BTE 675 HP OD")

        list_dome_emboutOG = tk.Listbox(self, height=9, width=25, exportselection=0)
        list_dome_emboutOG.insert(1, "Tube fin Dome open OG")
        list_dome_emboutOG.insert(2, "Tube fin Dome ferme OG")
        list_dome_emboutOG.insert(3, "Tube fin Dome double OG")
        list_dome_emboutOG.insert(4, "Gabarit court OG")
        list_dome_emboutOG.insert(5, "Gabarit moyen OG")
        list_dome_emboutOG.insert(6, "Gabarit long OG")
        list_dome_emboutOG.insert(7, "Tube fin Embout OG")
        list_dome_emboutOG.insert(8, "Tube gros Embout OG")

        list_dome_emboutOD = tk.Listbox(self, height=9, width=25, exportselection=0)
        list_dome_emboutOD.insert(1, "Tube fin Dome ouvert OD")
        list_dome_emboutOD.insert(2, "Tube fin Dome ferme OD")
        list_dome_emboutOD.insert(3, "Tube fin Dome double OD")
        list_dome_emboutOD.insert(4, "Gabarit court OD")
        list_dome_emboutOD.insert(5, "Gabarit moyen OD")
        list_dome_emboutOD.insert(6, "Gabarit long OD")
        list_dome_emboutOD.insert(7, "Tube fin Embout OD")
        list_dome_emboutOD.insert(8, "Tube gros Embout OD")

        # Disposition des éléments
        label_cognition.grid(row=0, column=0)
        label_dejaappareille.grid(row=1, column=0)
        label_otoscopie.grid(row=2, column=0)
        label_prisedempreinte.grid(row=3, column=0)
        label_remarque.grid(row=4, column=0)
        label_avisduresident.grid(row=5, column=0)
        label_conseildappareillage.grid(row=6, column=0)
        label_dome_embout.grid(row=7, column=0)

        list_cognition.grid(row=0, column=1)
        list_dejaappareille.grid(row=1, column=1)
        list_otoscopieOG.grid(row=2, column=1)
        list_otoscopieOD.grid(row=2, column=2)
        list_prisedempreinteOG.grid(row=3, column=1)
        list_prisedempreinteOD.grid(row=3, column=2)
        entry_remarque.grid(row=4, column=1, columnspan=2)
        list_avisduresident.grid(row=5, column=1)
        list_conseildappareillageOG.grid(row=6, column=1)
        list_conseildappareillageOD.grid(row=6, column=2)
        list_dome_emboutOG.grid(row=7, column=1)
        list_dome_emboutOD.grid(row=7, column=2)
        bouton_fin.grid(row=8, column=0)
        bouton_clear.grid(row=8, column=2)

        # Création de la liste contenant les réponses choisie
        les_item1 = [list_cognition, list_dejaappareille, list_otoscopieOG, list_otoscopieOD, list_prisedempreinteOG,
                     list_prisedempreinteOD]
        les_item2 = [entry_remarque, list_avisduresident, list_conseildappareillageOG, list_conseildappareillageOD,
                     list_dome_emboutOG]
        les_item3 = [list_dome_emboutOD]
        self.les_items = les_item1 + les_item2 + les_item3

        les_label1 = [label_cognition, label_dejaappareille, label_otoscopie, label_prisedempreinte, label_remarque]
        les_label2 = [label_avisduresident, label_conseildappareillage, label_dome_embout]
        self.les_labels = les_label1 + les_label2

        lestext1 = ["Cognition :", "Patient déjà appareillé :", "Otoscopie :", "Prise d'empreinte :", "Remarques :"]
        lestext2 = ["Avis du résident (Si possible) :", "Conseils d'appareillage :", "Choix dome/embout"]
        self.les_texts = lestext1 + lestext2